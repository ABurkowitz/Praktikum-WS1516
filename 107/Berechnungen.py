import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plot
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
#masse Kugel klein in g
m_kl=ufloat(4.4531,0.0001)
#abstand in m
x=ufloat(0.1,0.0001)
#Kg/m^-3 dichte wasser 274 geschke
rohf=ufloat(0.998,0.001)
#mPaccm³/g
K_kl=ufloat(0.07640,0.00001)
#Durchmesser der Kugeln
d1=unp.uarray([15.627,15.624,15.631,15.630,15.626,15.626,15.633,15.630,15.631,15.630],
              [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001])
d2=unp.uarray([15.795,15.794,15.792,15.799,15.793,15.798,15.799,15.798,15.797,15.802],
              [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001])
#zeiten
t1=unp.uarray([12.76,13.05,13.04,12.91,12.50,12.53,12.69,12.64,13.04,12.95],
              [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001])
t2=unp.uarray([87.33,87.03,88.39,88.36,88.01,88.32,88.07,88.43,88.03,88.23],
              [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001])
#Temperaturen
T1=unp.uarray([293.2,302.7,308.7,313.2,318.2,323.7,328.2,333.2,338.2,343.2],
             [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
#zeiten bei vershiedenen Temperaturen
t3=unp.uarray([88.03,68.90,61.18,56.80,51.56,47.29,43.90,40.61,37.66,35.49],
    [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
t4=unp.uarray([88.23,68.23,61.95,56.66,51.69,47.69,43.83,40.80,38.01,35.21],
    [0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])
#mittlere zeiten bei verschiedenen Temperaturen
tm_3=(t3+t4)/2

#Masse der Kugeln in g
m1=ufloat(4.45,0.01)
m2=ufloat(4.95,0.01)
#Mittlere Masse
dm_1=(d1[0]+d1[1]+d1[2]+d1[3]+d1[4]+d1[5]+d1[6]+d1[7]+d1[8]+d1[9])/10/1000
dm_2=(d2[0]+d2[1]+d2[2]+d2[3]+d2[4]+d2[5]+d2[6]+d2[7]+d2[8]+d2[9])/10/1000
print('durchmesser mittel in cm')
print(dm_1)
print(dm_2)
tm_1=(t1[0]+t1[1]+t1[2]+t1[3]+t1[4]+t1[5]+t1[6]+t1[7]+t1[8]+t1[9])/10
tm_2=(t2[0]+t2[1]+t2[2]+t2[3]+t2[4]+t2[5]+t2[6]+t2[7]+t2[8]+t2[9])/10
print('t mittel')
print(tm_1)
print(tm_2)
v1=x/tm_1
v2=x/tm_2
print('geschwindigkeit v')
print(v1)
print(v2)
#Dichte
roh1=m1/(4/3*np.pi*(dm_1/2)**3)/1000
roh2=m2/(4/3*np.pi*(dm_2/2)**3)/1000
print('roh in kg/m^3')
print(roh1)
print(roh2)
#Viskosität
eta=K_kl*(roh1-rohf*1000)*tm_1
print('eta')
print(eta)
K_gr=eta/(roh2-rohf*1000)/tm_2
print('K_groß')
print(K_gr)
#reynoldzahl: dichte_wasser*geschwindigkeit*radius_kugel/eta
Re1=rohf*1000*v1*dm_1*1000/eta
Re2=rohf*1000*v2*dm_2*1000/eta
print('Reynoldszahl')
print(Re1)
print(Re2)
eta_t=K_gr*(roh2-rohf*1000)*tm_3/1000
print('eta temperaturabhängig')
print(eta_t)


T1n=unp.nominal_values(T1)
#def f(T1n,a_0, a_1):
#    return (a_0* np.exp(a_1/T1n))
def f(T1n,a_0, a_1):
    return (np.log(a_0)+(a_1/T1n))
T1x=1/T1n
print(T1x)
params, covar = curve_fit(f,T1x,np.log(unp.nominal_values(eta_t)),p0=[0.0000046,1600])

#lneta=np.log(unp.nominal_values(eta_t))
x_plot1 = np.linspace(T1x[0],T1x[9], 1000)
plot.plot(x_plot1,f(x_plot1,*params), 'b-', label="Fit")
plot.plot(1/unp.nominal_values(T1),np.log(unp.nominal_values(eta_t)), 'rx', label="Messwerte")
plot.legend(loc='best')
plot.yscale('linear')
plot.xscale('linear')
#plot.xlabel('$\frac{1}{\si{\kelvin}}$')
plot.ylabel('$\log(\eta)$')
plot.savefig('Viskosität_temp.pdf')
#plot.show()
print(params)
fehler= np.sqrt(np.diag(covar))
print(fehler)
