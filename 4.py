import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#a)
Size = 12;
T = np.arange(0, 1, 1/Size);
X = signal.sawtooth(2*np.pi*T);

Fig = plt.figure();
plt.stem(T, X);
plt.xlabel("N");
plt.ylabel("X[N]");
plt.title("a) 1 Hz Sawtooth");
plt.grid(True);
plt.show();

#b)
H = [0]*Size;
H[int(0.25*Size)] = 1;
Fig = plt.figure();
plt.stem(T, H);
plt.xlabel("N");
plt.ylabel("δ(T − 0.25)");
plt.title("b) Kronecker Delta");
plt.grid(True);
plt.show();

#c)
Y = np.convolve(X, H, "full");
Fig = plt.figure();
plt.stem(np.arange(0, 2-1/(Size-1), 1/Size), Y);
plt.xlabel("N");
plt.ylabel("X * H");
plt.title("c) Convolution");
plt.grid(True);
plt.show();

#d)
FFTH = abs(np.fft.fft(H));
FFTX = abs(np.fft.fft(X));
K = Size*T/2-Size/4;
Fig, F = plt.subplots(2, sharex=True, sharey=True);
F[0].stem(K, np.concatenate((FFTX[int(Size/2):Size], FFTX[0:int(Size/2)])));
F[0].set_title("X Spectrum");
F[0].grid(True);
F[1].stem(K, np.concatenate((FFTH[int(Size/2):Size], FFTH[0:int(Size/2)])));
F[1].set_title("Y Spectrum");
F[1].grid(True);
plt.xlabel("K[Hz]");
plt.ylabel("|FFTH|");

#e)

plt.show();
