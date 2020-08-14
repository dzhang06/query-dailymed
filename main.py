import requests
import json
import xml.etree.ElementTree as ET

BASE_URL = 'https://dailymed.nlm.nih.gov/dailymed/services/v2/'
URL_BY_NDC = BASE_URL + 'spls.json?ndc='
example_ndc = '25010-210-27'


spl_search = requests.get(URL_BY_NDC + example_ndc)

root = spl_search.json()
data = root['data']
meta = root['metadata']
set_ids = []
for item in data:
    set_ids.append(item['setid'])


print(set_ids)
# pdf_url = 'https://dailymed.nlm.nih.gov/dailymed/downloadpdffile.cfm?setId='
# spl_by_ndc = requests.get(pdf_url + set_ids[0])
spl_by_ndc = requests.get(BASE_URL + 'spls/' + set_ids[0] + '.xml')
# print(spl_by_ndc.text)
root = ET.fromstring(spl_by_ndc.text)
print(root.tag)
print(root.attrib)

# for set_id in set_ids:
#     spl_by_ndc = requests.get(BASE_URL + 'spls/' + set_id + '.xml')
#     print(spl_by_ndc.text)

