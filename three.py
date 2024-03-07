from two import l1
import openai
import numpy as np
openai.api_key = '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'

s=''
for i in l1:
    s=s+i
# print(s)
def get_summary(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # Adjust this for randomness
    )
    return response.choices[0].message["content"]

prompt = f"""
TASKS:
Your task is to summarize given string and return in point-to-point wise.

Do the above tasks for s.

Review: ```{s}```
"""

summary=get_summary(prompt=prompt)

print(summary)