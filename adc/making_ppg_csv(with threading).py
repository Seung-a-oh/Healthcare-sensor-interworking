import mcp3008_sa as ms
import time
import threading

f = open("threading_ppg.csv", "w")

PPG = 0
BEAT = 1

count = 0

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

f.write('time,ppg,beat\n')

def ReadValue():
	global count

	ppg = ms.readAnalog(mcp_ppg, PPG)
	beat = ms.readAnalog(mcp_beat, BEAT)
	
	now = time.localtime()
	now_time = str(now.tm_year) + str(now.tm_mon) +str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec)
	
	f.write(now_time + ',' + str(ppg) + ',' + str(beat) + '\n')
	
	count += 1

	timer = threading.Timer(0.01, ReadValue)
	timer.start()
	
	if count == 1000:
		timer.cancel()
		f.close()
	
ReadValue()	
