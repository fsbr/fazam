# okay lets shazam this shit.
import numpy as np
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

# rayvans has 2 channel audio
fs,data = wavfile.read('PK.wav')
#generate the spectrogram channel wise
N = len(data)
time = np.arange(N)/float(fs)
plt.plot(time,data)
plt.show()

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

row = Sxx.shape[0]
col = Sxx.shape[1]
Sxx1 = np.ones((row,col))
# i is a nparry 
for i in range(0,row):
    for j in range(0, col):
        if Sxx[i,j] > 0.1*sMax:
            Sxx1[i,j] = Sxx[i,j]
        else:
            Sxx1[i,j] = 0
print(Sxx1)
plt.pcolormesh(t,f,Sxx1)
plt.ylim([0, 4000])
plt.title('hacked constellation')
plt.show()
            
