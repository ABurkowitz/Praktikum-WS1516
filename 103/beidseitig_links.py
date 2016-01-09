import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const

x, d0, dm = np.genfromtxt('messwerte_stab1_beidseitig_links.txt', unpack=True)
#Einheiten in SI
x/=100
d0/=1000
dm/=1000
L=0.553
m=4.6897
h=0.01

dx=dm-d0
a=3*L**2 *x - 4*x**3

def f(a,b,c):
 return ( b * a ) + c

parameters1, pcov = curve_fit(f, a, dx)
plt.plot(a,f(a,*parameters1), 'g-', label='Fit')

plt.plot(a,dx, 'rx', label='Messwerte')
plt.xlabel(r'$L x^2-\frac{x^3}{3} / m^3$')
plt.ylabel(r'$D(x) / m$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('stab1_beidseitig_links.pdf')

parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)

#Ausgabe:
#0.01215+/-0.00026
#(3.9+/-3.8)e-05
#
#(0.012148489634388785+/-0.00026141830644587375, 3.87212718805573e-05+/-3.805538808440429e-05)
#[[  6.83395309e-08  -9.56185419e-09]
# [ -9.56185419e-09   1.44821256e-09]]

#Elasitzitätsmodul:
E = (m * const.g)/(4*h**4*parameters1[0])
print(E)

# (9.46+/-0.20)e+10
