import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#a)
Size = 12;
T = np.arange(0, 4, 1/Size);
X = signal.sawtooth(2*np.pi*T);

Fig = plt.figure();
plt.stem(T, X);
plt.xlabel("N");
plt.ylabel("X[N]");
plt.title("a) 1 Hz Sawtooth");
plt.grid(True);
plt.show();

#b)
