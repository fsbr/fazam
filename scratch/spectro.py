# making the spectrogram

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

fs = 10e3
N = 1e5

amp = 2*np.sqrt(2)
noise_power = 0.01 *fs/2
time = np.arange(N)/ float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp*np.sin(2*np.pi*3e3*time + mod)
noise = np.random.normal(scale=np.sqrt(noise_power),size=time.shape)
noise *= np.exp(-time/5)
x = carrier + noise

f, t, Sxx = signal.spectrogram(x,fs)
plt.pcolormesh(Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

print(Sxx.shape)
