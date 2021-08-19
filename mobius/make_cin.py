import requests

url = "http://203.253.128.177:7579/Mobius/healthcare-interworking/emg"

cin_contents = ""

payload = "{\n    \"m2m:cin\": {\n        \"con\": \"" + cin_contents + "\"\n    }\n}"
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': '{{aei}}',
  'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
