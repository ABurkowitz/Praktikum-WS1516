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
V , phi = np.genfromtxt('daten/Messung_or.txt', unpack=True)
phi=phi/360*2*np.pi
C=13
A=7.4*np.pi/2
def f(A,x,C):
 return A * np.cos(x) + C
plt.plot(phi, V , 'rx', label="Messdaten")
#parameters1, cov1 = curve_fit(f, phi, V)
#fehler1= np.sqrt(np.diag(cov1))
#plt.plot(phi, f(phi, *parameters1), 'r-', label='Fit T1')
plt.plot(x,f(A,x,C), 'r-',label="Theoriekurve")
plt.xlabel(r'$Phasenwinkel / rad$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('or_signal.pdf')
#paras1=unp.uarray(parameters1,fehler1)

#np.savetxt('daten/or_signal.txt',unp.nominal_values(paras1), header="A,B,C")

#paras1=unp.uarray(parameters1,fehler1)
