import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plot
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
f, uc , a = np.genfromtxt('lin_resonanzkurve.txt', unpack=True)

#L(10.11e-3,0.03e-3)
#C(2.098e-9,0.006e-9)
#R1(48.1,0.1)
#R2(509.5,0.5)
#Rap(3.3e3)

#plt.plot(f, uc , 'b.', label="Kondensatorspannung")
#
#plt.xlabel(r'$Frequenz / Hz$')
#plt.ylabel(r'$Spannung / V$')
#
#errX=0.1
#errY=0.001
#plt.errorbar(f,uc,xerr=errX, yerr=errY,fmt='none')
#plt.tight_layout()
#plt.legend(loc='best')
#plt.savefig('Resonanzkurve.pdf')

def f(nu,  a_0, a_1):
    return (1 / np.sqrt((1 - a_0 * nu ** 2) ** 2 + (nu ** 2) * a_1))

x, z, a = np.genfromtxt('messwerte_phasenverschiebung.txt', unpack=True)
x=x*2*np.pi
L=10.11e-3
#,0.03e-3)
C=2.098e-9
#,0.006e-9)
R1=48.1
#,0.1)
R2=509.5
#,0.5)
R2e=R2*1.5
Rap=3.3e3
print(x)
#print(y)
print(z)
#print(a)


params, covar = curve_fit(f,x,z,p0=[L*C,R2**2*C**2])

print(params)
x_plot = np.linspace(0, 60)
x_plot1 = np.linspace(300, 10000000, 10000)
plot.errorbar(x, z + (a / 10), xerr=None, yerr=(a / 10), fmt='rx', label="Kondensatorspannung")

#plot.xscale('log')
plot.xlabel(' $\omega \;in\; \mathrm{ kHz }$')
plot.ylabel('$U_c/U_0$')
plot.xlim(1.6e5, 2.5e5)

#plot.grid()
#plot.legend(loc='best')
plot.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plot.plot(x_plot, f(x_plot, *params), 'b-', linewidth=1)
plot.plot(x_plot1, f(x_plot1, *params), 'b-', label="Fit")
plot.legend(loc='best')
params1=(L*C,R2**2*C**2)
#plot.plot(x_plot1, f(x_plot1, *params1), 'b-', linewidth=1)
plot.savefig('Resonanzkurve.pdf')
plot.show()
