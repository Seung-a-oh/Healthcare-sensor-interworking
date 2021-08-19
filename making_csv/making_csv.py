import mcp3008_sa as ms
import time
import threading
import pandas as pd
import schedule
import change_filename as fn
from datetime import datetime

#csv 파일 이름 저장 PPG_월/일_번호
filename = time.strftime('%m%d')+"_"+str(fn.a)
fcsv = open("../csv/PPG_"+filename+".csv", "w")
fpy = open("./change_filename.py", "w")

b = fn.a + 1
fpy.write("a = " + str(b))

PPG = 4
BEAT = 5

count = 0

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

fcsv.write('time,ppg,beat'+'\n')

def ReadValue():
	global count

	ppg = ms.readAnalog(mcp_ppg, PPG)
	beat = ms.readAnalog(mcp_beat, BEAT)
	
	if beat > 3:
		beat = 3.3
	else:
		beat = 0

	# t = time.strftime('%y%m%d_%H%M%S.', time.localtime(time.time()))
	# m = str(round(datetime.datetime.now().microsecond,2)).zfill(2)
	# # ti = str(t)[:-1]
	# ti = t + format(m,'.2s')

	date = datetime.now().strftime('%y%m%d')
	time = datetime.now().strftime('%H:%M:%S.%f')[:-3]

	fcsv.write(str(date) + ',' + str(time) + ',' + str(ppg) + ',' + str(beat)+'\n')	
	count += 1

	# threading
	timer = threading.Timer(0.06, ReadValue)
	timer.start()

	if count == 200:
		timer.cancel()
		fcsv.close()
		fpy.close()

ReadValue()
