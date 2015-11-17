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
g , d, v = np.genfromtxt('daten/LED_abstand.txt', unpack=True)
v=v/g
def f(A,x,C):
 return A * d + C
plt.plot(d, v , 'rx', label="Messdaten")

#plt.plot(x,f(A,x), 'r-',label="Theoriekurve")
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('LED.pdf')
