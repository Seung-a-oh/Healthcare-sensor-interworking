import time
import sys
import spidev
import Jetson.GPIO as gpio
import busio
import board
import digitalio

#spi = busio.SPI(clock=board.D11, MOSI=board.D10, MISO=board.D9)
#cs = digitalio.DigitalInOut(board.D8)

CLK=board.D11
MISO=board.D9
MOSI=board.D10
CS=board.D8

def setupSpiPins(clkPin,misoPin,mosiPin, csPin):
    pass

#spi = spidev.SpiDev()
#spi.open(0,0)

def buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08

    # Return python list of 3 bytes
    #   Build a python list using [1, 2, 3]
    #   First byte is the start bit
    #   Second byte contains single ended along with channel #
    #   3rd byte is 0
    return [1,(8+channel) << 4, 0]
    
def processAdcValue(result):
    '''Take in result as array of three bytes. 
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
    pass
        
#def readAdc(channel):
def readAdc(channel, clkPin, misoPin, mosiPin, csPin):
    if ((channel > 7) or (channel < 0)):
        return -1
    read_command = 0x18
    read_command |= channel
    sendBits(read_command, 5, clkPin, mosiPin)
    adcValue = recvBits(12,clkPin,misoPin)
    return adcValue
#    r = spi.xfer2(buildReadCommand(channel))
 #   return processAdcValue(r)

def sendBits(data, numBits, clkPin, mosiPin):
    ''' Sends 1 Byte or less of data'''
    
    data <<= (8 - numBits)
    
    for bit in range(numBits):
        pass
        # Set RPi's output pin high or low depending on highest bit of data field
        
        # Advance data to the next bit
        
        # Pulse the clock pin HIGH then immediately low


def recvBits(numBits, clkPin, misoPin):
    '''Receives arbitrary number of bits'''
    retVal = 0
    
    # For each bit to receive
        # Pulse clock pin high then immediately low
        
        # Read 1 data bit in and include in retVal
        
        # Advance input to next bit
    
    # Divide by two to drop the NULL bit
    return (retVal/2)
        
if __name__ == '__main__':
    try:
        while True:
            val = readAdc(0,CLK,MISO,MOSI,CS)
            print ("ADC Result: ", str(val))
            time.sleep(1)
    except KeyboardInterrupt:
        spi.close() 
        sys.exit(0)
