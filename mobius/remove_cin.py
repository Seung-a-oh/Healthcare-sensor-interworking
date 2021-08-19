import requests

url = "http://203.253.128.177:7579/Mobius/healthcare-interworking/ppg/latest"

payload = ""
headers = {
  'Accept': 'application/xml',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'admin:admin'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
