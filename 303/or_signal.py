import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
import math

V , phi = np.genfromtxt('daten/Messung_or.txt', unpack=True)
phi=phi/360*2*np.pi
C=12
A=12
def f(A,phi,C):
 return A * np.cos(phi) + C
plt.plot(phi, V , 'rx', label="Temperatur T1")
#parameters1, cov1 = curve_fit(f, phi, V)
#fehler1= np.sqrt(np.diag(cov1))
#plt.plot(phi, f(phi, *parameters1), 'r-', label='Fit T1')
plt.plot(phi,f(A,phi,C))
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Spannung / V$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('or_signal.pdf')
#paras1=unp.uarray(parameters1,fehler1)

#np.savetxt('daten/or_signal.txt',unp.nominal_values(paras1), header="A,B,C")

#paras1=unp.uarray(parameters1,fehler1)
