import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def set_mcp(pin):
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    while not spi.try_lock():
           pass
    
    spi.configure(baudrate=115200)
    spi.unlock()

    cs = digitalio.DigitalInOut(board.CE0)

    mcp = MCP.MCP3008(spi, cs)

    chnnel = AnalogIn(mcp, pin)
    
    return channel

def readAnalog(mcp_,pin):
    digital = round(mcp_.value*5/1023, 4)
    
    return digital
