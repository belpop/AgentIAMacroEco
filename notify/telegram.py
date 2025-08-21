import os, httpx

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID")

async def send_alert(title: str, link: str):
    if not BOT_TOKEN or not CHAT_ID:
        return
    text = f"⚠️ Alerte macro\n{title}\n{link}"
    async with httpx.AsyncClient(timeout=10) as client:
        await client.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
            "chat_id": CHAT_ID, "text": text, "disable_web_page_preview": True
        })
