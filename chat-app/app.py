import os
from openai import OpenAI

client = OpenAI()
# OpenAI APIキーを環境変数から取得
client.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # または"gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


# チャットのループ
print("ChatGPTにようこそ！ 'exit' と入力すると終了します。")
while True:
    user_input = input("あなた: ")
    if user_input.lower() == "exit":
        break
    response = chat_with_gpt(user_input)
    print("ChatGPT: " + response)
