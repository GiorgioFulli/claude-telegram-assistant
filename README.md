# Claude Telegram Assistant

A Telegram bot that sends my messages to Claude (Anthropic's API) and replies in the chat. It runs on a 2011 MacBook Air I converted into a headless Ubuntu server.

## What it does
- Receives my Telegram messages and replies using Claude Haiku
- Keeps conversation history within a session, guided by a system prompt
- Uses a 40-second timeout on Telegram requests (tested by forcing one)

## How it's built
- Python, the Anthropic Python SDK, and the Telegram Bot API
- API keys and tokens stored outside the code in permission-restricted files
- Hosted on Ubuntu Server 24.04, managed over SSH, with Tailscale for remote access
- I typed and tested every script myself, step by step, with Claude as a tutor explaining each line. I'm now taking Harvard's CS50 Python course to build the skill to write code like this from a blank page.

## Files
- `bot.py`: the bot
- `crm.py`: the start of a CRM lookup tool (test data only)
- `hello.py`, `ask_once.py`, `chatloop.py`, `hello_telegram.py`, `get_updates.py`: the step-by-step scripts I built along the way
- `KNOWN_ISSUES.md`: problems found and how they were handled

## Status
Works end to end when started manually over SSH. History resets on restart.
Next: let Claude look up the test CRM data through tool use.
