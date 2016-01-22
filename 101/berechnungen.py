import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
import scipy.constants as const
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

phi, F = np.genfromtxt('messwerte_statisch.txt', unpack=True)
r=0.14885
# Winkel: Grad in rad umrechnen:
#phi = (2*np.pi*phi)/360
phi = np.deg2rad(phi)
#print(phi)
phi_u = unp.uarray(phi,0.087)

D1 = (F*r)/phi_u
print('Winkelrichtgroesse D (statisch):')
D1_mittel = np.mean(D1)
print(D1_mittel)
print()


a, T = np.genfromtxt('messwerte_dynamisch.txt', unpack=True)
# eine Periode:
T/=5
# Haelfte der Zylinderlaenge noch draufaddieren, da der Abstand bis zum Beginn
# des Zylinders gemessen wurde h/2 = 1.485 cm
a+=1.485
#print(a)
# cm in m
a/=100


x=a**2
y=T**2
def f(x,b,c):
 return ( b * x ) + c

parameters1, pcov = curve_fit(f, x, y)
x_plot = np.linspace(0,0.041)
plt.xlim(0,0.041)
plt.plot(x_plot,f(x_plot,*parameters1), 'g-', label='Fit')


plt.plot(a**2,T**2, 'rx', label='Messwerte')
plt.xlabel(r'$a^2 / m^2$')
plt.ylabel(r'$T^2 / s^2$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('dynamisch.pdf')

parameters1 = correlated_values(parameters1, pcov)
print('Fitparameter:')
for param1 in parameters1:
    print(param1)
print()
#print(parameters1)
#print(pcov)

# Berechnung der Winkelrichtgroesse D nach der dynamischen Methode
m1=0.22343
m2=0.22250
D2 = 4 * np.pi**2 * (m1 + m2) * (1/parameters1[0])
print('Winkelrichtgroesse D (dynamisch):')
print(D2)


# Eigentraegheitsmoment:
R1=ufloat(0.01723,0.00001)
R2=ufloat(0.01737,0.00003)
h1=ufloat(0.02972,0.00002)
h2=ufloat(0.02973,0.00002)

I_D=m1*(R1**2/4 + h1**2/12) + m2*(R2**2/4 + h2**2/12) - (parameters1[1]/parameters1[0])*(m1+m2)
print('Eigentraegheitsmoment:')
print(I_D)
print()

# Winkelrichtgroesse der zwei Methoden mitteln:
D=(D1_mittel+D2)/2

# Berechnung des Trägheitsmoments von Zylinder 1
m_Z1 = 1.0739
r_Z1 = ufloat(0.03975,0.00005)
T1 = ufloat(1.673,0.005)

I_Z1t = 0.5 * m_Z1 * r_Z1**2
print('I_Z1 theoretisch:')
print(I_Z1t)

I_Z1e = (T1**2 * D) / (4*np.pi**2) - I_D
print('I_Z1 experimentell:')
print(I_Z1e)
print()


# Berechnung des Trägheitsmoments von Zylinder 2
m_Z2 = 1.5254
r_Z2 = ufloat(0.04003,0.00002)
h_Z2 = ufloat(0.13957,0.00007)
T2 = ufloat(2.324,0.009)

I_Z2t = m_Z2 * ((r_Z2**2 / 4)+(h_Z2**2/12))
print('I_Z2 theoretisch:')
print(I_Z2t)

I_Z2e = (T2**2 * D) / (4*np.pi**2) - I_D
print('I_Z2 experimentell:')
print(I_Z2e)
print()



# Ausgabe
#[ 1.57079633  1.74532925  2.0943951   2.61799388  3.14159265  3.4906585
#  4.01425728  4.71238898  5.23598776  5.75958653]
#Winkelrichtgroesse D (statisch):
#0.02627+/-0.00028
#
#[  3.485   5.485   7.485   9.485  11.485  13.485  15.485  17.485  19.485
#  21.485]
#Fitparameter:
#859.8+/-14.9
#6.0+/-0.4
#
#Winkelrichtgroesse D (dynamisch):
#0.02048+/-0.00035
#Eigentraegheitsmoment:
#-0.00302+/-0.00023
#
#I_Z1:
#0.0008484+/-0.0000021
#
#I_Z2:
#0.0012222+/-0.0000012
