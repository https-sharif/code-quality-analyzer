import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
r = requests.get("https://api.github.com/rate_limit", headers={"Authorization": f"token {GITHUB_TOKEN}"})

print("Status code:", r.status_code)
print("Response text:", r.text)