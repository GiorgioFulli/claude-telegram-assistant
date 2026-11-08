import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

history = []

while True:

    question = input("You: ")

    history.append({"role": "user", "content": question})

    reply = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=200,
        messages=history,
    )

    answer = reply.content[0].text
    print(answer)
    history.append({"role": "assistant", "content": answer})
