import sys
import os
from time import sleep

workingDirectory = os.getcwd()
print ('Number of Arguments: ', len(sys.argv), ' arguments.')
print ('Argument List:' , str(sys.argv))

# Set initial values
HMI1 = False
HMI2 = False
HMI3 = False
HMI4 = False
HMI5 = False
HMI6 = False
HMI7 = False
HMI8 = False
HMI9 = False
HMI10 = False

def setHMIArgs(args):
    global HMI1, HMI2, HMI3, HMI4, HMI5, HMI6, HMI7, HMI8, HMI9, HMI10
    for arg in args:
        if arg == "HMI1":
            HMI1 = True
        elif arg == "HMI2":
            HMI2 = True
        elif arg == "HMI3":
            HMI3 = True
        elif arg == "HMI4":
            HMI4 = True
        elif arg == "HMI5":
            HMI5 = True
        elif arg == "HMI6":
            HMI6 = True
        elif arg == "HMI7":
            HMI7 = True
        elif arg == "HMI8":
            HMI8 = True
        elif arg == "HMI9":
            HMI9 = True
        elif arg == "HMI10":
            HMI10 = True
            
if len(sys.argv) > 1:
    setHMIArgs(sys.argv[0:])

while True:
    if HMI1: print('HMI Button 1')
    if HMI2: print('HMI Button 2')
    if HMI3: print('HMI Button 3')
    if HMI4: print('HMI Button 4')
    if HMI5: print('HMI Button 5')
    if HMI6: print('HMI Button 6')
    if HMI7: print('HMI Button 7')
    if HMI8: print('HMI Button 8')
    if HMI9: print('HMI Button 9')
    if HMI10: print('HMI Button 10')
    if HMI1: HMI1 = False
    if HMI2: HMI2 = False
    if HMI3: HMI3 = False
    if HMI4: HMI4 = False
    if HMI5: HMI5 = False
    if HMI6: HMI6 = False
    if HMI7: HMI7 = False
    if HMI8: HMI8 = False
    if HMI9: HMI9 = False
    if HMI10: HMI10 = False
    sleep(0.1)

