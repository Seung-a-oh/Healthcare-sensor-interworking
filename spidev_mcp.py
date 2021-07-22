import time
import spidev


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 115200

def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
 
ch0 = 0
ch1 = 1

while True:
    ppg = ReadChannel(ch0)
    beat = ReadChannel(ch1)
    print("%.4f"%(ppg/1023*5))
    print("%.4f"%(round(beat/1023*5)))
    time.sleep(0.1)
