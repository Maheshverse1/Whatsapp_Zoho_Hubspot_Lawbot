import requests

CLIENT_ID = "1000.NS5C6OAOP68WI89UFDPBSCRNQID4FN"
CLIENT_SECRET = "825cd97425a1f6aa3057791de596cc047442bb3254"
REFRESH_TOKEN = "1000.a623d4251c605355414edc90c2eb1ffb.ab8a710df2ce0d5fd69ff49b7f73fba9"

url = "https://accounts.zoho.in/oauth/v2/token"
params = {
    "refresh_token": REFRESH_TOKEN,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "refresh_token"
}

response = requests.post(url, params=params)
print("Status:", response.status_code)
print("Response:", response.json())
