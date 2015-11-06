import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
T,Us,Ug,Uw,Um = np.genfromtxt('messwerte_temperatur.txt', unpack=True)

# Mittelwert der Offsetspannung abziehen U0=0.0072
Us-=0.0072
Ug-=0.0072
Uw-=0.0072
Um-=0.0072

# Auf der x-Achse soll T⁴-T0⁴ aufgetragen werden:
# Raumtemperatur auf 21 Grad geschaetzt.
T=(T**4-21**4)
def f(m,x,c):
 return m * x + c

parameters1, pcov1 = curve_fit(f, T, Us)
parameters2, pcov2 = curve_fit(f, T, Ug)
parameters3, pcov3 = curve_fit(f, T, Uw)
parameters4, pcov4 = curve_fit(f, T, Um)
plt.plot(T, f(T, *parameters1), 'k-', label='Fit 1')
plt.plot(T, f(T, *parameters2), 'g-', label='Fit 2')
plt.plot(T, f(T, *parameters3), 'r-', label='Fit 3')
plt.plot(T, f(T, *parameters4), 'b-', label='Fit 4')

plt.plot(T, Us, 'kx', label='U schwarz')
plt.plot(T, Ug, 'gx', label='U glänzend')
plt.plot(T, Uw, 'rx', label='U weiß')
plt.plot(T, Um, 'bx', label='U matt')
plt.xlabel(r'$T^{4}-T_0^4 / Grad Celsius$')
plt.ylabel(r'$U / mV$')
#plt.yscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('thermospannung.pdf')
#print(parameters1)
#print(pcov)
#np.savetxt('parameter.txt',parameters1,parameters2,parameters3,parameters4,pcov1,pcov2,pcov3,pcov4, header="Parameter der Fits")
