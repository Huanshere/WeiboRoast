# API 设置
OHMYGPT_API_KEY = ''  

# LLM 配置，你可以添加更多 API 如 openai, BASE_URL, MODEL
llm_config: list = [
    {
        'name': 'ohmygpt',
        'api_key': OHMYGPT_API_KEY,
        'base_url': 'https://apic.ohmygpt.com/',
        'model': ['deepseek-coder',
                  'deepseek-chat',
                  'gpt-4o', 
                  'claude-3-5-sonnet-20240620', 
                  'TA/Qwen/Qwen1.5-72B-Chat',
                  'TA/Qwen/Qwen1.5-110B-Chat',
                  'glm-4',
                  'gemini-1.5-pro-001',
                 'gemini-1.5-flash-001'],
    },
]

llm_support_json = ['deepseek-coder', 'gpt-4o']

# 需要去 weibo.cn 抓取 cookie, 用来获取微博内容
weibo_cookie =  """SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5q4PaQXn5Aqps8PKM8yApE5NHD95QN1KBpe02ESozpWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0.XeKepeoqEeBtt; _T_WM=10478669888; MLOGIN=1; SCF=AqXhPemzcZj_8q8wmFNql83dY2V8d4uO4z6pvlzxrz-SEHru08eJ5dFJARKtDge0Bwc7R0xVpYVHi5b3Nb65AbM.; SUB=_2A25LuCclDeRhGeFH71MS8SzKyT2IHXVotCbtrDV6PUJbktAGLVPYkW1Ne1IXQ2erdSkIPzfzUdrXYcDvKOalxqbN; SSOLoginState=1723619189; ALF=1726211189; M_WEIBOCN_PARAMS=luicode%3D20000174"""