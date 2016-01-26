
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
#fitparas=w[0:-3]
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
T0=R2e*C*0.5
def phi(a,b):
    return (a/b)*2*np.pi
ph=(0,0,0,0,0.09424777,0.19603538,0.24881414,0.42474333,0.41494156,0.47500881,
    0.5629734,0.64194048,0.64465481,0.72382295,0.69240702,0.72288047,
    0.7115079,0.75398224,0.8022371,0.89598222,1.02918575,1.22522113,
    1.12594681,1.28553971,1.47340695,1.62357508,1.69080517,1.87364586,
    1.80327418,1.99051311,2.18529185,2.19660158,2.25440689,2.56353961,
    2.63893783,2.89026524,3.01592895,3.0787608,3.11592895,3.16460154,3.1)
    #3.01592895,3.16460154,3.1)
#2.76460154,0)
#ph=( 0.,          0.,          0.,          0.,                 0,   0.19603538,
#  0.24881414,  0.41494156,  0.42474333,  0.47500881,  0.5629734  , 0.64194048,
#  0.64465481,  0.72382295,  0.69240702,  0.72288047,  0.7115079  , 0.75398224,
#  0.8022371 ,  0.89598222,  1.02918575,  1.22522113,  1.12594681 , 1.28553971,
#  1.47340695,  1.62357508-np.pi,  1.69080517-np.pi,  1.80327418-np.pi,  1.87364586-np.pi , 1.99051311-np.pi,
#  2.18529185-np.pi,  2.19660158-np.pi,  2.25440689-np.pi,  2.56353961-np.pi,  2.63893783-np.pi , 2.89026524-np.pi,
#  3.01592895-np.pi,  3.0787608 -np.pi,  3.01592895-np.pi,  2.76460154-np.pi,  0.)
def g(ome,a_1,a_0,a_2,a_3):
#    return (a_3+a_2*np.arctan(a_0*(a_1+ome)))
##    return (np.arctan(-ome*a_0/(1-a_1*ome**2)))
#    return (np.arctan(ome*T0/(1-T1*ome**2)))
#    return (np.arctan(ome*30)+1.5)
    return (a_2*np.arctan(a_0*(ome-a_1))+a_3)
#    return (np.arctan(-ome*a_0/(1-a_1*ome**2)))
#-3.43991515e-06   3.18309728e-07   2.91324254e+00  -5.42683776e-01]

params, covar = curve_fit(g,w,ph,p0=[40.000,0.00001,1,0])
#x_plot1 = np.linspace(-10, 10, 1000)
x_plot1 = np.linspace(300, 9000000, 100000)
#plt.plot(x_plot1, g(x_plot1, *params), 'b-', label="Fit")
plt.errorbar(w, phi(a,b) + (a / 10), xerr=None, yerr=(a / 10), fmt='rx', label="Phasenverschiebung")
#plt.errorbar(w, phi(a,b) + (a / 10), xerr=None, yerr=(a / 10), fmt='rx', label="Phasenverschiebung")
#plt.legend(loc='best')
#plt.tight_layout(pad=0, h_pad=1.1, w_pad=1.08)
#plt.plot(x_plot1,g(x_plot1))
plt.plot(x_plot1,g(x_plot1,*params))
plt.xscale('log')
plt.xlabel(' $\omega \;in\; \mathrm{ Hz }$')
plt.ylabel('$\phi \;$in$\;\mathrm{rad}$')
#plt.plot(f,phi(a,b),'r.')
#plt.plot(f,phi(a,b),'r+')
print(T0)
print(T1)
print(params)
fehler= np.sqrt(np.diag(covar))
print(fehler)
plt.savefig('phasenverschiebung.pdf')
plt.show()
print(phi(a,b))

#plt.errorbar(f,phi(a,b),xerr=errX, yerr=errY,fmt='none')
#plt.savefig('phasenverschiebung.pdf')
print(1.50e-6/(1/10000)*2*np.pi)

  #0.
  #0.
  #0.
  #0.
  #0.09424777
  #0.19603538
  #0.24881414
  #0.42474333
  #0.41494156
  #0.47500881
  #0.5629734
  #0.64194048
  #0.64465481
  #0.72382295
  #0.69240702
  #0.72288047
  #0.7115079
  #0.75398224
  #0.8022371
  #0.89598222
  #1.02918575
  #1.22522113
  #1.12594681
  #1.28553971
  #1.47340695
  #1.62357508
  #1.69080517
  #1.87364586
  #1.80327418
  #1.99051311
  #2.18529185
  #2.19660158
  #2.25440689
  #2.56353961
  #2.63893783
  #2.89026524
  #3.01592895
  #3.0787608
  #3.01592895
  #2.76460154
