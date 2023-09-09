#%%%%%  THIS IS RELAY 9 - 16 %%%%%%
import time
import usb_cdc
import microcontroller
import supervisor

supervisor.set_usb_identification("Relay916", "Relay_916", 00916, 01916)
microcontroller.enable_interrupts

try_count = 0

time.sleep(20) # wait for pi to load
usb_cdc.enable(console=True, data=True)
time.sleep(1)

if supervisor.runtime.serial_connected: print("connected")

while not (supervisor.usb_connected): 
    time.sleep(1) # WAIT AND CHECK AGAIN
    try_count +=1
    if try_count > 20: BOOTLOADER # microcontroller.reset() # reset and try again