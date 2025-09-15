import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

r = requests.get("https://api.github.com/rate_limit", headers=headers)

print("Status code:", r.status_code)
print("Response text:", r.text)