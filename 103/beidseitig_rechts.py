import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const

x, d0, dm = np.genfromtxt('messwerte_stab1_beidseitig_rechts.txt', unpack=True)
#Einheiten in SI
x/=100
d0/=1000
dm/=1000
L=0.553
m=4.6897
h=0.01

dx=dm-d0
a=4*x**3 - 12*L*x**2 + 9*(L**2)*x - L**3

def f(a,b,c):
 return ( b * a ) + c

parameters1, pcov = curve_fit(f, a, dx)
a_plot = np.linspace(0.02,0.18)
plt.xlim(0.02,0.18)
plt.plot(a_plot,f(a_plot,*parameters1), 'g-', label='Fit')

plt.plot(a,dx, 'rx', label='Messwerte')
plt.xlabel(r'$\left(4 x^3 - 12 L x^2 + 9 L^2 x - L^3\right)} / m^3$')
plt.ylabel(r'$D(x) / m$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('stab1_beidseitig_rechts.pdf')

parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)

#Ausgabe:
#0.01207+/-0.00006
#(4.8+/-0.8)e-05
#
#(0.012074401751652291+/-5.565018647514912e-05, 4.8030418172796886e-05+/-8.120504158407705e-06)
#[[  3.09694325e-09  -4.34868178e-10]
# [ -4.34868178e-10   6.59425878e-11]]

#Elasitzitätsmodul:
E = (m * const.g)/(4*h**4*parameters1[0])
print(E)
# (9.52+/-0.04)e+10
