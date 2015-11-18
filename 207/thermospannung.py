import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import correlated_values, correlation_matrix
T,Us,Ug,Uw,Um = np.genfromtxt('messwerte_temperatur.txt', unpack=True)

# Mittelwert der Offsetspannung abziehen U0=0.0072
Us-=0.0072
Ug-=0.0072
Uw-=0.0072
Um-=0.0072

# Grad Celsius in Kelvin
T+=273.15
# Auf der x-Achse soll T⁴-T0⁴ aufgetragen werden:
# Raumtemperatur auf 21 Grad geschaetzt.
T=(T**4-21**4)
def f(m,x,c):
 return m * x + c
#np.savetxt('werte.txt',np.column_stack((T,Us,Ug,Uw,Um)), header='T^4-T0^4, Us-U0, Ug-U0, Uw-U0, Um-U0')

plt.plot(T, Us, 'kx', label='U schwarz')
plt.plot(T, Ug, 'gx', label='U glänzend')
plt.plot(T, Uw, 'rx', label='U weiß')
plt.plot(T, Um, 'bx', label='U matt')

parameters1, pcov1 = curve_fit(f, T, Us)
parameters2, pcov2 = curve_fit(f, T, Ug)
parameters3, pcov3 = curve_fit(f, T, Uw)
parameters4, pcov4 = curve_fit(f, T, Um)

plt.plot(T, f(T, *parameters1), 'k-', label='Fit schwarz')
plt.plot(T, f(T, *parameters2), 'g-', label='Fit glänzend')
plt.plot(T, f(T, *parameters3), 'r-', label='Fit weiß')
plt.plot(T, f(T, *parameters4), 'b-', label='Fit matt')

plt.xlabel(r'$T^{4}-T_0^4 / K^4$')
plt.ylabel(r'$U / mV$')
#plt.yscale('log')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('thermospannung.pdf')

print('Fit schwarz')
parameters1 = correlated_values(parameters1, pcov1)
for param1 in parameters1:
    print(param1)
#epsilon_s == 1

print('Fit glaenzend')
parameters2 = correlated_values(parameters2, pcov2)
for param2 in parameters2:
    print(param2)
epsilon_g = parameters2[0] / parameters1[0]
print(epsilon_g)

print('Fit weiss')
parameters3 = correlated_values(parameters3, pcov3)
for param3 in parameters3:
    print(param3)
epsilon_w = parameters3[0] / parameters1[0]
print(epsilon_w)

print('Fit matt')
parameters4 = correlated_values(parameters4, pcov4)
for param4 in parameters4:
    print(param4)
epsilon_m = parameters4[0] / parameters1[0]
print(epsilon_m)

# Aktuelle Ausgabe
#Fit schwarz
#(1.047+/-0.007)e-10
#-0.836+/-0.010
#Fit glaenzend
#(7.3+/-0.5)e-12
#-0.062+/-0.006
#0.069+/-0.004
#Fit weiss
#(9.95+/-0.06)e-11
#-0.794+/-0.008
#0.951+/-0.009
#Fit matt
#(1.67+/-0.07)e-11
#-0.131+/-0.009
#0.159+/-0.006


#print('Fit schwarz')
#print(parameters1)
#print(pcov1)
#print('Fit glänzend')
#print(parameters2)
#print(pcov2)
#print('Fit weiß')
#print(parameters3)
#print(pcov3)
#print('Fit matt')
#print(parameters4)
#print(pcov4)
#Fit schwarz
#[  1.04688488e-10  -8.36232527e-01]
#[[  5.57523512e-25  -7.42087980e-15]
# [ -7.42087980e-15   1.02817826e-04]]
#Fit glänzend
#[  7.26261983e-12  -6.19519545e-02]
#[[  2.17557787e-25  -2.89578855e-15]
# [ -2.89578855e-15   4.01217504e-05]]
#Fit weiß
#[  9.95319028e-11  -7.93846147e-01]
#[[  3.40839518e-25  -4.53672187e-15]
# [ -4.53672187e-15   6.28572214e-05]]
#Fit matt
#[  1.66698453e-11  -1.31416208e-01]
#[[  4.23936518e-25  -5.64277894e-15]
# [ -5.64277894e-15   7.81818705e-05]]
