import anthropic

client = anthropic.Anthropic() #This creates the client, which holds my API key and sends requests to Anthropic

reply = client.messages.create(model="claude-haiku-5-5", max_tokens=200, messages=[{"role": "user", "content": "What is the capital of Italy?"}]) #This is an action done through the client object

print(reply.content[0].text)
print(f"Tokens IN: {reply.usage.input_tokens}, Tokens OUT: {reply.usage.output_tokens}")
