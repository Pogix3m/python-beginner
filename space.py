# python3 -m venv venv              => to create venv(like node_modules folder) with venv folder name
# source venv/bin/activate          => activate
# pip3 install requests              => install package

import requests

response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())