
import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
import cmath as ac
#a: Abstand der Nulldurchgaenge
#f: Frequenz
f, Uc, a = np.genfromtxt('messwerte_phasenverschiebung.txt', unpack=True)
w=f*2*np.pi
L=10.11e-3
#,0.03e-3)
C=2.098e-9
#,0.006e-9)
R1=48.1
#,0.1)
R2=509.5
#,0.5)
R2e=R2*3
Rap=3.3e3
b=1/f
T1=L*C*1
T0=R2e*C*1
def phi(a,b):
    return (a/b)*2*np.pi
ph=(0,0,0,0,0.09424777,0.19603538,0.24881414,0.42474333,0.41494156,0.47500881,
    0.5629734,0.64194048,0.64465481,0.72382295,0.69240702,0.72288047,
    0.7115079,0.75398224,0.8022371,0.89598222,1.02918575,1.22522113,
    1.12594681,1.28553971,1.47340695,1.62357508,1.69080517,1.87364586,
    1.80327418,1.99051311,2.18529185,2.19660158,2.25440689,2.56353961,
    2.63893783,2.89026524,3.01592895,3.0787608,3.01592895,3.16460154,3.1)
#2.76460154,0)
def g(ome,  a_0, a_1):
    return (1.5*np.arctan(-ome*a_0/(1-a_1*ome**2)))

params, covar = curve_fit(g,w,ph,p0=[T0,T1])
x_plot1 = np.linspace(300, 3000000, 100000)
plt.plot(x_plot1, g(x_plot1, *params), 'b-', label="Fit")
plt.errorbar(w, phi(a,b) + (a / 10), xerr=None, yerr=(a / 10), fmt='rx', label="Phasenverschiebung")
plt.legend(loc='best')
#plt.tight_layout(pad=0, h_pad=1.1, w_pad=1.08)
plt.xlim(1.6e5, 2.5e5)
plt.xscale('log')
plt.xlabel(' $\omega \;in\; \mathrm{ kHz }$')
plt.ylabel('$U_c/U_0$')
#plt.plot(f,phi(a,b),'r.')
#plt.plot(f,phi(a,b),'r+')


plt.savefig('linphasenverschiebung.pdf')
plt.show()
