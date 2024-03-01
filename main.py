import requests
import json

url = "https://arpeggi.io/api/kits/v1/voice-models"

api_token = '_xmObO6A.eTVAdadv7pLY1pPyH0_MgxMU'

headers = {
    'Authorization' : f'Bearer {api_token}'
}

params = {
    'order': 'asc',
    'page': 1,
    'perPage': 10,
    'myModels' : "true"
}

response = requests.get(url=url, headers=headers, params=params)

if response.status_code == 200:
    # print(json.dumps(response.json(), indent=4))
    voice_name = [{voice["title"] : voice["id"]}  for voice in response.json()["data"]]
    # print(voice_name)
else:
    print("Something happened and there was an issue")
    
for item in voice_name:
    try:
        print(f'ID: {item["Me"]}')
        voice_id = item["Me"]
    except:
        pass
    # print(item)
    
url_conversion = "https://arpeggi.io/api/kits/v1/voice-conversions"

data = {
    'voiceModelId' : voice_id,
    'conversionStrength' : 0.5,
    'modelVolumeMix' : 0.5,
    'pitchShift' : 0
}

file = {
    'soundFile' : ("delilah.wav", open("delilah.wav", "rb"))
}

response = requests.post(url=url_conversion, headers=headers, params=data, files=file)

# Do conversion
if response.status_code == 200:
    conversion_data = response.json()
    job_id = conversion_data["id"]
    print(f"Job ID: {job_id}")
else:
    print(response.status_code)
    

