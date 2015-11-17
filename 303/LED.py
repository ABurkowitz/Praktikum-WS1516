import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
import math
x = np.linspace(5.1, 180)
g , d, v = np.genfromtxt('daten/LED_abstand.txt', unpack=True)
v=v/g
r=x*x
o=4*np.pi
C=0.5
def f(o,r):
 return  o/r
plt.plot(d, v , 'rx', label="Messdaten")

plt.plot(x,f(o,r), 'r-',label="Theoriekurve")
plt.xlabel(r'$Abstand / cm$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('LED.pdf')
