import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
print(json.dumps(response.json(), indent= 2))

v = response.json()
for c in v["results"]:
    print(c["tracidName"])
    
print(response)