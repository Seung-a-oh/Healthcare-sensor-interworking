import requests

url = "http://203.253.128.177:7579/Mobius/healthcare-interworking/emg"

#생성하고 싶은 cnt 이름
cnt_name = "envelope"

payload = "{\n  \"m2m:cnt\": {\n    \"rn\": \""+ cnt_name + "\",\n    \"lbl\": [\"ss\"],\n    \"mbs\": 16384\n  }\n}"

headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'SqN3adXOw968',
  'Content-Type': 'application/vnd.onem2m-res+json; ty=3'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
