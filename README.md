# 微博吐槽大会 WeiboRoast

微博吐槽大会是一个仿照wordware的毒舌AI，集成了微博数据抓取、处理、分析和生成幽默毒舌评论的自动化系统，通过weibo-crawler爬取指定用户的近20条原创微博，然后调用 GPT 模型生成对微博用户的"吐槽"。

## 快速开始

方法1. [下载 Windows 一键启动包](https://pan.baidu.com/s/15t1o2Bnu-pJuEL_Y6BA3fg?pwd=rt0p) ，在`config.py`中填写key后`一键启动.bat`

方法2. 从源码安装： 

    pip install -r requirements.txt
    streamlit run st.py
   

## 使用方法

1. 在 `config.py` 中填写API 密钥（可以自定义配置所有模型）。
2. 双击 `一键启动.bat` 运行程序（默认使用 sonnet 模型，每次使用约 1 毛钱）。

![演示](https://github.com/user-attachments/assets/8ff73c11-dbe8-49e3-aa89-800de64ce0ce)

## 高级用法

- 修改 `prompts_storage.py` 中的提示以自定义 AI 生成的内容
- 修改 `st.py` 中的 `model` , 推荐效果 sonnet > Qwen1.5 72B > deepseek-coder

## 致谢

本项目直接使用了 [weibo-crawler](https://github.com/dataabc/weibo-crawler) 的代码。