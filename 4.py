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
plt.title("b) Convolution");
plt.grid(True);
plt.show();
