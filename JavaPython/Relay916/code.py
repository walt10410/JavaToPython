# ^^^^^  Relay Code for 9 - 16
import time
import usb_cdc
import digitalio
import board
from analogio import AnalogOut
from digitalio import DigitalInOut, Direction
import array
import neopixel
import microcontroller
print("Hello World!")
time.sleep(3)

#************CONSTENTS & INITIAL VALUES
microcontroller.enable_interrupts
DEBUG = True

serial = usb_cdc.data
serial.timeout : 0.5 #seconds
usb_cdc.console.timeout : 0.5 #seconds

in_data = bytearray()
out_data = b'waiting****'

USB_Index = -1 # DO NOT CHANGE
Inputs = [250,0,0,0,0,0,0,0,0,2]#leading 0 may not be needed. element 0=msTime for energized, and 9=multiplier for time
Ch_Select = array.array('I', [250,0,0,0,0,0,0,0,0,2]) # unsigned interger array each item is 2 bytes
bUSB_read= True
count = 0 # used to prevent lock up if not recognized by PI
Continue = False
#****************
#%%%%%%%%%%%%%%%DEFINE THE RELAYS USE
#Ch_Select Index	Use
#Ch[0]			Delay in ms to wait to deenergize the relay. Allows time to switch to move
#				Range is 100 to 999
#Ch[1]	Relay 1	Switch 1 MAIN LINE
#Ch[2]	Relay 2	Switch 1 BRANCH LINE
#Ch[3]	Relay 3	Switch 2 MAIN LINE
#Ch[4]	Relay 4	Switch 2 BRANCH LINE
#Ch[5]	Relay 5	Switch 3 MAIN LINE
#Ch[6]	Relay 6	Switch 3 BRANCH LINE
#Ch[7]	Relay 7	Switch 4 MAIN LINE
#Ch[8]	Relay 8	Switch 4 BRANCH LINE
# Relay Module 9 through 16
#Ch[1]	Relay 1	Switch 5 MAIN LINE
#Ch[2]	Relay 2	Switch 5 BRANCH LINE
#Ch[3]	Relay 3	Switch 6 MAIN LINE
#Ch[4]	Relay 4	Switch 6 BRANCH LINE
#Ch[5]	Relay 5	OPEN
#Ch[6]	Relay 6	OPEN
#Ch[7]	Relay 7	OPEN
#Ch[8]	Relay 8	OPEN

# Ch[9]	open	must be integet
#%%%%%%%%%%%%%%%

#************FUNCTIONS*********
def log(msg):
    if DEBUG: print(msg)
    
 #&&&&&&&&&&&&&LED&&&&&&&&&RGB&&&&&
#Contents and IO
#LED = digitalio.DigitalInOut(board.GP13)  # bit bang to chip controlling the leds
num_pixels = 1
ORDER = neopixel.GRB
LED = board.GP13
pixels = neopixel.NeoPixel(LED, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER)
# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1

# The number of NeoPixels

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)   
#***************************************
    
ch1 = digitalio.DigitalInOut(board.GP21)
ch2 = digitalio.DigitalInOut(board.GP20)
ch3 = digitalio.DigitalInOut(board.GP19)
ch4 = digitalio.DigitalInOut(board.GP18)
ch5 = digitalio.DigitalInOut(board.GP17)
ch6 = digitalio.DigitalInOut(board.GP16)
ch7 = digitalio.DigitalInOut(board.GP15)
ch8 = digitalio.DigitalInOut(board.GP14)

# Set Direction
ch1.direction = digitalio.Direction.OUTPUT
ch2.direction = digitalio.Direction.OUTPUT
ch3.direction = digitalio.Direction.OUTPUT
ch4.direction = digitalio.Direction.OUTPUT
ch5.direction = digitalio.Direction.OUTPUT
ch6.direction = digitalio.Direction.OUTPUT
ch7.direction = digitalio.Direction.OUTPUT
ch8.direction = digitalio.Direction.OUTPUT

# Set initial outputs to 0
ch1.value = False
ch2.value = False
ch3.value = False
ch4.value = False
ch5.value = False
ch6.value = False
ch7.value = False
ch8.value = False
        
