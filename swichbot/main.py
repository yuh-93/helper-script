import json, os, requests
from dotenv import load_dotenv

API_HOST = "https://api.switch-bot.com"
load_dotenv()
OPEN_TOKEN = os.getenv("OPEN_TOKEN")
DEBIVELIST_URL = f"{API_HOST}/v1.0/devices"

HEADERS = {
    "Authorization": OPEN_TOKEN,
    "Content-Type": "application/json; charset=utf8",
}


def _get_request(url):
    res = requests.get(url, headers=HEADERS)
    data = res.json()
    if data["message"] == "success":
        return res.json()
    return {}
