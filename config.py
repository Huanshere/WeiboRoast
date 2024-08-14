# API 设置
OHMYGPT_API_KEY = ''  

# LLM 配置，你可以添加更多 API 如 openai, BASE_URL, MODEL
llm_config: list = [
    {
        'name': 'ohmygpt',
        'api_key': OHMYGPT_API_KEY,
        'base_url': 'https://api.ohmygpt.com',
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