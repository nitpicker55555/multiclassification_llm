import json
import re


def dict_extract(text):
    # Extract JSON-like string
    start = text.find('{')
    end = text.rfind('}') + 1  # Include the closing '}'
    json_like_str = text[start:end]

    # Replace Python's True/False with JSON's true/false
    json_like_str = json_like_str.replace("True", "true").replace("False", "false")

    # Add double quotes around the keys and replace single quotes with double quotes in the values
    json_like_str = re.sub(r"([{,]\s*)(\w+)(\s*:\s*)([^,}\s]+)", r'\1"\2"\3"\4"', json_like_str)

    # Handle special case where values are lists
    json_like_str = re.sub(r'"\[', '[', json_like_str)
    json_like_str = re.sub(r'\]"', ']', json_like_str)

    try:
        # Parse the modified string as JSON
        json_like_str = json.loads(json_like_str)
    except json.JSONDecodeError as e:
        # Return error message for debugging
        return {"error": str(e), "string": json_like_str}

    return json_like_str

# Extract the JSON-like string
dict_={  "Military Deployment": [
    "tacoma",
    "lewis-mcchord",
    "afghan villager",
    "iraq deployment",
    "afghanistan deployment",
    "rogue base",
    "kandahar province",
    "2-3 infantry",
    "court-martial",
    "war trophie",
    "hashish abuse",
    "madigan army medical center",
    "medical retirement",
    "gi voice",
    "jennifer mcbride",
    "weekend rampage",
    "seattle time",
    "thomson reuter",
    "hong kong",
    "cnn",
    "british military",
    "colonel blimp",
    "dad's army",
    "us assessment",
    "queen's devotion",
    "gulf war",
    "guardian report",
    "george bush",
    "tony blair",
    "iraq war",
    "military prestige",
    "british society",
    "royal family",
    "class divide",
    "freedom of information",
    "regimental life",
    "public school",
    "us soldier",
    "uk soldier",
    "military budget",
    "military history",
    "military stereotype",
    "finest hour",
    "world war ii",
    "waterloo",
    "manchester"
  ],
  "Wartime Atrocities": [
    "wartime atrocitie",
    "premeditated murder",
    "unarmed civilian",
    "2010 murder",
    "series of scandal"
  ],
  "War": [
    "suicide",
    "leadership problem",
    "mental health",
    "chain of command"
  ],
  "Medical Center": [
    "madigan army medical center"
  ],
  "Green Schools": [
    "gcse",
    "recycling",
    "green school",
    "student-led",
    "rachel pickering",
    "green movement",
    "henry greenwood",
    "kingsmead school",
    "eco-school",
    "solar panel",
    "green flag",
    "sustainability",
    "communication"
  ],
  "Environmental Movement": [
    "environmental audit"
  ],
  "Geography Curriculum": [],
  "Sustainable Development": [],
  "Environmental Impact": [],
  "Western Capital": [],
  "Geographic Location": [],
  "Aid Work": [],
  "Western Organizations": [],
  "Management and Experience": [],
  "Neo-Colonialism": [],
  "machine learning": [],
  "large-language model": [],
  "Automation and Employment": [
    "artificial intelligence",
    "job automation",
    "ai exposure",
    "generative ai",
    "chatbot",
    "gpt-4",
    "coding",
    "website creation",
    "job losse",
    "productivity",
    "gdp growth",
    "labor market",
    "job creation"
  ],
  "Technology Procurement": [],
  "Geographic Information Systems": [],
  "Encryption and Data Protection": [],
  "Gender Identity": [],
  "Socialization and Independence": [],
  "Religious Education": [],
  "Public Service": [],
  "Transgender Rights": [],
  "Political Funding": [],
  "Renewable Energy": [],
  "Climate Debt": [],
  "Carbon Tax": [],
  "Green Technologies": [],
  "Sustainable Fashion": [],
  "Carbon Footprint": [],
  "Army": [],
  "War": []}
extracted_json_str = dict_extract(str(dict_))
print(extracted_json_str)
