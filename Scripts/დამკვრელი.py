#!/usr/bin/env python3

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import sys

ენა=pyaudio.PyAudio()

ფაილი=sys.argv[1]	#მიიღოს შემდეგი არგუმენტი როგორც ცვლადი
ხმა=np.load(ფაილი)	#ეს გენერირებული ფაილია
პირი=ენა.open(format=pyaudio.paFloat32, channels = 1, rate=44100,output=True)	#ეს ილაპარაკებს ენის დახმარებით

plt.close('all')	#მაინც, ყოველი შემთხვევისთვის
plt.plot(ხმა)
plt.title("არ დაიჯერო რომ ასე გამოიყურება ხმა")
plt.grid(True,which='both')
plt.axhline(y=0,color='k')
plt.show()
#ეს ზედები ყველა დახატვისთვისაა, არაფერი საჭირო და მნიშვნელოვანი

while True:
	პირი.write(ხმა)	#გამოსცეს ხმა

პირი.stop_stream()	#გაჩუმდეს
პირი.close()	#დაკეტოს პირი
ენა.terminate()	#დაივიწყოს რა არის ენა
