import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
p,T = np.genfromtxt('daten/Dampfdruckkurve_array.txt', unpack=True)
#R=8.314 4598 J mol-1 K-1
R=8.3144598
T=T+273.15
T=1/T
def f(m,T,C):
 return m * T + C

lnp=np.log(p)
plt.plot(T, lnp , 'rx', label="Temperatur T1")
parameters1, pocv = curve_fit(f, T, lnp)

plt.plot(T, f(T, *parameters1), 'r-', label='Fit T1')

plt.xlabel(r'$\frac{1}{T}/\frac{1}{K}$')
plt.ylabel(r'$ln(\frac{p}{p_0})$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('daten/Dampfdruckkurve.pdf')

np.savetxt('daten/ausglkurve_pT.txt',parameters1, header="m,T,C")
m=parameters1[0]
L= - m *R
print (L)
#np.savetxt('daten/Verdampfungswaerme.txt', L , header="Verdampfungswaerme_L")
