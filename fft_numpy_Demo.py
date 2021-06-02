import matplotlib.pyplot as plt
import numpy as np

N = 16
n = np.arange(0, N)
f0 = 5.0

cosine_sig = np.cos(2.0*np.pi*f0/N*n)
X = np.fft.fft(cosine_sig)

fig = plt.figure(1)
plt.subplot(2,1,1)
plt.stem(n,cosine_sig)
plt.title('Input Signal')

plt.subplot(2,1,2)
plt.stem(n,np.abs(X))
plt.title('Spectrum')

plt.show()