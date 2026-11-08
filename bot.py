import os
import requests
import anthropic

telegram_token = os.environ["CLAUDEBOT_TELEGRAM_TOKEN"]
address_out = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
address_in = f"https://api.telegram.org/bot{telegram_token}/getUpdates"
my_id = int(os.environ["CLAUDEBOT_CHAT_ID"])
offset = 0
client = anthropic.Anthropic()
history = []
system_prompt = "You are Mac 2.0, a Telegram assistant for Giorgio. Your answers should be short as they are read on a phone."

while True:
    timeout = 30
    result = requests.get(address_in, params={"offset": offset, "timeout": timeout}, timeout=40)
    print(result.status_code)
    updates = result.json()

    for update in updates["result"]:
        if update["message"]["from"]["id"] == my_id:
            print(update["message"]["text"]) #Telegram message shown on the Terminal
            history.append({"role": "user", "content": update["message"]["text"]})
            reply = client.messages.create(model="claude-haiku-5-5", max_tokens=4000, messages=history, system=system_prompt) #The whole conversation is sent to Claude and the answer is stored in reply
            answer = ""
            for block in reply.content:
                if block.type == "text":
                    answer = block.text
            history.append({"role": "assistant", "content": answer})
            sent = requests.post(address_out, data={"chat_id": my_id, "text": answer}) #Sends Claude's answer to Telegram's chat
            print(answer)
            print(f"Tokens IN: {reply.usage.input_tokens}, Tokens OUT: {reply.usage.output_tokens}")
        offset = update["update_id"] + 1
