import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
T,p = np.genfromtxt('data2.txt', unpack=True)
p=p/1000
lnp=np.log(p)


T1=unp.uarray([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0,110.0,111.0,112.0,113.0,114.0,115.0,116.0,117.0,118.0,119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0],
              [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
T=T+273.15
T1=T1+273.15
kT1=1/T1
R=8.3144598
print(kT1[0])
print(kT1[26])
def g(t,A,B):
    return (-A/R*t+B)

x = np.linspace(0.0026, 0.0032,1000)
parameters1, pocv = curve_fit(g, 1/T, lnp, maxfev=10000)
plt.plot(x, g(x,*parameters1) , 'r-', label="Fit")
errX=0.0000001
errY=0.0000001
plt.errorbar(1/T,lnp,xerr=errX, yerr=errY,fmt='none', label="Messwerte")
#plt.plot(1/T, lnp , 'b.', label="Messwerte")
print('parameter')
print(parameters1)
fehler= np.sqrt(np.diag(pocv))
print(fehler)
plt.xlabel(r'Temperaturkehrwert $1/T$ in 1/K')
plt.ylabel(r'  log $p/p_0$')
plt.xlim(0.0026,0.0031)
#plt.xscale('log')
plt.tight_layout()
plt.legend(loc='best')
#plt.show()
plt.savefig('verdampfungwaerme1.pdf')
L=ufloat(parameters1[0],fehler[0])
La=ufloat(R*373.15,0.0000057)
li=L-La
lie=li/(6.022140857*10**23)/(1.6021766208*10**(-19))
print(La)
print(li)
print(lie)
druck=np.array([-5.74,-5.68,-5.66,-5.61,-5.57,-5.52,-5.47,-5.42,-5.37,-5.31,-5.25,-5.20,-5.14,-5.08,-5.01,-4.95,-4.88,-4.81,-4.75,-4.68,-4.60,-4.52,-4.46,-4.38,-4.30,-4.22,-4.14])
druck=druck+6.74
print(druck)
print(T)
# 1.
# 1.06
# 1.08
# 1.13
# 1.17
# 1.22
# 1.27
# 1.32
# 1.37
# 1.43
# 1.49
# 1.54
# 1.6
# 1.66
# 1.73
# 1.79
# 1.86
# 1.93
# 1.99
# 2.06
# 2.14
# 2.22
# 2.28
# 2.36
# 2.44
# 2.52
# 2.6
