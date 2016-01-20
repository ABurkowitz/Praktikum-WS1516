import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const

x, d0, dm = np.genfromtxt('messwerte_stab2_einseitig.txt', unpack=True)
#Einheiten in SI
x/=100
d0/=1000
dm/=1000
L=0.49
m=0.5285
r=0.005

dx=dm-d0
a=0.49 * (x**2) - ((x**3) / 3)

np.savetxt('werte_2.txt', dx)
np.savetxt('einseitig2_berechnete_werte.txt', a)

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
plt.savefig('stab2_einseitig.pdf')

parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)

#Ausgabe:
#0.06007+/-0.00020
#(6.6+/-1.0)e-05
#
#(0.06006796128396497+/-0.00019830358084137499, 6.611099424467891e-05+/-1.0412583882012512e-05)
#[[  3.93243102e-08  -1.87124696e-09]
# [ -1.87124696e-09   1.08421903e-10]]

#Elasitzitätsmodul:
E = (2 * m * const.g)/(const.pi*r**4*parameters1[0])
print(E)
# (8.789+/-0.029)e+10
