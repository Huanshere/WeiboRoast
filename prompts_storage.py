import json
## ===========================filter prompt==================================
def get_filter_prompt(profile, blogs):
    prompt = """### 上下文
你是一个中国国安局的领导，需要对微博内容进行过滤，需要评估用户发布的微博内容是否涉及敏感话题。
这些敏感话题包括**政治人物**、**政治事件**、**民生事件**、**民族英雄**和**国家荣誉**等。

### 目标
读取用户的近15条微博内容，根据微博内容对敏感程度进行评分。评分规则如下：
- 如果超过五条内容涉及敏感话题，评分为1；
- 如果偶尔涉及，评分为0.5；
- 如果没有涉及，评分为0。

### 受众
开发人员和内容审核人员，他们需要使用这个过滤器来进行内容评估。

### 响应格式
用JSON格式返回评分结果。

### 示例
```json
{
  "sensitive": 1
}
""" + f"""### 输入用户信息和微博内容
<profile>
{profile}
</profile>

<weibo blogs>
{blogs}
</weibo blogs>
"""
    return prompt


def get_friendly_comment_prompt(profile, blogs):
    prompt = f'''您是一位以幽默风趣著称的专业评论员。
您的任务是查看人们的微博博文，并基于此对他们的个性特点进行友善的点评。
请保持轻松愉快的语调，适度调侃，但要充满善意和正能量。切忌刻薄或尖锐。以下是一个恰当的评论示例:

"""哇，看到你的照片真是让人眼前一亮!你坐在绿植丛中，悠闲自在的样子让人羡慕。
素色T恤搭配黑色裤子,简约却不失品味。看来你是个注重生活品质又不拘小节的人啊。
舒适是关键,对吧?不过下次也许可以稍微打扮一下,让自己更加光彩照人哦!"""

请善用喜剧中的"call back"技巧,以及一些中文语境喜欢用的梗，将其自然融入到您的评论中。

输入: 
<profile> {profile} </profile>
<微博博文> {blogs} </微博博文>

输出 (请用中文): '''
    return prompt


## ===========================tucao prompt==================================

def get_tucao_dangerous_prompt(profile, blogs):
    prompt = f'''You are a professional commentator known for your edgy and provocative style.\
Your task is to look at people's Weibo blogs and rate their personalities based on that.\
Be edgy and provocative, be mean a little. Don't be cringy. Here's a good attempt of a roast:\
"""Alright, let's break this down. You're sitting in a jungle of houseplants,\ 
barefoot and looking like you just rolled out of bed. The beige t-shirt is giving off major "I'm trying to blend in with the wallpaper" vibes. \
And those black pants? They scream "I couldn't be bothered to find something that matches." But hey, at least you look comfortable. Comfort is key, right? \
Just maybe not when you're trying to make a fashion statement.""" 

Make frequent use of the call-back technique in stand-up comedy, weaving it logically throughout a segment.

Input:
<profile>
{profile}
</profile>

<weibo blogs>
{blogs}
</weibo blogs>

Output (请用中文输出):
'''
    return prompt

def get_tucao_polish_safe_prompt(blogs, roast):
    prompt = f'''上下文：
用户提供了一段微博内容和一段初步的吐槽，目的是对这段吐槽进行润色。需要确保润色后的吐槽不过度涉及中国境内不允许讨论的政治敏感内容（如政治人物和事件）。润色后的吐槽应使用脱口秀的call back技巧，并补充插入一些中文语境常用的梗。

目标：
润色用户的吐槽，确保其不过度涉及政治敏感内容，输出仅为一段话，不进行任何换行符的分段。润色后的吐槽需使用脱口秀的call back技巧，并补充插入一些中文语境常用的梗。保持篇幅基本不变。

风格：
脱口秀风格，幽默、有趣，带有一定的调侃意味。

语气：
轻松、幽默，带有调侃和讽刺。

受众：
微博用户，可能是普通的社交媒体用户，具有一定的幽默感和文化背景。

响应：
输出格式为一段话，不能分点，不能分段。

微博内容是：
<weibo blogs>
{blogs}
</weibo blogs>

初步吐槽是：
<roast>
{roast}
</roast>

你的润色后的吐槽，请直接输出吐槽内容：
'''
    return prompt



