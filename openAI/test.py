import requests
from secrets_1 import OpenAI_API_KEY
# Replace 'YOUR_OPENAI_API_KEY' with your actual API key

# Define the API endpoint URL
url = 'https://api.openai.com/v1/completions'

# Set the headers with the API key
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + OpenAI_API_KEY
}

# Create the request payload
payload = {
  "model": "text-davinci-003",
  "prompt": "1984 by george orwell",
  "max_tokens": 64,
  "temperature": 0.5
}

# Send the API request
response = requests.post(url, headers=headers, json=payload)

# Check the response status code
if response.status_code == 200:
    print('API key is valid. Request successful.')
else:
    print("Error Code: " + str(response.status_code) + "\n" + response.text )
