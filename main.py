import requests
import json

def getData(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout = 20)
    return response.json()
    if response.status_code == 200:
        data = response.json()
        return data
if __name__ == "__main__":
    name = "Justedizi"
    print(getData(name))

