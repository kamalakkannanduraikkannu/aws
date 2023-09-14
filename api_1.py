import os
import requests
def get(String):
    return String+"10"
response = requests.get("https://www.python.org")
f=open("response.html","+a")
f.write(str(response.content))
f.close()
print(response.__str__)





