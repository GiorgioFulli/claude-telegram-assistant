import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

reply = client.messages.create(
	model="claude-haiku-5-5",
	max_tokens=200,
	messages=[{"role": "user", "content": "Say hello to Giorgio in one sentence."}],
)

print(reply.content[0].text)
