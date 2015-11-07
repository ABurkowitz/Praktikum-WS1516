import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import correlated_values, correlation_matrix
x,U = np.genfromtxt('messwerte_abstand.txt', unpack=True)


def f(m,x,c):
 return m * x + c

#def g(a,x,b):
# return (a / x) + b
#
#def h(d,x,e):
# return (d / x**2) + e

parameters1, pcov = curve_fit(f, x, U)
#parameters2, pcov2 = curve_fit(g, x, U)
#parameters3, pcov3 = curve_fit(h, x, U)

plt.plot(x, f(x, *parameters1), 'g-', label='linearer Fit')
#plt.plot(x, g(x, *parameters2), 'b-', label='1/r Fit')
#plt.plot(x, h(x, *parameters3), 'y-', label='1/r^2 Fit')
plt.plot(x, U, 'rx', label='Messwerte Thermospannung')
plt.xlabel(r'$x / cm$')
plt.ylabel(r'$U / mV$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('strahlintensitaet.pdf')
parameters1 = correlated_values(parameters1, pcov)
for param1 in parameters1:
    print(param1)
print()
print(parameters1)
print(pcov)
#np.savetxt('daten/ausglkurve_pT.txt',parameters1, header="m,T,C")