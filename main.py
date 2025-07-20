import telegram
import requests
import time

BOT_TOKEN = '8049852462:AAF8uRczEwylqGaKK9wstitv0wiD5BE7VaU'
CHAT_ID = 7515706665

WALLETS = [
    "0x100f4a6d8713e0df271f25323f9d9399496ff179",
    "0xe4178ba889ac1c931861533b98bb86cb9d4858c7"
]

seen = set()
bot = telegram.Bot(token=BOT_TOKEN)

def check_wallets():
    for w in WALLETS:
        url = f"https://api.solscan.io/account/transactions?address={w}&limit=1"
        try:
            data = requests.get(url).json()
            if isinstance(data, list) and len(data):
                tx = data[0].get("txHash")
                if tx and tx not in seen:
                    seen.add(tx)
                    bot.send_message(chat_id=CHAT_ID, text=f"تراکنش جدید:\n{w}\n{tx}")
        except:
            pass

while True:
    check_wallets()
    time.sleep(15)