#%%%%START LOOP%%%%
while not Continue:
    serial_line = serial.readline()
    print('serial line')
    print(serial_line)
    if serial_line == b'who are you\n':
        serial.write(b'Relay916' + b'\n')
    if serial_line == 'Great\n':
        serial.write('Relay916_continue' +'\n')
        Continue = True
        
while True:
    while serial.in_waiting > 0:
        USB_Index += 1      #starts at 0
        bUSB_read = True	# used to id change or new input for writing to relays
        serial_line = serial.readline()
        print('serial line')
        print(serial_line)
        if serial_line == b'who are you\n':
            serial.write(b'Relay916'+ '\n')
        serial_bit = serial.read(1) # read 1 character from buffer
        print(serial_bit)
        
        if USB_Index == 3:
            temp = in_data.decode()
            print(temp)
            Ch_Select[0] = int(temp)
        if USB_Index == 4:
            temp = serial_bit.decode()
            Ch_Select[1] = int(temp)
        if USB_Index == 6:
            temp = serial_bit.decode()
            Ch_Select[2] = int(temp)
        if USB_Index == 8:
            temp = serial_bit.decode()
            Ch_Select[3] = int(temp)
        if USB_Index == 10:
            temp = serial_bit.decode("utf-8")
            Ch_Select[4] = int(temp)
        if USB_Index == 12:
            temp = serial_bit.decode("utf-8")
            Ch_Select[5] = int(temp)
        if USB_Index == 14:
            temp = serial_bit.decode("utf-8")
            Ch_Select[6] = int(temp)
        if USB_Index == 16:
            temp = serial_bit.decode("utf-8")
            Ch_Select[7] = int(temp)
        if USB_Index == 18:
            temp = serial_bit.decode("utf-8")
            Ch_Select[8] = int(temp)
        if USB_Index == 20:
            temp = serial_bit.decode("utf-8")
            Ch_Select[9] = int(temp)
        #start of if
        if serial_bit == b'\n':		# Found end of line
            log(in_data.decode("utf-8"))
            out_data = in_data
            serial.write(out_data)
            time.sleep(0.5)
            in_data = bytearray()
            serial.reset_input_buffer()
            serial.reset_output_buffer()
            USB_Index = -1		#set counter for next set of data
        else:
            # add bytes read to the bytearray
            in_data += serial_bit
        # end of if

#^^ if read data then write outputs^^
    
    if bUSB_read:	# input and write output here
            if Ch_Select[1] == 1:
                ch1.value = True
            else:
                ch1.value = False
            if Ch_Select[2] == 1:
                ch2.value = True
            else:
                ch2.value = False
            if Ch_Select[3] == 1:
                ch3.value = True
            else:
                ch3.value = False
            if Ch_Select[4] == 1:
                ch4.value = True
            else:
                ch4.value = False
            if Ch_Select[5] == 1:
                ch5.value = True
            else:
                ch5.value = False
            if Ch_Select[6] == 1:
                ch6.value = True
            else:
                ch6.value = False
            if Ch_Select[7] == 1:
                ch7.value = True
            else:
                ch7.value = False
            if Ch_Select[8] == 1:
                ch8.value = True
            else:
                ch8.value = False
            if Ch_Select[9] < 1: Ch_Select[9] = 1 # this is multipklier, must be 1 or greater
            time.sleep(Ch_Select[0]*Ch_Select[9]/1000) # delay timer so switch will move and stabalize, then turn off all relays

            ch1.value = False
            ch2.value = False
            ch3.value = False
            ch4.value = False
            ch5.value = False	# on Relay 9 through 16 this is open
            ch6.value = False	# on Relay 9 through 16 this is open
            ch7.value = False	# on Relay 9 through 16 this is open
            ch8.value = False	# on Relay 9 through 16 this is open
            bUSB_read = False
    ################NEOPIXEL BELOW

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill([255, 0, 0])
    pixels.show()

    rainbow_cycle(0.0014)  # rainbow cycle with 1ms delay per step)

    # time delays
    time.sleep(0.010)   # allow pico to do other things
