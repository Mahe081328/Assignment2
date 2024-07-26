import requests
import json

url = "http://api.open-notify.org/iss-now.json"

status = requests.get(url)

if status.status_code == 200:
    data = status.json()
    data1 = json.dumps(data)
    print(data1)
else:
    print(f"Failed to Fetch Data: Error{status.status_code}")
