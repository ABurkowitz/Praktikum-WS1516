import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt', unpack=True)
#min in sekunden
t= t*60
T1 = ufloat(T1 + 273.15 , 0.1)
T2 = ufloat(T2 + 273.15 , 0.1)

def f(t,A,B,C):
 return A * t **2 + B * t + C
def g(t,a,b,c):
 return a * t **2 + b * t +c

plt.plot(t, T1 , 'rx', label="Temperatur T1")
plt.plot(t, T2 , 'bx', label="Temperatur T2")
parameters1, pocv = curve_fitx = ufloat(5, 1)(f, t, T1)
parameters2, pocv = curve_fit(g, t, T2)
plt.plot(t, f(t, *parameters1), 'r-', label='Fit T1')
plt.plot(t, f(t, *parameters2), 'b-', label='Fit T2')
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Tempratur / K$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Temperaturgraphik.pdf')

np.savetxt('daten/ausglkurve_T1.txt',parameters1, header="A,B,C")
np.savetxt('daten/ausglkurve_T2.txt',parameters2, header="a,b,c")

t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt', unpack=True)
#min in sekunden
t= t*60
T1 = T1 + 273.15
T2 = T2 + 273.15

def f(t,A,B,C):
 return A * t **2 + B * t + C
def g(t,a,b,c):
 return a * t **2 + b * t +c

plt.plot(t, T1 , 'rx', label="Temperatur T1")
plt.plot(t, T2 , 'bx', label="Temperatur T2")
parameters1, pocv = curve_fit(f, t, T1)
parameters2, pocv = curve_fit(g, t, T2)
plt.plot(t, f(t, *parameters1), 'r-', label='Fit T1')
plt.plot(t, f(t, *parameters2), 'b-', label='Fit T2')
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Tempratur / K$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Temperaturgraphik.pdf')

np.savetxt('daten/ausglkurve_T1.txt',parameters1, header="A,B,C")
np.savetxt('daten/ausglkurve_T2.txt',parameters2, header="a,b,c")
