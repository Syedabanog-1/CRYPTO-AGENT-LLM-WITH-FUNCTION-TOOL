import os
import requests
import asyncio
import dotenv

from agents import (
    OpenAIChatCompletionsModel,
    Agent,
    Runner,
    set_tracing_disabled,
    AsyncOpenAI,
    function_tool
)

# ✅ Load environment variables
dotenv.load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# ✅ Disable tracing (optional for debugging)
set_tracing_disabled(True)

# ✅ Setup Gemini client
client = AsyncOpenAI(
    base_url='https://generativelanguage.googleapis.com/v1beta/openai/.',
    api_key=GEMINI_API_KEY
)

# ✅ Setup OpenAI Model using Gemini
model = OpenAIChatCompletionsModel('gemini-2.0-flash', openai_client=client)

# ✅ Function Tool to fetch crypto prices
@function_tool
def get_crypto_price(name: str):
    print(f"Getting {name} Price...")
    coins = requests.get("https://api.coinlore.net/api/tickers/").json()["data"]

    for coin in coins:
        if coin['name'].lower() == name.lower() or \
           coin['symbol'].lower() == name.lower() or \
           coin['nameid'] == name.lower():
            price = coin['price_usd']
            print(f"Fetched Price: {price}")
            return {
                "name": coin["name"],
                "symbol": coin["symbol"],
                "price_usd": price
            }

    return {"error": f"Coin '{name}' not found."}

# ✅ Define the Crypto Agent
CryptoDataAgent = Agent(
    name='CryptoDataAgent',
    instructions=(
        "You are a Crypto Agent. You provide real-time rates using get_crypto_price tool. "
        "EXPECT the user always asks about coins. NEVER respond to any other TOPIC."
    ),
    model=model,
    tools=[get_crypto_price]
)

# ✅ Main program
user_question = input("What do you want to ask? ")

async def main():
    results = await Runner.run(CryptoDataAgent, user_question)
    print(results.final_output)

asyncio.run(main())
