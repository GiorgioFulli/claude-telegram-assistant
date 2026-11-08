import os
import requests

telegram_token = os.environ["CLAUDEBOT_TELEGRAM_TOKEN"]
chat_id = os.environ["CLAUDEBOT_CHAT_ID"]
address = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
text = "Hello from Mac 2.0"
content_to_send = {"chat_id": chat_id, "text": text}
result = requests.post(address, data=content_to_send) 
print(result.status_code)

