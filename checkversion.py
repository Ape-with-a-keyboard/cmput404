import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/Ape-with-a-keyboard/cmput404/master/checkversion.py")

print response.text
print response.status_code
