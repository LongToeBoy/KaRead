#!/usr/bin/env python3

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import sys

p=pyaudio.PyAudio()

infile=sys.argv[1]
samples=np.load(infile)
stream=p.open(format=pyaudio.paFloat32, channels = 1, rate=44100,output=True)

plt.close('all')
plt.plot(samples)
plt.title("ეს სირობა გამოგივიდა")
plt.grid(True,which='both')
plt.axhline(y=0,color='k')
plt.show()
while True:
	stream.write(samples)

stream.stop_stream()
stream.close()
p.terminate()
