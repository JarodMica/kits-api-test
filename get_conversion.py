import requests
import os

job_id = 23353866
url_get_conversion = f"https://arpeggi.io/api/kits/v1/voice-conversions/{job_id}"
api_token = 'add your API'
headers = {
    'Authorization' : f'Bearer {api_token}'
}

response = requests.get(url=url_get_conversion, headers=headers)

# Get conversion
if response.status_code == 200:
    job_data = response.json()
    print(job_data)
else:
    print(response.status_code)
    
output_file_url = job_data['outputFileUrl']
if output_file_url:
    response = requests.get(output_file_url)
    if response.status_code == 200:
        filename = "converted_file.wav"
        save_path = os.path.join(os.getcwd(), filename)
        
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File saved as {save_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
else:
    print("No outputFileUrl found in the API response.")