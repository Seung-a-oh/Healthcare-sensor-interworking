import requests

url = "http://203.253.128.177:7579/Mobius/h_test"

payload = ""
headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'Superman'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
