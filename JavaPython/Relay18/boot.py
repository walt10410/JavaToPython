#%%%%%  THIS IS RELAY 1 - 8 %%%%%%
import time
import usb_cdc
import microcontroller
import supervisor

supervisor.set_usb_identification("Relay18", "Relay_18", 0018, 0118)
# microcontroller.enable_interrupts

time.sleep(20) # wait for pi to load
usb_cdc.enable(console=True, data=True)
time.sleep(1)

if supervisor.runtime.serial_connected:
    print("connected")
else:
    print('waiting')
    time.sleep(20) # WAIT AND CHECK AGAIN
if not(supervisor.runtime.serial_connected):
    microcontroller.reset # microcontroller.reset() # reset and try again