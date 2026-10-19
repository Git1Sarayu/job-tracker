import json
import urllib.request

job = {
    "company": "66degrees",
    "role": "IT Service Desk Intern",
    "date_applied": "2026-10-20",
    "status": "applied"
}

req = urllib.request.Request(
    "http://127.0.0.1:5000/applications",
    data=json.dumps(job).encode(),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req) as response:
    print(response.read().decode())