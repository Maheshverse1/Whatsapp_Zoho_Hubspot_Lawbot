# integrations/crm_router.py

import json
import os
from integrations.zoho_crm import create_lead as create_zoho_lead
from integrations.hubspot_crm import create_lead as create_hubspot_lead

# Load active CRM from config file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'crm_config.json')

def get_active_crm():
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            return config.get("active_crm", "zoho")
    except Exception as e:
        print("⚠️ Failed to load CRM config:", e)
        return "zoho"

def create_lead(lead_data):
    crm = get_active_crm()
    if crm == "zoho":
        return create_zoho_lead(lead_data)  # ✅ pass dict directly
    elif crm == "hubspot":
        return create_hubspot_lead(lead_data)  # ✅ pass dict directly
    else:
        print(f"❌ Unsupported CRM: {crm}")
        return None
