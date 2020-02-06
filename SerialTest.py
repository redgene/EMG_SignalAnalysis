
import serial

import pandas as pd
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras import models    

from keras.layers import Activation, Dense, Dropout
from sklearn.preprocessing import LabelBinarizer
import sklearn.datasets as skds
from pathlib import Path


ser = 0

# Function for Initializing the Serial Port
def init_serial():
    # COMNUM = 1        # COM Port Number | Windows
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600

    # ser.port = COMNUM - 1   #COM Port Name Start from 0
    ser.port = '/dev/cu.SOC' # COM Port | Unix
    ser.timeout = 10
    ser.open()          	  # Opens SerialPort

    if ser.isOpen():
        print("Open: " + ser.portstr)
    else:
    	print("Not successful")

# Call the Serial Initilization Function
init_serial()
# temp = raw_input("Type what you want to send, hit enter:\r\n")
# ser.write("temp")         #Writes to the SerialPort

model = models.load_model('/Users/utkarshtripathi/Documents/PlatformIO/Projects/Models/third.h5')

while 1:
    dataBytes = ser.readline()               	  # Read from Serial Port
    print('Data incoming Port: ' + dataBytes)     # Print What is Read from Port
