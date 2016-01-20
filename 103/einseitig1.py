import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

x, d0, dm = np.genfromtxt('messwerte_stab1_einseitig.txt', unpack=True)
#Einheiten in SI
x/=100
d0/=1000
dm/=1000
L=0.49
m=1.0205
h=0.01

dx=dm-d0
a=0.49 * (x**2) - ((x**3) / 3)


np.savetxt('werte_1.txt', dx)
np.savetxt('einseitig1_berechnete_werte.txt', a)

def f(a,b,c):
 return ( b * a ) + c

parameters1, pcov = curve_fit(f, a, dx)
a_plot = np.linspace(0,0.08)
plt.xlim(0,0.08)
plt.plot(a_plot,f(a_plot,*parameters1), 'g-', label='Fit')

plt.plot(a,dx, 'rx', label='Messwerte')
plt.xlabel(r'$\left(L x^2-\frac{x^3}{3}\right) / m^3$')
plt.ylabel(r'$D(x) / m$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('stab1_einseitig.pdf')

parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)

#Ausgabe:
#0.06566+/-0.00023
#(5.7+/-1.2)e-05
#
#(0.06565624625512359+/-0.0002273424226440303, 5.658138734608184e-05+/-1.1937364033455201e-05)
#[[  5.16845771e-08  -2.45941014e-09]
# [ -2.45941014e-09   1.42500660e-10]]
#

#a1=ufloat(parameters1[0].n,parameters1[0].s)
# braucht man nicht, da python, wenn man parameters1[0] schreibt, mit ufloats rechnet.

#Elasitzitätsmodul:
E = (6 * m * const.g)/(h**4*parameters1[0])
print(E)


# Berechnung Mittelwert des Emoduls von Stab 1
e1=ufloat(9.146e+10,0.032e+10)
e2=ufloat(9.46e+10,0.20e+10)
e3=ufloat(9.52e+10,0.04e+10)

e=(e1+e2+e3)/3
print(e)

#Standardabweichung des Mittelwerts
s=unp.sqrt(1/6 *( (e1-e)**2 + (e2-e)**2 + (e3-e)**2 ))
print(s)
