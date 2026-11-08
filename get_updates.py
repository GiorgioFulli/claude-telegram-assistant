import os
import requests


telegram_token = os.environ["CLAUDEBOT_TELEGRAM_TOKEN"]
address_in = f"https://api.telegram.org/bot{telegram_token}/getUpdates"

offset = 0
result = requests.get(address_in, params={"offset": offset})
print(result.status_code)
updates = result.json()
my_id = int(os.environ["CLAUDEBOT_CHAT_ID"])

for update in updates["result"]:
    if update["message"]["from"]["id"] == my_id:
        print(update["message"]["text"])
    offset = update["update_id"] + 1
print(offset)

