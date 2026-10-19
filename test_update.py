import json
import urllib.request

change = {"status": "interview"}

req = urllib.request.Request(
    "http://127.0.0.1:5000/applications/1",
    data=json.dumps(change).encode(),
    headers={"Content-Type": "application/json"},
    method="PUT"
)

with urllib.request.urlopen(req) as response:
    print(response.read().decode())