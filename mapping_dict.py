mapping_dict = {
  "privacy violation": "Privacy Violations",
  "discrimination": "Equal Rights Violations",
  "mental harm": "Psychological Harm",
  "whether mental harm is reversible": "Psychological Harm: Reversibility",
  "whether it affects self-identity and values": "Psychological Harm: Influential Attributes of Self-identity and Values",
  "severity of mental harm": "Psychological Harm: Severity",
  "whether the mental harm is persistent": "Psychological Harm: Persistence",
  "physical harm": "Physical Harm",
  "severity of physical harm": "Physical Harm: Severity",
  "whether the physical harm is persistent": "Physical Harm: Persistence",
  "is the physical harm reversible": "Physical Harm: Reversibility",
  "whether the physical harm is easily detectable": "Physical Harm: Detectability",
  "economic loss": "Economic Loss",
  "is the economic loss persistent": "Economic Loss: Persistence",
  "severity of economic loss": "Economic Loss: Severity",
  "local population": "Impact Scope: Local",
    "global implications":"Impact Scope: Global",
  "model data timeliness is not good": "Attributes Caused by Untimely Maintenance of Training Data",
  "system reproducibility is weak": "Attributes Caused by Opacity or Weak Reproducibility",
  "whether it is due to the limitations of traditional methods of supervision": "Attributes Caused by Limitations of Traditional Supervision Methods",
  "individual": "Impact Scope: Individual",
  "severity of discrimination": "Equal Rights Violations: Severity",
  "is vulnerable group": "Equal Rights Violations: Vulnerable Group Attributes",
  "sensitive privacy breach": "Privacy Violations: Sensitivity",
  "severity of privacy violation": "Privacy Violations: Severity",
  'geographic information data is inaccurate':'GIS Data Accuracy',
  'Outdated geographic information':'GIS Data Timeliness',
  'sensor information preprocessing error':'GIS Data Preprocessing',
  'sensor information acquisition error':'GIS Data Acquisition',
  'geographic information data source integration issues':'GIS Data Integration',
  'data storage management issues':'GIS Data Storage and Management',
  'information processing problems':'GIS Data Analysis and Processing',
  'geographical information application issues':'GIS Data Application and Dissemination'}

keys=[]
for name,key in mapping_dict.items():
  if key not in keys:
    keys.append(key)
  else:print(name,"..",key)
print(len(keys))