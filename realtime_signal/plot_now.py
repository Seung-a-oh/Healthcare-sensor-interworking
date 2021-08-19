import mcp3008_sa as ms

import os
import matplotlib.pyplot as plt
from drawnow import *

loadavg = []

plt.ion()
cnt=0

PPG = 0
mcp_ppg = ms.set_mcp(PPG)

def plotLoadAvg():
    plt.title('PPG')
    plt.grid(True)
    plt.ylabel('ppg v')
    plt.plot(loadavg, label='ppg')
    #plt.legend(loc='upper right')

#pre-load dummy data
for i in range(0,50):
    loadavg.append(0)
    
for i in range(50):
    ppg = ms.readAnalog(mcp_ppg,PPG)
    loadavg.append(ppg)
    loadavg.pop(0)
    drawnow(plotLoadAvg)

plt.savefig("ppg_signal.png",dpi=350)
