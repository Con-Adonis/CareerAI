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

def infoEntry(userInfo):
    with open('user_info.json', 'w') as f:
        json.dump(userInfo, f)
    
    print("successfully wrote user info")