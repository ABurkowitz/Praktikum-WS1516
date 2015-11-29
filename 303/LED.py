import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
import math
x = np.linspace(5.1, 180,1000)
g , d, v = np.genfromtxt('daten/LED_abstand.txt', unpack=True)
v=v/g
r=d*d
o=4*np.pi


def f(o,r):
 return  1/(o*r**2)
plt.plot(d, v , 'rx', label="Messdaten")
#plt.xscale('log',basex=2)
#plt.yscale('log',basey=2)
plt.plot(d,f(o,r), 'r-',label="Theoriekurve")
plt.xlabel(r'$Abstand / cm$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('LED.pdf')
