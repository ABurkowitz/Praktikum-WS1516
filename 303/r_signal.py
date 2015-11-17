import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
import math
x = np.linspace(0, 7)
V , phi = np.genfromtxt('daten/Messung_r.txt', unpack=True)
phi=phi/360*2*np.pi
A=30
def f(A,x):
 return A * np.cos(x)
plt.plot(phi, V , 'rx', label="Messdaten")

plt.plot(x,f(A,x), 'r-',label="Theoriekurve")
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('r_signal.pdf')
