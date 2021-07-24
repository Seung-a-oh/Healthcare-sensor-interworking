import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

while not spi.try_lock():
    pass
spi.configure(baudrate=115200)
spi.unlock()

cs = digitalio.DigitalInOut(board.CE0)

mcp = MCP.MCP3008(spi, cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)

while True:
    print("PPG:", round(chan0.value*5/1023, 4))
    print("BEAT", round(chan1.value*5/1023, 4))
    time.sleep(0.5)
    
