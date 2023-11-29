import random

# Expanded dictionary format
expanded_dict = {}

# Original dictionary structure
tech_categories = {
    "AI": ["ai", "chatgpt", "openai", "deep learning", "llm", "machine learning", "image generator", "nlp", "transformer"],
    "Software": ["app", "application", "software", "github copilot", "code", "developer", "devop", "programming", "user experience"],
    "Internet": ["social medium", "internet", "cybersecurity", "web3", "website"],
    "Data": ["data", "data analytic", "data science"],
    "Blockchain": ["cryptocurrency", "blockchain", "nft", "defi", "decentralization"],
    "Hardware": ["robot", "3d", "3d modeling", "laser"],
    "Gaming": ["game", "multiplayer", "gameplay", "game design", "fifa"],
    "Virtual Reality": ["virtual reality", "metaverse", "hologram"]
}

# Generate random numbers for each item and calculate sum for each category
for category, items in tech_categories.items():
    category_sum = 0
    for item in items:
        random_value = random.randint(1, 30)
        expanded_dict[f"{item}"] = random_value
        category_sum += random_value
    expanded_dict[f"{category}_sum"] = category_sum

expanded_dict





import json
with open(r"example_aaa.jsonl", 'a') as f:
    json_str = json.dumps(expanded_dict)
    f.write(json_str + '\n')