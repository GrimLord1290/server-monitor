import os
from dotenv import load_dotenv
import psutil
import requests
import time

load_dotenv()

# ВСТАВЬ СВОЙ ТОКЕН БОТА
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ВСТАВЬ СВОЙ CHAT_ID
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        pass

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    alerts = []

    if cpu > 80:
        alerts.append(f"🔥 CPU: {cpu}%")
    if memory > 80:
        alerts.append(f"💾 Память: {memory}%")
    if disk > 80:
        alerts.append(f"💿 Диск: {disk}%")

    if alerts:
        message = "⚠️ ВНИМАНИЕ! Превышены лимиты:\n" + "\n".join(alerts)
        send_telegram(message)
        print(message)
    else:
        print(f"✅ Всё ок. CPU: {cpu}%, Память: {memory}%, Диск: {disk}%")

if __name__ == "__main__":
    print("Мониторинг запущен. Проверка каждые 60 секунд...")
    while True:
        check_system()
        time.sleep(60)