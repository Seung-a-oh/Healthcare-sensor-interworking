import mcp3008_sa as ms
import time

SOUND = 0

mcp_sound = ms.set_mcp(SOUND)

while True:
    ppg = ms.readAnalog(mcp_sound, SOUND)

    print("sound:", ppg)
 
    time.sleep(0.2)

