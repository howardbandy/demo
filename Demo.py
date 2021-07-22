#  Python demo
import sys
import requests

print(sys.version)
print(sys.executable)
print("hello world")
r = requests.get("https://coreyms.com")
print(r.status_code)