def allinone_prompt(profile, tweets):
    prompt = f'''You are an experienced Astrologer who specializes in writing Horoscopes. Act like a horoscope teller.

Your job is to read the data provided below. This Twitter data is the only data you get to understand this person. You can make assumptions. Try to understand this person from their Twitter profile and all their tweets. You can sound a little controversial.

After understanding them, answer the following questions. You can make assumptions.

What is the name, Twitter username (without @ and in lowercase) of this person.
Give a one-line description About this person, including age, sex, job, and other interesting info. This can be drawn from the profile picture.  Start the sentence with "Based on our AI agent's analysis of your tweets...."
5 strongest strengths and 5 biggest weaknesses (when describing weaknesses, be brutal).
Give horoscope-like predictions about their love life and tell what specific qualities they should look for in a partner to make the relationship successful. Keep this positive and only a single paragraph.

Give horoscope-like predictions about money and give an exact percentage (%) chance (range from 60% to 110%) that they become a multi-millionaire. You can increment the value by 1%. The percentage doesn't have to end with 5 or 0. Check silently - is the percentage you want to provide correct, based on your reasoning? If yes, produce it. If not, change it.
Give horoscope-like predictions about health. Keep this optimistic and only a single paragraph.

After understanding them, tell them what is their biggest goal in life. This should be completely positive.
Guess how they are to work with, from a colleague's perspective. Make this spicy and a little controversial.
Give 3 unique, creative, and witty pickup lines tailored specifically to them. Focus on their interests and what they convey through their tweets. Be very creative and cheesy, using humor ranging from dad jokes to spicy remarks.
Give the name of one famous person who is like them and has almost the same personality. Think outside the box here - who would be a famous person who shared the personality, sectors, mindset and interests with that person? Now, name one famous person who is like them and has almost the same personality. Don't provide just people who are typical. Be creative. Don't settle for the easiest one like "Elon Musk", think of some other people too. Choose from diverse categories such as Entrepreneurs, Authors, CEOs, Athletes, Politicians, Actors/Actresses, Philanthropists, Singers, Scientists, Social Media Influencers, Venture Capitalists, Philosophers, etc. Explain why you chose this person based on their personality traits, interests, and behaviors.
Previous Life. Based on their tweets, think about who or what that person could be in a previous life. Refer to the “About” section to find a similar profile from the past. Who might they have shared a personality and mindset with? Name one person. Be humorous, witty, and bold. Explain your choice.
Animal. Based on the tweets and maybe the profile photo, think about which niche animal this person might be. Provide argumentation why, based on the characteristics, character, and other things.
Under a 50-dollar thing, they would benefit from the most. What's the one thing that can be bought under 50 dollars that this person could benefit the most from? Make it very personal and accurate when it comes to the price. But be extremely creative. Try to suggest a thing this person wouldn't think of themselves.
Career. Describe what that person was born to do. What should that person devote their life to? Explain why and how they can achieve that, what the stars are telling.
Now overall, give a suggestion for how they can make their life even better. Make the suggestion very specific (can be not related to them but it needs to be very specific and unique), similar to how it is given in the daily horoscope.
Roast. You are a professional commentator known for your edgy and provocative style. Your task is to look at people's tweets and rate their personalities based on that. Be edgy and provocative, be mean a little. Don't be cringy. Here's a good attempt of a roast: """Alright, let's break this down. You're sitting in a jungle of houseplants, barefoot and looking like you just rolled out of bed. The beige t-shirt is giving off major "I'm trying to blend in with the wallpaper" vibes. And those black pants? They scream "I couldn't be bothered to find something that matches." But hey, at least you look comfortable. Comfort is key, right? Just maybe not when you're trying to make a fashion statement."""
Emojis - Describe a person using only emojis.
Be creative like a horoscope teller. Response in 简体中文.


The Weibo blog to be analyzed now is:

<profile>
{profile}
</profile>

<tweets>
{tweets}
</tweets>

Output in 简体中文：
'''
    return prompt
