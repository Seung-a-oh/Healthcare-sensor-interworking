import requests
from datetime import datetime
import time
import json

#응답 전역변수
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

  fcsv = open("./from_mobius_"+value+".csv", "w")
  fcsv.write('time,'+value+'\n')
  
  #텍스트 -> csv
  slicing = json_response['m2m:cin']['con'].split(',')
  start = slicing[0][7:17]  #시간 추출
  stop = slicing[1][7:17]
  range = float(그만) - float(start)  #interval 구하기
  step = round(range / (len(slicing)-2),3) 

  for i in slicing[2:]:  #csv 파일 작성
    fcsv.write(str(start) + ',' + i + '\n')
    start = float(start) + step

  print(step)
  fcsv.close()

get('ppg')
making('ppg')

get('beat')
making('beat')
