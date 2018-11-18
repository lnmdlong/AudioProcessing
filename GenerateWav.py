#!usr/bin/env python
#code=utf-8

import wave
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import sys
 
sys.setrecursionlimit(1000000)

#define the params of wave
channels = 1
sampwidth = 2
framerate = 9600
file_name = 'sample.wav'
frequency_begin = 1
frequency_end = 100
#define the time of wave
time = 1
 
def Generate_Wav():
	#generate the time bar
	t = np.arange(0,time,1.0/framerate)
	#generate the chirp signal from 300 to 3300Hz
	wave_data = signal.chirp(t, frequency_begin, time, frequency_end, method = 'linear')*1000
	#cast to the type of short
	wave_data = wave_data.astype(np.short)
	#open a wav document
	f = wave.open(file_name,"wb")
	#set wav params
	f.setnchannels(channels)
	f.setsampwidth(sampwidth)
	f.setframerate(framerate)
	#turn the data to string
	f.writeframes(wave_data.tostring())
	f.close()
 
def read_wave_data(file_path):  
    #open a wave file, and return a Wave_read object  
    f = wave.open(file_path,"rb")  
    #read the wave's format infomation,and return a tuple  
    params = f.getparams()  
    #get the info  
    nchannels, sampwidth, framerate, nframes = params[:4]  
    #Reads and returns nframes of audio, as a string of bytes.   
    str_data = f.readframes(nframes)  
    #close the stream  
    f.close()  
    #turn the wave's data to array  
    wave_data = np.fromstring(str_data, dtype = np.short)   
    time = np.arange(0, nframes) * (1.0/framerate)  
    return wave_data, time
 
def Plot_Wav():
	wave_data, time = read_wave_data(file_name)
	plt.plot(time, wave_data)
	plt.grid(True)
	plt.show()
 
def main():
	Generate_Wav()
 
if __name__ == "__main__":
	main()

