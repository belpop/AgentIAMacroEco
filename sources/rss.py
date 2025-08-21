import feedparser, hashlib

IMPORTANT_FEEDS = [
    "https://www.reuters.com/markets/rss",
    "https://www.ecb.europa.eu/press/govcdec/rss/en.rss",
    "https://www.federalreserve.gov/feeds/press_all.xml",
    "https://www.bankofengland.co.uk/news/news/rss",
]

KEYWORDS = [
    "rates", "hikes", "cuts", "inflation", "cpi", "unemployment", "gdp",
    "pmi", "sanctions", "stimulus", "qe", "taper", "guidance", "energy"
]

G20 = ["United States", "China", "Euro zone", "Japan", "Germany", "France",
       "UK", "India", "Brazil", "Canada", "Russia", "Italy", "Australia",
       "Mexico", "South Korea", "Saudi Arabia", "Turkey", "Indonesia",
       "Argentina", "South Africa"]

def score_item(item: dict) -> int:
    title = (item.get("title") or "").lower()
    summary = (item.get("summary") or "").lower()
    score = 0
    if any(k in (item.get("link") or "") for k in ["ecb.europa.eu", "federalreserve.gov",
                                                   "bankofengland.co.uk", "boj.or.jp"]):
        score += 30
    if any(k in title or k in summary for k in KEYWORDS):
        score += 20
    if any(c.lower() in title or c.lower() in summary for c in [g.lower() for g in G20]):
        score += 10
    if any(k in title for k in ["oil", "brent", "wti", "gas", "usd", "treasuries", "ust"]):
        score += 10
    return score

def item_hash(item: dict) -> str:
    base = (item.get("link") or "") + (item.get("title") or "")
    return hashlib.sha256(base.encode()).hexdigest()

def fetch_items():
    for url in IMPORTANT_FEEDS:
        feed = feedparser.parse(url)
        for e in feed.entries:
            yield {
                "source": url,
                "title": e.get("title"),
                "summary": e.get("summary"),
                "link": e.get("link"),
                "published": e.get("published"),
                "hash": item_hash(e),
                "score": score_item({"link": e.get("link"), "title": e.get("title"), "summary": e.get("summary")}),
            }
