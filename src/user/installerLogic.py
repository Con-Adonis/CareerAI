import os
import json

def apiEntry(apiKey):
    with open('.env', 'w') as f:
        json.dump({'apiKey': apiKey}, f)
    
    print("successfully wrote API key")
    apiConfirm()

def apiConfirm():
    with open('.env', 'r') as f:
        data = json.load(f)
        key = data.get('apiKey', None)
    print("successfully read API key:", key)

def infoEntry(newData):
    pathname = "data/userInfo.json"

    if os.path.exists(pathname):
        with open(pathname, 'r') as f:
            userData = json.load(f)
    else:
        userData = {}
    
    userData.update(newData)

    with open(pathname, 'w') as f:
        json.dump(userData, f, indent=4)