import requests
import json
import pandas as pd
import time


url = "http://api.open-notify.org/iss-now.json"

status = requests.get(url)

if status.status_code == 200:
    data = status.json()
else:
    print(f'Failed To Fetch Data: Error {status.status_code}')

arr = []
iss_position = data["iss_position"]
latitude = iss_position["latitude"]
longitude = iss_position["longitude"]
timestamp = data["timestamp"]

while len(arr) < 100:
    arr.append({
        "Latitude":latitude,
        "Longitude":longitude,
        "Time_Stamp":timestamp
        })
    
time.sleep(1)

df = pd.DataFrame(arr)
df.to_csv('iss_location.csv', index = False)

print("Data Fetched and saved to 'iss_location.csv'.")
