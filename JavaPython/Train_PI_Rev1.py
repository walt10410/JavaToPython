import time
import serial
#import array
import gpiozero
import serial.tools.list_ports as list_ports
import os

# ************CONSTANTS***********
Ch_Select18 = [999,0,0,0,0,0,0,0,0,3]
Ch_Select916 = [200,0,0,0,0,0,0,0,0,2]
Continue = False

# Push Button inputs and logic
PButton1 = gpiozero.Button(4, pull_up=False, bounce_time=0.1, hold_time=1, hold_repeat = False)
PButton2 = gpiozero.Button(17, pull_up=False, bounce_time=0.1, hold_time=1, hold_repeat = False)
PButton3 = gpiozero.Button(27, pull_up=False, bounce_time=0.1, hold_time=1, hold_repeat = False)
PButton4 = gpiozero.Button(22, pull_up=False, bounce_time=0.1, hold_time=1, hold_repeat = False)
PButton5 = gpiozero.Button(9, pull_up=False, bounce_time=0.1, hold_time=1, hold_repeat = False)
#

TramStop1 = gpiozero.Button(5, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)
TramStop2 = gpiozero.Button(6, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)
TramStop3 = gpiozero.Button(13, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)
TramStop4 = gpiozero.Button(19, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)
# ^^End of line sensors -  LEFT then RIGHT
TramStop3 = gpiozero.Button(26, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)
TramStop4 = gpiozero.Button(23, pull_up=False, bounce_time=0.05, hold_time=0.5, hold_repeat = False)



# ***********************************
RelayNum18 = ''     # used to get the correct port (ttyACM?) 
RelayNum916 = ''    # used to get the correct port (ttyACM?)

#$$$$$$$$$$$$     TO DO LIST     SAMMY - PLEASE ADD TO WHEN READY
#             1 ) Determine which ttyACM is to which module
#                  a) pid=Relay18 other =Relay_18
#                  b) pid=Relay916 other =Relay_916
#             2 ) Relay board 18 returns b" " on write. Now it works correctly! same code a other
#             3 ) Control and interface to HMI
#             5 ) Outputs on PI
#                 a) button actions
#                 b) street lights
#             6 ) Playing sounds based on selection from HMI
#             7 ) Push Buttons
#                   a ) PB1 - Play a sound
#                   b ) PB2 - Flash a LED on the panel (RGBW)
#                   c ) PB3 - Flash a LED located on the train board
#                   d ) PB4 - 
#                   e ) PB5 - 
#                   f ) inputs for Tram locations (may need 2 for each middle station) 
#             8 ) done  
# #           9 )    ? more to add?
#
#*********************
# ^^^^^^^ FIND THE 2 DATA PORTS ^^^^^^^^

while True:
    all_ports = list_ports.comports()
    all_port_len = len(all_ports)
    for i in range (all_port_len):
        port = all_ports[i]
        if port.description == 'Relay_18 - CircuitPython CDC2 control':
            RelayNum18 = str(port.device)
        if port.description == 'Relay_916 - CircuitPython CDC2 control':
            RelayNum916 = str(port.device)
    if RelayNum18 == '' or RelayNum916 == '':
        time.sleep(2)
#************************
#        exit_flag = threading.Event()
#def thread_func(): 
#    while not exit_flag.wait(timeout=DELAY):
#       action()
#*******************************
    if RelayNum18 == '' or RelayNum916 =='':
        if RelayNum18 == '': print('FAILED TO MAKE CONNECTION TO 1 - 8')
        if RelayNum916 == '': print('FAILED TO MAKE CONNECTION TO 9 - 16')
        exit()      # STOP IF MISSING A RELAY CARD

# set the Relay Module to correctttyACM        
ser18 = serial.Serial(RelayNum18, baudrate=115200, bytesize=8, parity='N', rtscts=True, timeout=0.1, write_timeout=0.1, inter_byte_timeout=0, exclusive = None)
ser916 = serial.Serial(RelayNum916, baudrate=115200, bytesize=8, parity='N', rtscts=True, timeout=0.1, write_timeout=0.1, inter_byte_timeout=0, exclusive=None)
#
#@@@@@@@@@@@@@@  DEFINE FUNCTIONS AND OTHER  @@@@@@
#
def Play(sound): # may have to apt install mpg123, send sound from icons or buttons
    os.system("mpg123 " + sound)

 # ADD LOGIC HERE FOR RELAY CONTROL
#
#
#   if __________???_________ = 1 (tram stop) then leave Realy 916 Ch-Select[5] =1
#   if __________???_________ = 1 (lights) then leave Realy 916 Ch-Select[6] =1

def PushB1():
        # play a sound of something
        PB1 = False
def PushB2():
        # play a sound or flash light?
        PB2 = False
def PushB3():
        # play a sound or flash light?
        PB3 = False
def PushB4():
        # play a sound or flash light?
        PB4 = False
def PushB5():
        # play a sound or flash light?
        PB5 = False
#
# !!! TRAM POSITION Functions !!!   
def TramStop_1():
    Ch_Select916[5] = 1     #close relay to open power to track
    time.sleep(0.5)
    Play(sound)     # CALL FUNCTION - ADD WHAT SOUND HERE, STOP, DOOR DOPEN DOOR CLOSE, START
    Ch_Select916[5] = 1

def TramStop_2():
    #Ch_Select916[5] = 1     #CONTROLLER STOP TRAM AT ENDS
    time.sleep(0.5)
    Play(sound)     # CALL FUNCTION - ADD WHAT SOUND HERE, STOP, DOOR DOPEN DOOR CLOSE, START
    #Ch_Select916[5] = 1





