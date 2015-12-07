import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
x, t , uc = np.genfromtxt('ausgleichsrechnungdaten.txt', unpack=True)
T1=t*50
print(T1)
t=t*50*10**(-6)
R=1/48.1
def f(t,A,B,C,D,E):
 return A*np.exp(B*t)*np.cos(C*t+D)+E


plt.plot(t, uc , 'bx', label='Messwerte')
parameters1, pocv = curve_fit(f, t, uc)

plt.plot(t, f(t, *parameters1), 'b-', label='Ausgleichskurve')
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Spannung / U$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('dämpfungschwingung.pdf')

np.savetxt('dämpfungparas.txt',parameters1, header="a,b,c")
fehler1= np.sqrt(np.diag(pocv))
print (parameters1)
print (fehler1)
pi2ny=ufloat(parameters1[1],fehler1[1])
#L(10.11e-3,0.03e-3)
#C(2.098e-9,0.006e-9)
#R1(48.1,0.1)
#R2(509.5,0.5)
#Rap(3.3e3)
#1.22627763e-01   1.63147814e+02   3.47381148e+02   5.80136682e-02
#1.15649731e-02

L=ufloat(10.11e-3,0.03e-3)
C=ufloat(2.098e-9,0.006e-9)
Reff=2*L*pi2ny

print ('pi2ny')
print (pi2ny)
#pi2ny(-5.53+/-0.16)e+03

print ('Reff')
print(Reff)
#Reff-111.9+/-3.3
Rap=unp.sqrt(4*L/C)
print('Rap')
print (Rap)
#Rap4390.4+/-9.0



Tex=1/pi2ny
print('Tex')
print(Tex)
#Tex-0.000181+/-0.000005
#print ('Refft')

#print ('Text')
