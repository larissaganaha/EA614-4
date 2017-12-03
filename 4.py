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
H = [0]*8;
H[int(0.25*Size)] = 1;
Fig = plt.figure();
plt.stem(T[0:8], H);
plt.xlabel("N");
plt.ylabel("δ(T − 0.25)");
plt.title("b) Kronecker Delta");
plt.grid(True);
plt.show();

#c)
Y = np.convolve(X, H, "full");
Fig = plt.figure();
plt.stem(np.arange(0, 19/Size, 1/Size), Y);
plt.xlabel("N");
plt.ylabel("Y = X * H");
plt.title("c) Convolution");
plt.grid(True);
plt.show();

#d)
FFTH = np.fft.fft(H);
FFTX = np.fft.fft(X);
K = Size*T/2-Size/4;
Fig, F = plt.subplots(2, sharex=True, sharey=True);
F[0].stem(K, abs(np.concatenate((FFTX[int(Size/2):Size], FFTX[0:int(Size/2)]))));
F[0].set_title("X Spectrum");
F[0].grid(True);
F[1].stem(K[2:10], abs(np.concatenate((FFTH[4:8], FFTH[0:4]))));
F[1].set_title("H Spectrum");
F[1].grid(True);
plt.xlabel("K[Hz]");
plt.ylabel("|FFT|");
plt.show();

Fig, F = plt.subplots(2, sharex=True, sharey=True);
F[0].stem(K, np.angle(np.concatenate((FFTX[int(Size/2):Size], FFTX[0:int(Size/2)])), deg=True));
F[0].set_title("X Phase Plot");
F[0].grid(True);
F[1].stem(K[2:10], np.angle(np.concatenate((FFTH[4:8], FFTH[0:4])), deg=True));
F[1].set_title("H Phase Plot");
F[1].grid(True);
plt.xlabel("K[Hz]");
plt.ylabel("Phase[°]");
plt.show();

#e)
SpectrumY = [0]*Size;
for I in range(0, 8): SpectrumY[I] = FFTX[I] * FFTH[I];
Fig, F = plt.subplots(2, sharex=True);
F[0].stem(K, abs(np.concatenate((SpectrumY[int(Size/2):Size], SpectrumY[0:int(Size/2)]))));
F[0].set_title("|FFTY|");
plt.grid(True);
F[1].stem(K, np.angle(SpectrumY, deg=True));
F[1].set_title("Y Phase[°]");\
plt.xlabel("K[Hz]");
plt.grid(True);
plt.show();

#f)
H = [0]*Size;
H[int(0.25*Size)] = 1;
FFTH = np.fft.fft(H);
SpectrumY = FFTX * FFTH;
Fig, F = plt.subplots(2, sharex=True);
F[0].stem(K, abs(np.concatenate((SpectrumY[int(Size/2):Size], SpectrumY[0:int(Size/2)]))));
F[0].set_title("|FFTY|");
plt.grid(True);
F[1].stem(K, np.angle(SpectrumY, deg=True));
F[1].set_title("Y Phase[°]");\
plt.xlabel("K[Hz]");
plt.grid(True);
plt.show();

#g)
Y_ = np.fft.ifft(SpectrumY);
Fig = plt.figure();
plt.stem(np.arange(0, 1, 1/Size), abs(Y_));
plt.xlabel("N");
plt.ylabel("Y'[N]");
plt.title("g) Recovered 1 Hz Sawtooth");
plt.grid(True);
plt.show();

#h)
SpectrumY = np.concatenate((FFTX[0:6], [0]*7, FFTX[6:12])) * np.concatenate((FFTH[0:6], [0]*7, FFTH[6:12]));
Y__ = np.fft.ifft(SpectrumY);

Fig, F = plt.subplots(3, sharex=True);
F[0].stem(np.arange(0, 19/Size, 1/Size), Y);
F[0].set_title("Y[N]");
plt.grid(True);
F[1].stem(np.arange(0, 1, 1/Size), Y_);
F[1].set_title("Y'[N]");
plt.grid(True);
F[2].stem(np.arange(0, 19/Size, 1/Size), Y__);
F[2].set_title("Y''[N]");
plt.grid(True);
plt.xlabel("N");
plt.show();
