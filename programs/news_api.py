# import pprint
import requests
import win32com.client
    

speaker = win32com.client.Dispatch("SAPI.spvoice")
secret = '5f4abda030e34ed49c7059a192fd582f'

url = 'https://newsapi.org/v2/everything?'

parameters = {
    'q': 'apple', # query phrase
    "sortBy": "top",
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}

response = requests.get(url, params=parameters)

# Convert the response to JSON format and pretty print it
response_json = response.json()
# pprint.pprint(response_json)

for i in response_json['articles']:
    # print(i)
    print(i['title'], ":" )
    speaker.Speak(i['title'])
    speaker.Speak("well")
    print("\n         ", i['description'])
    speaker.Speak(i['description'])
    print("---------------------------------------------------------------------------------------------")              

