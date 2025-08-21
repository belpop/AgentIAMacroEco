import asyncio
from sources.rss import fetch_items
from notify.telegram import send_alert

SEEN = set()

async def tick():
    for item in fetch_items():
        if item["hash"] in SEEN:
            continue
        SEEN.add(item["hash"])  # en prod: stocker en DB
        if item["score"] >= 60:
            await send_alert(item["title"], item["link"])

async def main():
    while True:
        try:
            await tick()
        except Exception as e:
            print("error:", e)
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
