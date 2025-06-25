
# 🪙 CryptoDataAgent — Real-Time Crypto Price Agent

This project uses the [OpenAI Agents SDK](https://github.com/openai/agents) with Gemini API to provide real-time cryptocurrency prices using the [CoinLore API](https://www.coinlore.com/cryptocurrency-data-api).

## 🚀 Features

- Uses Gemini (`gemini-2.0-flash`) model via OpenAI Agent SDK
- Supports real-time price queries for coins (e.g., BTC, ETH)
- Fully customizable agent tools
- Simple CLI-based input/output
- Async support for faster execution

## 📦 Requirements

Make sure to install dependencies:

```bash
pip install -r requirements.txt
requirements.txt
text
Copy
Edit
requests
python-dotenv
agents  # from OpenAI Agents SDK (install with pip)
🔐 Environment Setup
Create a .env file with your Gemini API key:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
🧠 How It Works
A function tool get_crypto_price is defined to fetch real-time data.

An Agent is created that only responds to coin-related questions.

The input from the user is processed via Runner.run().

📈 Example
bash
Copy
Edit
$ python crypto_agent.py
What do you want to ask? Bitcoin price
Fetched Price: 64537.23
Bitcoin (BTC) is currently trading at $64537.23

![get crypto price](https://github.com/user-attachments/assets/874e0899-4b3e-42f2-8134-cb705652ae26)
![crypto rate](https://github.com/user-attachments/assets/865b039c-0e08-416f-a5dd-caeb66687813)
