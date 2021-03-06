import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
f, uc , a = np.genfromtxt('messwerte_phasenverschiebung.txt', unpack=True)

#L(10.11e-3,0.03e-3)
#C(2.098e-9,0.006e-9)
#R1(48.1,0.1)
#R2(509.5,0.5)
#Rap(3.3e3)

#def g(t,B,C):
# return 1/np.sqrt((1-B*t**2)**2+t**2*C)
def g(nu,  a_0, a_1):
    return (1/ np.sqrt((1 - a_0 * nu ** 2) ** 2 + (nu ** 2) * a_1))
nu = np.linspace(500, 900000, 9000)
parameters1, pocv = curve_fit(g, f, uc, maxfev=10000)
plt.plot(nu, g(nu,*parameters1) , 'r-')
print(parameters1)
fehler= np.sqrt(np.diag(pocv))
print(fehler)
errX=0.1
errY=0.001
plt.errorbar(f,uc,xerr=errX, yerr=errY,fmt='none')
plt.plot(f, uc , 'b.', label="Kondensatorspannung")

plt.xlabel(r'$Frequenz / Hz$')
plt.ylabel(r'$Uc/U$')
plt.xscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Kondensatorspannungen.pdf')

L=ufloat(10.11e-3,0.03e-3)
C=ufloat(2.098e-9,0.006e-9)
R=ufloat(509.5,0.5)
Re=R+50

rdiffomega=Re/L
romegares=unp.sqrt(1/(C*L)-(Re/L)**2/2)
print ('rdiffomega')
print (rdiffomega)
print ('romegares')
print (romegares)
rguete=romegares/rdiffomega
print ('rguete')
print (rguete)
eomegadiff=ufloat(10000,0.1)
eomegares=ufloat(33500,0.1)
eguete=1/eomegadiff*eomegares
print (eguete)
#(rdiffomega)(5.040+/-0.016)e+04
#(romegares)(2.171+/-0.004)e+05
#(rguete)4.309+/-0.010

omegares=unp.sqrt(1/(L*C)-(Re/L)**2/2)
omega0=unp.sqrt(1/(L*C))
omega1=Re/(L*2)+unp.sqrt((Re/(2*L))**2+1/(L*C))
omega2=-Re/(L*2)+unp.sqrt((Re/(2*L))**2+1/(L*C))
print('omegares')
print(omegares)
print('omega0')
print(omega0)
print('omega1')
print(omega1)
print('omega2')
print(omega2)
#omegares(2.136+/-0.004)e+05
#omega0=(2.171+/-0.004)e+05
#omega1=(2.438+/-0.005)e+05
#omega2=(1.934+/-0.004)e+05

#print ('momega1')
#Ra=ufloat(48.1,0.1)
#momega1=-Re/(2*L)+unp.sqrt((Re/(2*L))**2+1/(L*C))
#print (momega1)

#momega1=1/(10.11e-3*2.098e-9)-(559.5/10.11e-3)**2/2

#momega1=np.sqrt(45614511336.33989)
#print (momega1)
