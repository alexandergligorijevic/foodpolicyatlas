import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

XML_URL = "https://atlas.foodbanking.org/wp-content/uploads/country-data.xml"

headers = {

    "User-Agent": "Mozilla/5.0",

    "Referer": "https://atlas.foodbanking.org/"

}

response = requests.get(XML_URL, headers=headers, timeout=30)
response.raise_for_status()

xml_text = response.text

# Save raw XML too
with open("country-data.xml", "w", encoding="utf-8") as f:
    f.write(xml_text)

root = ET.fromstring(xml_text)

def element_to_dict(element):
    data = {}
    for child in element:
        if len(child):
            data[child.tag] = element_to_dict(child)
        else:
            data[child.tag] = child.text
    return data

countries = []

for child in root:
    item = element_to_dict(child)
    item["_xml_tag"] = child.tag
    countries.append(item)

output = {
    "source": XML_URL,
    "scraped_at": datetime.now(timezone.utc).isoformat(),
    "record_count": len(countries),
    "countries": countries
}

with open("country-data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Downloaded and converted {len(countries)} records")
