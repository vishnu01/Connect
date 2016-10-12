import socket
import os
def myplayer(text):
    import pyaudio
    import wave
    chunk = 1024
    f = wave.open(text)
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
    data = f.readframes(chunk)
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return
myip=socket.gethostbyname(socket.gethostname())
if myip is "127.0.0.1":
    print("You are not connected to the internet!")
    myplayer("noint.wav")
else:
    print("You are connected to the internet!")
    myplayer("int.wav")
