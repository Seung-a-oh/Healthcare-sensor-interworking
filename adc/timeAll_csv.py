import mcp3008_sa as ms
import time
import schedule

f = open("time_ppg1.csv", "w")

PPG = 0
BEAT = 1

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

f.write('time,ppg,beat\n')

for i in range(200):
	ppg = ms.readAnalog(mcp_ppg, PPG)
	beat = ms.readAnalog(mcp_beat, BEAT)

	now = time.localtime()
	now_time = str(now.tm_year) + str(now.tm_mon) +str(now.tm_mday) + str(now.tm_hour) + str(now.tm_min) + str(now.tm_sec)
	#t = time.strftime('%H:%M:%S')
	
	f.write(now_time + ',' + str(ppg) + ',' + str(beat) + '\n')
	print(ppg, beat)
	time.sleep(0.05)
	
f.close()
