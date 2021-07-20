import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

SCK=board.D11
MOSI=board.D10
MISO=board.D9
# create the spi bus
spi = busio.SPI(SCK, MOSI, MISO)
#spi = busio.SPI(clock=board.D11, MISO=board.D9, MOSI=board.D10)
#spi = busio.SPI(0, SPI1_SCK=board.D18, SPI1_MOSI=board.D17, SPI1_MISO=board.D16)

#spi = busio.SPI(0, SPI1_SCK, SPI1_MOSI, SPI1_MISO)
#spi = board.SPI()
#cs=digitalio.DigitalInOut(board.CE0)
#spi = busio.SPI(0, clock=SPI1_SCK, MISO=SPI1_MISO, MOSI=SPI1_MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

#cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

while True:
	print('Raw ADC Value: ', chan.value)
	print('ADC Voltage: ' + str(chan.voltage) + 'V')
	time.sleep(0.5)
