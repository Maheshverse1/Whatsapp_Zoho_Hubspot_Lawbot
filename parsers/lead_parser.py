# parsers/lead_parser.py

def parse_lead(user_info, phone):
    name = user_info.get("name", "Unknown")
    return {
        "name": name,         # used by Zoho
        "full_name": name,    # used by HubSpot
        "email": user_info.get("email", ""),
        "phone": phone
    }
