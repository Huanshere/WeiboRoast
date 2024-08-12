import streamlit as st
import json
from ask_gpt import ask_gpt
from prompts_storage import get_prompt
from weibo import weibo_for_tucao

def tucao_main(share_link: str, max_blogs: int = 20):
    user_id = share_link.split('/u/')[-1]
    user_id_list = [user_id]
    screen_names = weibo_for_tucao(user_id_list, max_blogs)[0]

    with open(f'weibo/{screen_names}/{user_id}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    profile = f"{data['user']['screen_name']}, {data['user']['verified_reason']}\n{data['user']['description']}"
    blogs= '\n'.join([weibo['text'] for weibo in data['weibo'][:max_blogs]])

    tucao_prompt = get_prompt(profile=profile, blogs=blogs)
    response = ask_gpt(tucao_prompt, model='claude-3-5-sonnet-20240620', response_json=False)
    return response

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
    if not '/u' in share_link:
        st.error("🚫 请输入正确的微博分享链接 仅支持带/u/的链接")
        st.stop()
    with st.spinner("👿 正在生成吐槽..."):
        response = tucao_main(share_link).strip()
    
    with st.container():
        st.markdown(f'<div class="output-card"><h3>吐槽 😄</h3>{response}</div>', unsafe_allow_html=True)
    
    st.balloons()