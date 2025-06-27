# integrations/hubspot_crm.py

import requests
import os

# Load token safely
HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN") or "tokenpaste"
HUBSPOT_API_URL = "https://api.hubapi.com/crm/v3/objects/contacts"

def create_lead(lead_data):
    full_name = lead_data.get("full_name", "Unknown User")
    email = lead_data.get("email", "")
    phone = lead_data.get("phone", "")

    # Split full name into firstname and lastname for HubSpot
    name_parts = full_name.strip().split(" ", 1)
    firstname = name_parts[0]
    lastname = name_parts[1] if len(name_parts) > 1 else "User"

    headers = {
        "Authorization": f"Bearer {HUBSPOT_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "properties": {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "lifecyclestage": "lead"
        }
    }

    response = requests.post(HUBSPOT_API_URL, headers=headers, json=payload)
    print("📤 HubSpot response:", response.status_code, response.text)

    if response.status_code == 201:
        print("✅ HubSpot lead created!")
        return response.json()
    else:
        print("❌ HubSpot lead creation failed:", response.text)
        return None
