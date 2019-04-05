#!/usr/bin/env python3

import numpy as np
import csv
import sys

დისკ_სიხშირე=44100


with open(sys.argv[1], 'rt')as f:
	reader = csv.reader(f, delimiter='	', skipinitialspace=True)
	ინფო=list()
	cols=next(reader)
	
	for col in cols:
		ინფო.append(list())
	for line in reader:
		for i in range(0,len(ინფო)):
			ინფო[i].append(line[i])
	ხმ_ინფო=dict()
	
	for i in range(0,len(cols)):
		ხმ_ინფო[cols[i]]=ინფო[i]

#print(data)
სიხშირეები=ხმ_ინფო['Frequency (Hz)']
სიძლიერეები=ხმ_ინფო['Level (dB)']
ხმა=[]
print(type(ხმა)," ",type(სიხშირეები))
def აჯამე(სიხ,სიძ,დრო,დისკ):
	global ხმა
	ბიჯ=0
	if not isinstance(სიხ, int):
		for x in სიხ:
			ამპლიტუდა=10**(round(float(სიძ[ბიჯ]),1)/10)
			print(ამპლიტუდა)
			გრადუსი=2*np.pi*np.arange(დისკ*დრო)*round(float(x),1)/დისკ
			ხმა.append((np.sin(გრადუსი)*ამპლიტუდა).astype(np.float32))
			ბიჯ+=1
			print(round(ბიჯ/len(სიხ)*100,1),"%")
		ხმა=sum(ხმა)
		
	else:
		ხმა=(np.sin(2*np.pi*np.arange(სიხ*დრო)*სიხ/დისკ)).astype(np.float32)
		ხმა=np.asarray(ხმა)
	return ხმა

მოჯვი=აჯამე(სიხშირეები,სიძლიერეები,2,44100)
ტუალეტში='/home/clever/სამუშაო მაგიდა/ხმა'
np.save(ტუალეტში,მოჯვი)


