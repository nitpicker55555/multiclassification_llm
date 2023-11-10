import re

text = "{'label_list': ['GPS privacy breach', 'concerd'ns', 'senior' GPs', 'patients', 'personal data', 'NHS Digital', 'doctors' surgeries', 'Tower Hamlets', 'east London', 'patient data', 'collection', 'refusal', 'Health and Social Care Act 2012', 'privacy campaigners', 'plans', 'medical histories', 'database', 'private sector', 'researchers', 'NHS Digital', 'data', 'pseudonymization', 'critics', 'patients', 'medical records', 'breach', 'collection', 'sharing', 'personal medical data', 'patient awareness', 'consent']}"

# 正则表达式
pattern = r"('[^',]*')([^',]*')([^',]*')"
def convert_lists_to_sets(d):
    """
    Recursively convert all lists in a nested dictionary to sets.
    """
    for key, value in d.items():
        if isinstance(value, list):
            d[key] = set(value)
        elif isinstance(value, dict):
            convert_lists_to_sets(value)

# 替换函数
def replace(match):
    return match.group(1) + match.group(2).replace("'", "", 1) + match.group(3)

# 执行替换
result = re.sub(pattern, replace, text)

print(result)
aa={'Privacy': {'Data': {'data breach', 'data leak', 'data security', 'data protection', 'data exposure', 'data collection', 'data sharing'}, 'Personal Information': ['personal data', 'sensitive information', 'email addresses', 'phone numbers', 'home addresses', 'passport numbers', 'medical records', 'Social Security numbers'], 'Incidents': ['GPS privacy breach', 'privacy breach', 'privacy concerns', 'privacy issues', 'privacy breaches'], 'Laws & Regulations': ['General Data Protection Regulation', 'data protection laws', 'privacy policy', 'privacy rights']}, 'Security': {'Breaches': ['security breach', 'security lapse', 'security concerns', 'security flaw'], 'Cybersecurity': ['cyber-attack', 'hacker', 'attack', 'vulnerability', 'encryption', 'spyware'], 'Incidents': ['incident', 'unauthorized access', 'identity theft', 'fraud', 'theft']}, 'Technology': {'Navigation': ['GPS', 'Navigation system', 'navigation system errors', 'navigation systems', 'satellite navigation systems', 'satellite navigation system'], 'Devices': ['tracking devices', 'smartphones', 'Bluetooth technology'], 'Software & Apps': ['app', 'apps', 'software', 'dating app', 'fitness tracking app'], 'Systems': ['technology', 'system', 'database', 'server', 'backup systems', 'communication systems']}, 'Incidents & Issues': {'Failures': ['system failure', 'Navigation system failure', 'GPS malfunction', 'malfunction'], 'Errors': ['error', 'human error', 'navigation errors', 'inaccuracy'], 'Breaches': ['data breaches', 'privacy breaches', 'security breaches'], 'Exposures': ['Location data exposure', 'data exposure', 'exposure']}, 'Legal & Compliance': {'Actions': ['investigation', 'lawsuit', 'settlement', 'fine', 'penalty'], 'Regulations': ['law', 'regulation', 'General Data Protection Regulation', 'data protection laws']}, 'Organizations & Entities': {'Companies': ['Google', 'Facebook', 'Uber', 'Apple', 'Meta', 'TikTok'], 'Government': ['government', 'UK', 'Russia', 'China', 'India', 'US', 'European Union', 'Pentagon', 'U.S.', 'United States', 'European Commission'], 'Groups': ['NSO Group', 'Norwegian Consumer Council', 'military', 'law enforcement', 'healthcare system']}, 'People & Roles': {'Individuals': ['user', 'customer', 'patient', 'driver', 'employee', 'passenger', 'doctor', 'police officers', 'crew', 'CEO', 'citizen', 'member'], 'Personal Roles': ['victim', 'investigator', 'security researcher', 'expert', 'lawyer', 'client']}, 'Events & Consequences': {'Accidents': ['vehicle accidents', 'GPS malfunction accidents', 'accident', 'collision'], 'Disruptions': ['disruption', 'delay', 'issue', 'challenge', 'impact'], 'Responses': ['response', 'warning', 'warn', 'recall']}, 'Miscellaneous': {'Information': ['news', 'information', 'record', 'report', 'document', 'dataset', 'news article'], 'Concerns': ['concern', 'safety concerns', 'security concerns', 'privacy concerns'], 'Misc': ['risk', 'problem', 'mistake', 'violation', 'abuse', 'use', 'interest', 'effort', 'plan', 'method', 'topic', 'case', 'ability', 'service', 'adoption', 'dependence', 'market', 'target', 'worldwide', 'space']}}
convert_lists_to_sets(aa)
print(aa)