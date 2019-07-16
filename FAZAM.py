# okay lets shazam this shit.
import numpy as np
from scipy.io import wavfile
from scipy import signal,ndimage
import matplotlib.pyplot as plt

# rayvans has 2 channel audio
#fs,data = wavfile.read('RV.wav')
fs,data = wavfile.read('EWF.wav')
#generate the spectrogram channel wise
N = len(data)
time = np.arange(N)/float(fs)
#plt.plot(time,data)
#plt.show()

# lets get just the left ear
f,t,Sxx = signal.spectrogram(data[:,0],fs,nfft=1024,scaling='spectrum')
print(Sxx)
plt.pcolormesh(t,f,Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

# set the bounds to 4000 because that's whats in the paper
plt.ylim([0,4000])
plt.show()

# Sxx is already the dimension we want

print(f.ndim)
print(f.size)
print(f.shape)
print(Sxx.ndim)
print(Sxx.size)
print(Sxx.shape)


##### so this whole downstairs part we want to use peakfinding
# get average amplitude
print("Sxx,average",np.mean(Sxx))
print("Sxx, max", np.amax(Sxx))
print("Sxx, min", np.amin(Sxx))
print("length of Sxx",len(Sxx))
print("sxx is",Sxx)

sMax = np.amax(Sxx)
# set the value to zero dude just do an n^2 thing

# set threshold
# pathetically slow im sure this could be made faster but lets roll
row = Sxx.shape[0]
col = Sxx.shape[1]
Sxx1 = np.ones((row,col))
# i is a nparry 

# this not only didnt work, but it also sucked lol
#hackx = np.array([])
#hacky = np.array([])
#for i in range(0,row):
#    for j in range(0, col):
#        if Sxx[i,j] > 0.1*sMax:
#            # this operation wastes time imo
#            #Sxx1[i,j] = 1#Sxx[i,j]
#            hackx = np.append(hackx,i)
#            hacky = np.append(hacky,j)
#        else:
#            pass
#            #Sxx1[i,j] = 0

# so i think that we can roll with this and the understanding is that we're using
# delta index instead of delta t

print(Sxx1)
#plt.pcolormesh(t,f,Sxx1)
plt.scatter(hackx,hacky)
plt.ylim([0, 4000])
plt.title('hacked constellation')
plt.show()

# trying new max filter
#constellation = ndimage.maximum_filter(Sxx,size=10)           
#print(constellation)
#plt.pcolormesh(t,f,constellation)
#plt.ylim([0,4000])
#plt.show()
