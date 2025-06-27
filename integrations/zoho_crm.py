# integrations/zoho_crm.py

import requests
import os

# Static config
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN") or "your token"
CLIENT_ID = "ID"
CLIENT_SECRET = "Secret"
API_DOMAIN = "https://www.zohoapis.in"

ACCESS_TOKEN = None  # global cache

def refresh_access_token():
    url = "https://accounts.zoho.in/oauth/v2/token"
    params = {
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token"
    }
    r = requests.post(url, params=params)
    print("🔁 Refresh response:", r.status_code, r.text)
    if r.status_code == 200 and "access_token" in r.json():
        new_token = r.json()["access_token"]
        print("✅ Refreshed Zoho Access Token")
        return new_token
    else:
        print("❌ Zoho token refresh failed:", r.text)
        return None

def get_headers():
    global ACCESS_TOKEN
    if ACCESS_TOKEN is None:
        ACCESS_TOKEN = refresh_access_token()

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    # Validate access token
    test = requests.get(f"{API_DOMAIN}/crm/v2/settings/modules", headers=headers)
    if test.status_code == 401:
        print("🔒 Token expired, refreshing...")
        ACCESS_TOKEN = refresh_access_token()
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"

    return headers

def create_lead(lead_dict):
    name = lead_dict.get("name", "Unknown")  # Not full_name
    email = lead_dict.get("email", "")
    phone = lead_dict.get("phone", "")

    url = f"{API_DOMAIN}/crm/v2/Leads"
    payload = {
        "data": [{
            "Last_Name": name,
            "Email": email,
            "Phone": phone,
            "Lead_Source": "Chatbot"
        }]
    }

    r = requests.post(url, headers=get_headers(), json=payload)

    if r.status_code == 201:
        print("✅ Zoho lead created!")
        return r.json()
    else:
        print("❌ Zoho lead creation failed:", r.text)
        return None
