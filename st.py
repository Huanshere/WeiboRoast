import streamlit as st
import json
from ask_gpt import ask_gpt
from prompts_storage import get_tucao_dangerous_prompt, get_tucao_polish_safe_prompt, get_filter_prompt, get_friendly_comment_prompt
from weibo import weibo_for_tucao

def crawl_weibo(share_link: str, max_blogs: int = 15):
    user_id = share_link.split('/u/')[-1]
    user_id_list = [user_id]
    screen_names = weibo_for_tucao(user_id_list, max_blogs)[0]

    try:
        with open(f'weibo/{screen_names}/{user_id}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        st.error("😣 无法获取微博内容 请换一个博主试试")
        st.stop()

    profile = f"{data['user']['screen_name']}, {data['user']['verified_reason']}\n{data['user']['description']}"
    blogs = '\n'.join([weibo['text'] for weibo in data['weibo'][:max_blogs]])
    
    return profile, blogs

def filter_content(profile: str, blogs: str, user_id: str):
    filter_prompt = get_filter_prompt(profile=profile, blogs=blogs)
    filter_response = ask_gpt(filter_prompt, model='deepseek-coder', response_json=True, log_title=user_id)
    print(filter_response)
    sensitive_point = filter_response['sensitive']
    print(f"敏感度评分：{sensitive_point}")
    return float(sensitive_point)

def generate_friendly_comment(profile: str, blogs: str, user_id: str):
    friendly_comment_prompt = get_friendly_comment_prompt(profile=profile, blogs=blogs)
    friendly_comment_response = ask_gpt(friendly_comment_prompt, model='TA/Qwen/Qwen1.5-72B-Chat', response_json=False, log_title=user_id)
    fc_response = friendly_comment_response.replace('\n\n', '').replace('\n', '')
    print(fc_response)
    return fc_response

def generate_tucao(profile: str, blogs: str, user_id: str):
    tucao_dangerous_prompt = get_tucao_dangerous_prompt(profile=profile, blogs=blogs)
    tucao_dangerous = ask_gpt(tucao_dangerous_prompt, model='claude-3-5-sonnet-20240620', response_json=False, log_title=user_id)
    print(f"初步吐槽：\n{tucao_dangerous}")
    tucao_polish_safe_prompt = get_tucao_polish_safe_prompt(blogs=blogs, roast=tucao_dangerous)
    tucao_safe = ask_gpt(tucao_polish_safe_prompt, model='TA/Qwen/Qwen1.5-72B-Chat', response_json=False, log_title=user_id)
    print(f"润色后的吐槽：\n{tucao_safe}")
    tucao_safe = tucao_safe.replace('\n\n', '').replace('\n', '') 
    return tucao_safe


st.set_page_config(layout="centered", page_title="微博吐槽大会", page_icon="🤭")

st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .output-card {
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        padding: 20px;
        margin-top: 20px;
        background-color: #f9f9f9;
    }
    .emoji {
        font-size: 24px;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤭 微博吐槽大会")
st.markdown("")
share_link = st.text_input("📎 输入博主的分享链接", help="例如: https://weibo.com/u/2751313073 目前仅支持带/u/的")


if share_link:
    if '/u' not in share_link:
        st.error("🚫 请输入正确的微博分享链接 仅支持带/u/的链接")
        st.stop()
    
    with st.spinner("📱 正在搜集微博内容..."):
        profile, blogs = crawl_weibo(share_link)
    
    
    with st.spinner("👀 正在过滤敏感内容..."):
        sensitive_point = filter_content(profile, blogs, share_link.split('/u/')[-1])

        if sensitive_point ==0 :
            with st.spinner("👿 正在吐槽..."):
                response = generate_tucao(profile, blogs, share_link.split('/u/')[-1]).strip()
        else:
            with st.spinner("😯 正在思考..."):
                response = generate_friendly_comment(profile, blogs, share_link.split('/u/')[-1]).strip()
    
    with st.container():
        st.markdown(f'<div class="output-card"><h3>吐槽 😄</h3>{response}</div>', unsafe_allow_html=True)
    
    st.balloons()