###
from scipy.io import wavfile

x = wavfile.read('PK.wav')
print(x)
print(x[:,0])
