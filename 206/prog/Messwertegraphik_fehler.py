import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt', unpack=True)
#min in sekunden
t= t*60
T1 = T1 + 273.15
T2 = T2 + 273.15
t1 = unp.uarray(T1 , 0.1)
t2 = unp.uarray(T2 , 0.1)
def ucurve_fit(f,x,y, **kwargs):
    if np.any(unp.std_devs(y)==0):
        sigma= None
    else:
        sigma=unp.std_devs(y)

    popt, pcov =scipy.optimize.curve_fit(f,x, unp.nominal_values(y),sigma=sigma, **kwargs)

    return unc.correlated_values(popt, pcov)



def f(t,A,B,C):
 return A * t **2 + B * t + C
def g(t,a,b,c):
 return a * t **2 + b * t +c

plt.plot(t, unp.nominal_values(t1) , 'rx', label="Temperatur T1")
plt.plot(t, unp.nominal_values(t2) , 'bx', label="Temperatur T2")
parameters1, pocv = ucurve_fit(f, t, t1)
parameters2, pocv = ucurve_fit(g, t, t2)
plt.plot(t, f(t, *parameters1), 'r-', label='Fit T1')
plt.plot(t, f(t, *parameters2), 'b-', label='Fit T2')
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Tempratur / K$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Temperaturgraphik.pdf')

np.savetxt('daten/ausglkurve_T1.txt',parameters1, header="A,B,C")
np.savetxt('daten/ausglkurve_T2.txt',parameters2, header="a,b,c")
