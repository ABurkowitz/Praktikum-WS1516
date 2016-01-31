import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
T,p = np.genfromtxt('data1.txt', unpack=True)

a=0.9
p=(p+6.74)
#*10**5
lnp=np.log(p)


T1=unp.uarray([100.0,101.0,102.0,103.0,104.0,105.0,106.0,107.0,108.0,109.0,110.0,111.0,112.0,113.0,114.0,115.0,116.0,117.0,118.0,119.0,120.0,121.0,122.0,123.0,124.0,125.0,126.0],
              [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
T=T+273.15
T1=T1+273.15
kT1=1/T1
R=8.3144598
print(kT1[0])
print(kT1[26])
def g(t,  A,B,C,D):
    return (A*t**3+B*t**2+C*t+D)

x = np.linspace(370, 400,1000)
parameters1, pocv = curve_fit(g, T, p, maxfev=10000)
#plt.plot(x, g(x,*parameters1) , 'r-', label="Fit")
errX=0.0000001
errY=0.0000001
#plt.errorbar(T,p,xerr=errX, yerr=errY,fmt='none')
#plt.plot(T, p , 'b.', label="Messwerte")
print('parameter')
print(parameters1)
fehler= np.sqrt(np.diag(pocv))
print(fehler)
plt.xlabel(r'Temperatur $T$ in K')
plt.ylabel(r'Verdampfungswärme  $L$  in $10^3$J/mol')
#plt.xscale('log')
plt.tight_layout()



print(T)

Lp=((R*T)/2+np.sqrt(((R*T/2)**2)-a*(parameters1[0]*T**3+parameters1[1]*T**2+parameters1[2]*T+parameters1[3])))

Lp=Lp*(3*parameters1[0]*T**3+2*parameters1[1]*(T**2)+parameters1[2]*T)
Lp=Lp/(parameters1[0]*T**3+parameters1[1]*T**2+parameters1[2]*T+parameters1[3])
Lp=Lp/1000
#Lp=((R*T)/2+np.sqrt((R*T/2)**2-a*(parameters1[0]*T**3+parameters1[1]*T**2+parameters1[2]*T+parameters1[3])))
#Lp=Lp*(parameters1[0]*T**3+parameters1[1]*T**2+parameters1[2]*T)/(parameters1[0]*T**3+parameters1[1]*T**2+parameters1[2]*T+parameters1[3])
print(Lp)
plt.errorbar(T,Lp,xerr=errX, yerr=errY,fmt='none')
plt.plot(T, Lp , 'b.', label="Verdampfungswärme")
plt.legend(loc='best')
plt.savefig('verdampfungwaerme3.pdf')
#plt.show()
