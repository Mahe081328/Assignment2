import requests
import json

url = "http://api.open-notify.org/iss-now.json"

status = requests.get(url)

if status.status_code == 200:
    data = status.json()
    # data = json.loads(a)
    iss_position = data["iss_position"]
else:
    print(f"Failed to Fetch Data: Error{status.status_code}")

print("Latitude: ", iss_position["latitude"])
print("Longitude: ", iss_position["longitude"])
print("Time_Stamp: ", data["timestamp"])
