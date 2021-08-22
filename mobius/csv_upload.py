import mcp3008_sa as ms
import time
import threading
import pandas as pd
import schedule
import change_filename as fn
from datetime import datetime
import requests
import pandas as pd
import numpy as np

#csv 파일 이름 저장 PPG_월/일_번호
filename = time.strftime('%m%d')+"_"+str(fn.a)
fcsv = open("../csv/PPG_"+filename+".csv", "w")
fpy = open("./change_filename.py", "w")

b = fn.a + 1
fpy.write("a = " + str(b))

PPG = 4
BEAT = 5
NUM = 100

count = 0

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

fcsv.write('time,ppg,beat'+'\n')

def ReadValue():
   global count

   ppg_val = ms.readAnalog(mcp_ppg, PPG)
   beat_val = ms.readAnalog(mcp_beat, BEAT)
   
   if beat_val > 3:
      beat_val = 3.3
   else:
      beat_val = 0

   time = datetime.now().strftime('%y%m%d_%H%M%S.%f')[:-3]

   fcsv.write(str(time) + ',' + str(ppg_val) + ',' + str(beat_val)+'\n')   
   count += 1

   # threading
   timer = threading.Timer(0.05, ReadValue)
   timer.start()

   if count == NUM:
      timer.cancel()

      fcsv.close()
      fpy.close()

      post('ppg')
      post('beat')
      # post('ecg', 'ecg')

def post(value):
   df = pd.read_csv("../csv/PPG_"+filename+".csv", encoding="UTF-8")
   
   t = df.loc[:NUM, 'time']
   va = t[0] + "," + t[NUM-1]

   v = df.loc[:NUM, value]
   for i in range(NUM):
      va = va + "," + str(v[i])

   url = "http://203.253.128.177:7579/Mobius/healthcare-interworking/ppg/" + value

   cin_contents = va

   payload = "{\n    \"m2m:cin\": {\n        \"con\": \"" + str(cin_contents) + "\"\n    }\n}"
   headers = {
   'Accept': 'application/json',
   'X-M2M-RI': '12345',
   'X-M2M-Origin': '{{aei}}',
   'Content-Type': 'application/vnd.onem2m-res+json; ty=4'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)

ReadValue()