import requests

url = "http://203.253.128.177:7579/Mobius"

#생성하고 싶은 ae 이름
ae_name = "h_test2"

payload = "{\n  \"m2m:ae\" : {\n    \"rn\": \"" + ae_name + "\",\n      \"api\": \"0.2.481.2.0001.001.000111\",\n      \"lbl\": [\"key1\", \"key2\"],\n      \"rr\": true,\n      \"poa\": [\"http://203.254.173.104:9727\"]\n    }\n}"

headers = {
  'Accept': 'application/json',
  'X-M2M-RI': '12345',
  'X-M2M-Origin': 'S',
  'Content-Type': 'application/vnd.onem2m-res+json;ty=2'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
