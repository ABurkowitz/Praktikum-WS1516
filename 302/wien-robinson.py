import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
v,Ubr = np.genfromtxt('messwerte_wien-robinson.txt', unpack=True)
Us=6.94
R=1000
C=6.527*10**(-7)
w0=1/(R*C)
print(w0)
def f(w):
    return np.sqrt((1/9)*((((w/w0)**2-1)**2)/((1-(w/w0)**2)**2+9*(w/w0)**2)))

w=240*np.linspace(10e-2,10e3,num=50000)
print(w)
plt.xlim(10e-2,10e1)
plt.plot(w/w0, f(w), 'g-', label='Theoriekurve')
plt.xscale('log')
plt.plot(v/240, Ubr/Us, 'rx', label='Messwerte')

plt.xlabel(r'$\Omega = \frac{v}{v_0}$')
plt.ylabel(r'$\frac{U_{Br}}{U_{s}}$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('wien-robinson.pdf')
