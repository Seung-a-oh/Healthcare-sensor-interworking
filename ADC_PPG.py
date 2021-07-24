import mcp3008_sa as ms
import time

PPG = 0
BEAT = 1

mcp_ppg = ms.set_mcp(PPG)
mcp_beat = ms.set_mcp(BEAT)

while True:
    ppg = ms.readAnalog(mcp_ppg,PPG)
    beat = ms.readAnalog(mcp_beat,BEAT)

    print("PPG:", ppg)
    print("BEAT:", beat)
    
    time.sleep(1)
