import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import correlated_values, correlation_matrix
x,U = np.genfromtxt('messwerte_abstand.txt', unpack=True)

def f(c,x,d):
 return ( c / (x**2) ) + d

parameters1, pcov = curve_fit(f, x, U, p0=[6,0.2])

plt.xlim(0.5, 21)
plt.ylim(0,1)
z = np.linspace(0.5,21)
#plt.plot(x_plot, f(x_plot, *parameters1), 'y-', label='Fit')
plt.plot(z, (7.54252/z**2)+0.202731, 'g-', label='Fit')
# per Gnuplot geplottet und
#c               = 7.54252          +/- 0.8747       (11.6%)
#d               = 0.202731         +/- 0.00492      (2.427%)

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
