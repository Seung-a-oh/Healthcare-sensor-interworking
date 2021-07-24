import mcp3008_sa as ms
import time

f = open("10sec.csv", "w")

PPG = 0
BEAT = 1

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

f.write('ppg,beat\n')

for i in range(200):
	ppg = ms.readAnalog(mcp_ppg, PPG)
	beat = ms.readAnalog(mcp_beat, BEAT)

	f.write(str(ppg) + ',' + str(beat) + '\n')
	time.sleep(0.05)

f.close()