#&&&&&&&&&& PREPARE FOR DATA FOR SENDING &&&

#*******************TEMP LOOP FPR TESTING, ADD & REMOVING 1 & 0s
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
icount = 1
while True:
    if icount > 8: icount = 1
    if Ch_Select18[8] == 0:
        Ch_Select18[icount] = 1
    else:
        Ch_Select18[icount] = 0

    if Ch_Select916[8] == 0:
        Ch_Select916[icount] = 1
    else:#
        Ch_Select916[icount] = 0

#^^^^^^^^^^ Prepare transmit words ^^^^^^^^^^^^
#^^^ Relay 1 - 8
    ch1 = str(Ch_Select18[1])       # Sw 1 Main
    ch2 = str(Ch_Select18[2])       # Sw 1 Branch
    ch3 = str(Ch_Select18[3])       # Sw 2 Main
    ch4 = str(Ch_Select18[4])       # Sw 2 Branch
    ch5 = str(Ch_Select18[5])       # Sw 3 Main
    ch6 = str(Ch_Select18[6])       # Sw 3 Branch
    ch7 = str(Ch_Select18[7])       # Sw 4 Main
    ch8 = str(Ch_Select18[8])       # Sw 4 Branch
#^^ Relay 9 - 16 ^^^
    ch9 = str(Ch_Select916[1])       # Sw 5 Main
    ch10 = str(Ch_Select916[2])       # Sw 5 Branch
    ch11 = str(Ch_Select916[3])       # Sw 6 Main
    ch12 = str(Ch_Select916[4])       # Sw 6 Branch
    ch13 = str(Ch_Select916[5])       # Tram Stop
    ch14 = str(Ch_Select916[6])       # Lights
    ch15 = str(Ch_Select916[7])     # OPEN
    ch16 = str(Ch_Select916[8])     # OPEN

# Verify/change setting delay time (ms) [index 0] and the multiplies [index 9]. delay time is to be 100 to 999 only
    if Ch_Select18[0] < 100: Ch_Select18[0] = 100       #Delay time in ms 
    if Ch_Select18[0] > 999: Ch_Select18[0] = 999
    if Ch_Select18[9] < 1: Ch_Select18[9] = 1           # time delay multiplier
    if Ch_Select18[9] > 9: Ch_Select18[9] = 9

    if Ch_Select916[0] < 100: Ch_Select916[0] = 100     #Delay time in ms 
    if Ch_Select916[0] > 999: Ch_Select916[0] = 999
    if Ch_Select916[9] < 1: Ch_Select916[9] = 1         # time delay multiplier
    if Ch_Select916[9] > 9: Ch_Select916[9] = 9

    ch20 = str(Ch_Select18[0])   # delay time RELAY 1-8
    ch29 = str(Ch_Select18[9])   # delay multiplier RELAY 1-8
    ch30 = str(Ch_Select916[0])  # delay time RELAY 9-16
    ch39 = str(Ch_Select916[9])  #delay multiplier RELAY 9-16

#&&&&&&&&&& BUILD THE STRING WORDS AND CONVERT TO BYTES FOR SENDING &&&&&&&&
    send18 = ch20+','+ch1+','+ch2+','+ch3+','+ch4+','+ch5+','+ch6+','+ch7+','+ch8+','+ch29+', \n'
    send916 = ch30+','+ch9+','+ch10+','+ch11+','+ch12+','+ch13+','+ch14+','+ch15+','+ch16+','+ch39+', \n'

    send18_bytes = bytes(send18, 'utf-8')
    send916_bytes = bytes(send916, 'utf-8')

#     OPEN PORTS AND CHECK
    if not ser18.is_open: ser18.open    # VERIFY PORT IS OPEN
    if not ser916.is_open: ser916.open  # VERIFY PORT IS OPEN
    if not (ser18.open or ser916.open):
        if not ser18.open: print('Relay 1 - 8 not OPEN, STOP')
        if not ser916.open: print('Relay 9 - 16 not OPEN, STOP')
        exit()

    ser18.write(send18_bytes)       # send bytes
    ser916.write(send916_bytes)     # send bytes
    time.sleep(0.500)     # wait for data to be written NEEDED???

    test18=ser18.readline()
    test916=ser916.readline()
    time.sleep(0.250)    # NEEDED???
    if send18_bytes != test18: print('SEND FAIL TO 1 - 8')
    if send916_bytes != test916: print('SEND FAIL TO 9 - 16')

    icount += 1     # temp for loading 1 & 0s REMOVE WHEN DONE WITH TEST AT TOP
    # ***********PUSH BUTTONS AND TRAM INPUTS, ANYOTHER INPUTS
    
    PButton1.when_pressed = PushB1  # call function if pressed, once
    PButton2.when_pressed = PushB1
    PButton3.when_pressed = PushB3
    PButton4.when_pressed = PushB4
    PButton5.when_pressed = PushB5
    
    TramStop1.when_pressed = TramStop_1  # Stop Tram at location, NB first then SB
    TramStop2.when_pressed = TramStop_1
    TramStop3.when_pressed = TramStop_1
    TramStop4.when_pressed = TramStop_1
    TramStop5.when_pressed = TramStop_2
    TramStop6.when_pressed = TramStop_2

    if x: Ch_Select916[6] = 1       # turn on lights, UPDATE WITH SCREEN DATA
    if not x: Ch_Select916[6] = 0   # turn off lights, UPDATE WITH SCREEN DATA
         

    time.sleep(10)  # SECONDS temp to slow down count REMOVE WHEN DONE WITH TEST AT TOP