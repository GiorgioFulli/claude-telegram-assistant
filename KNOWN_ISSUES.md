# Known Issues: Mac 2.0 (bot.py)

How to use this file: one entry per problem. Write what you saw (symptom), why it happens (cause), how bad it is (impact), and how to fix it. Change the status when it's fixed, but don't delete the entry. The record of what broke and why is the useful part.

Status values: OPEN, IN PROGRESS, FIXED, WON'T FIX (by design)

---

## 1. Bot freezes silently if the network drops
- **Status:** FIXED
- **Found:** 8 Oct 2026
- **Symptom:** No "200" printed, no reply in Telegram, nothing in the terminal. The script looks alive but does nothing.
- **Cause:** `requests.get` has no client-side timeout. The `"timeout": 30` inside `params` is an instruction to Telegram, not to `requests`. If the connection dies, `requests` waits forever.
- **Impact:** High once the bot runs as a service (step 7). It would sit frozen with no error and no restart.
- **Fix:** Add `timeout=40` as a keyword argument to `requests.get`. Must be longer than Telegram's 30 seconds. Note: this turns a silent freeze into a visible crash (ReadTimeout). Catching that error with try/except is a later improvement.

## 2. Sticker, photo, or voice message crashes the script
- **Status:** OPEN
- **Symptom:** KeyError: 'text'
- **Cause:** Non-text messages have no "text" key, and `update["message"]["text"]` assumes there is one.
- **Impact:** High. The crash happens before `offset` is updated, so Telegram sends the same message again on every restart and the bot crashes again immediately (crash loop).
- **Fix idea:** Check that "text" exists before using it, and skip the message otherwise.

## 3. Edited message crashes the script
- **Status:** OPEN
- **Symptom:** KeyError: 'message'
- **Cause:** When you edit a message, Telegram sends an update with the key "edited_message" instead of "message".
- **Impact:** High. Same crash loop as issue 2.
- **Fix idea:** Check that "message" exists in the update before reading it, and skip the update otherwise.

## 4. Claude refusal is not handled
- **Status:** OPEN
- **Symptom:** Not seen yet.
- **Cause:** Haiku 5.5 can return stop_reason "refusal". The reply may contain no text block, so `answer` stays "".
- **Impact:** Unknown, not tested. Telegram rejects an empty message, so you would get no reply. An empty assistant message in `history` may also cause an error on the next call.
- **Fix idea:** If `answer` is empty, send a fallback message and don't add the empty answer to `history`.

## 5. Any API error crashes the script
- **Status:** OPEN
- **Symptom:** Traceback from anthropic (for example an overloaded or rate-limit error) or from requests.
- **Cause:** No error handling (try/except) anywhere in the loop.
- **Impact:** Medium. One temporary error from Claude or Telegram stops the bot.
- **Fix idea:** try/except around the Claude call and the Telegram calls. Learn try/except first.

## 6. Failed Telegram sends are ignored
- **Status:** OPEN
- **Symptom:** Claude's answer prints in the terminal but never arrives in Telegram.
- **Cause:** The result of `requests.post` is stored in `sent` but never checked.
- **Impact:** Low to medium. Also affects replies over Telegram's 4096-character limit, which are rejected.
- **Fix idea:** Print `sent.status_code`. Anything other than 200 means the send failed.

## 7. Conversation history resets when the script restarts
- **Status:** WON'T FIX for now (by design)
- **Cause:** `history` only exists in memory while the script runs.
- **Impact:** Low. Accepted limitation; the memory goal was dropped in favour of the agent.

## 8. ask_once.py and chatloop.py crash on Haiku 5.5
- **Status:** OPEN (low priority)
- **Cause:** They use `reply.content[0].text`, but the first block can be a thinking block with no `.text`.
- **Impact:** Only matters if those scripts are run again.
- **Fix idea:** Same block loop as bot.py, or delete the scripts.

## 9. Housekeeping
- **Status:** OPEN
- `.bak` files from the sed model-ID replacement are still in ~/claudebot.
- An empty file from the misspelled filename on 8 Oct is probably there too. Check with `ls -l ~/claudebot/` and remove 0-byte files you don't need.
