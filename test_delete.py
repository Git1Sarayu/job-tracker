import urllib.request

req = urllib.request.Request(
    "http://127.0.0.1:5000/applications/2",
    method="DELETE"
)

with urllib.request.urlopen(req) as response:
    print(response.read().decode())