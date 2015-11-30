import numpy as np
#import scipy.optimize
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#import uncertainties as unc
#import uncertainties.unumpy as unp
#from uncertainties import correlated_values, correlation_matrix
#from uncertainties import ufloat
#import math
g , d, v = np.genfromtxt('daten/LED_abstand.txt', unpack=True)
v=v/g
r=d*d
o=4*np.pi


def f(x):
 return  150/(4*np.pi*(x**2))

plt.plot(d, v , 'rx', label="Messdaten")
plt.xscale('log')
plt.yscale('log')
plt.xlim(5.1, 150)
x = np.linspace(5.1, 150,1000)
plt.plot(x,f(x), 'r-',label="Theoriekurve")
plt.xlabel(r'$Abstand / cm$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('LED.pdf')
