import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

a, T = np.genfromtxt('messwerte_dynamisch.txt', unpack=True)
# eine Periode:
T/=5
# Haelfte der Zylinderlaenge noch draufaddieren, da der Abstand bis zum Beginn
# des Zylinders gemessen wurde h/2 = 1.485 cm
a+=1.485
# cm in m
a/=100


x=a**2
y=T**2
def f(x,b,c):
 return ( b * x ) + c

parameters1, pcov = curve_fit(f, x, y)
x_plot = np.linspace(0,0.041)
plt.xlim(0,0.041)
plt.plot(x_plot,f(x_plot,*parameters1), 'g-', label='Fit')


plt.plot(a**2,T**2, 'rx', label='Messwerte')
plt.xlabel(r'$a^2 / m^2$')
plt.ylabel(r'$T^2 / s^2$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('dynamisch.pdf')

parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)

# Ausgabe
#859.8+/-14.9
#6.0+/-0.4
#
#(859.792980724919+/-14.864754587544962, 5.957209931216193+/-0.355184226447176)
#[[  2.20960929e+02  -4.17340457e+00]
# [ -4.17340457e+00   1.26155835e-01]]
