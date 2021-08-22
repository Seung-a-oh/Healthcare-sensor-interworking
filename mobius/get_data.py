import requests
from datetime import datetime
import time
import json

fcsv = open("./from_mobius.csv", "w")

json_response = ""

def get(value):
  global json_response

  url = "http://203.253.128.177:7579/Mobius/healthcare-interworking/ppg/" + value + "/la"

  payload={}
  headers = {
    'Accept': 'application/json',
    'X-M2M-RI': '12345',
    'X-M2M-Origin': 'SOrigin'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  json_response = json.loads(response.text)
  print(response.text)

slicing = ""
def making(value):
  global slicing
  fcsv.write('time,'+value+'\n')
  slicing = json_response['m2m:cin']['con'].split(',')
  # start = slicing[0][7:17]
  # stop = slicing[1][7:17]
  start = 203322.777
  stop = 203323.998
  range = float(stop) - float(start)
  step = round(range / (len(slicing)-2),3)
  print(step)

  for i in slicing[2:]:
    fcsv.write(str(start) + ',' + i + '\n')
    start = start + step
  fcsv.close()

get('beat')
making('beat')

# json_response["con"]