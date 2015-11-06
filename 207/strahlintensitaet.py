import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
x,U = np.genfromtxt('messwerte_abstand.txt', unpack=True)


def f(m,x,c):
 return m * x + c


parameters1, pcov = curve_fit(f, x, U)

plt.plot(x, f(x, *parameters1), 'g-', label='Fit')
plt.plot(x, U, 'rx', label='Messwerte Thermospannung')
plt.xlabel(r'$x / cm$')
plt.ylabel(r'$U / mV$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('strahlintensitaet.pdf')
print(parameters1)
print(pcov)
#np.savetxt('daten/ausglkurve_pT.txt',parameters1, header="m,T,C")
