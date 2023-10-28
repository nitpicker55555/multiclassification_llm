import re

s = """
Here is the JSON-format response based on the provided news:
json
Copy code
{
    "Is_relevant": true,
    "Specific_information": "Waymo, a self-driving tech company, has reported 18 minor incidents involving its autonomous vehicles in the Phoenix area since 2019. These incidents occurred during tests and actual rides. Waymo aims to improve transparency by releasing safety data on their website and hopes it will contribute to industry-wide safety standards for self-driving cars. The data indicates that Waymo vehicles in Phoenix experienced minor incidents once every 339,000 miles and avoided 29 other incidents with the intervention of a safety driver, occurring once every 210,000 miles. Fortunately, none of these incidents, including those prevented, resulted in serious injuries. Waymo cars were rear-ended 11 times, but the data suggests that they were not rear-ended more frequently than human-driven vehicles in the area. Eight of the most significant incidents were attributed to human errors, while Waymo's technology successfully avoided incidents involving striking fixed objects or departing from the roadway, which are common incidents with human drivers that can lead to fatalities."
}
The news is relevant to driverless car incidents, and the specific information about the incidents has been extracted as detailed as possible in the JSON response.
"""
matches = re.findall(r'\{(.*?)\}', s, re.DOTALL)


print(matches[0])