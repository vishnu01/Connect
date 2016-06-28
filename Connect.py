import os
import webbrowser
import subprocess as s
ip=raw_input("Enter the IP/Domain name :")
if(s.call(["ping",ip])==0):
    print "valid internet" 
    webbrowser.open("C:\Users\Public\Music\Sample Music\sleep.mp3")
else :
    print "no internet"
    raw_input()
