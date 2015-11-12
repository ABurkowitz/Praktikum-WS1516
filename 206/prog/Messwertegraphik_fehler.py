import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat

t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt', unpack=True)
#min in sekunden
t= t*60
T1 = T1 + 273.15
T2 = T2 + 273.15
T1f=unp.uarray(T1,0.1)
T2f=unp.uarray(T2,0.1)

def f(t,A,B,C):
 return A * t **2 + B * t + C
def g(t,a,b,c):
 return a * t **2 + b * t +c
plt.plot(t, T1 , 'rx', label="Temperatur T1")
plt.plot(t, T2 , 'bx', label="Temperatur T2")
parameters1, cov1 = curve_fit(f, t, T1)
parameters2, cov2 = curve_fit(g, t, T2)
fehler1= np.sqrt(np.diag(cov1))
fehler2= np.sqrt(np.diag(cov2))
plt.plot(t, f(t, *parameters1), 'r-', label='Fit T1')
plt.plot(t, f(t, *parameters2), 'b-', label='Fit T2')
plt.xlabel(r'$Zeit / s$')
plt.ylabel(r'$Tempratur / K$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Temperaturgraphik.pdf')
np.savetxt('datenf/ausglkurve_T1.txt',parameters1 , header="A,B,C")
np.savetxt('datenf/ausglkurve_T2.txt',parameters2, header="a,b,c")
np.savetxt('datenf/ausglkurve_T1f.txt',fehler1 , header="fehler ABC")
np.savetxt('datenf/ausglkurve_T2f.txt',fehler2 , header="fehler abc")
paras1=unp.uarray(parameters1,fehler1)
paras2=unp.uarray(parameters2,fehler2)
#print (paras1)
#Diffquotienten////////////////////////////////////////////

Zeiten = np.array([5 ,10 ,15 ,19],float)

#dT/dt=2A*t+B
#t von min nach sekunden
T1diffq=2*paras1[0] *Zeiten*60 +paras1[1]
T2diffq=2*paras2[0] *Zeiten*60 +paras2[1]
#print (T1diffq)

np.savetxt( 'datenf/Diffquof1.txt' ,(unp.nominal_values(T1diffq),unp.std_devs(T1diffq)),
header='diffquotienten fuer t (5,10,15,19)')
np.savetxt( 'datenf/Diffquof2.txt' ,(unp.nominal_values(T2diffq),unp.std_devs(T2diffq)),
header='diffquotienten fuer t (5,10,15,19)')

#Güteziffer/////////////////////////////////////////////////////////

vi=unp.uarray(Zeiten,0)
vi[0]=T1f[5]/(T1f[5]-T2f[5])
vi[1]=T1f[10]/(T1f[10]-T2f[10])
vi[2]=T1f[15]/(T1f[15]-T2f[15])
vi[3]=T1f[19]/(T1f[19]-T2f[19])
np.savetxt('datenf/gueteziffer_idf.txt',(unp.nominal_values(vi),unp.std_devs(vi)), header="Gueteziffer-id")


t, No =np.genfromtxt('daten/Leistung_array.txt',float,unpack=True)
vr=unp.uarray(Zeiten,0)
N=unp.uarray(No,5)

#1.11.2015 23:48
#http://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI&Mask=7&Type=JANAFL&Table=on#JANAFL
#spezifische wärmecapazität Cp=75.38(J/mol*K)
#1.11.2015 23:48
#http://webbook.nist.gov/cgi/fluid.cgi?T=294.85&PLow=1&PHigh=2&PInc=&Appl
#et=on&Digits=5&ID=C7732185&Action=Load&Type=IsoTherm&TUnit=K&PUnit=bar&D
#Unit=mol%2Fl&HUnit=kJ%2Fmol&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm&RefState=DEF
#Dichte wasser 55.389mol/l (294.85 K,1Bar)

Dichte=55.389
Cp=75.38
#Wärmecapazität wasser
m1cw=ufloat(Dichte*3*Cp,0)
#m1cw=12525.668459999999

#Wärmecapazität wasser + Kupferspule
mkck= 660

#∆Q1/∆t= (m1 cw + mk ck )∆ T 1/∆ t

#v_real=dQ1/dt/N= (m1 cw + mk ck )dT1/dt/N
vr[0]=((T1diffq[0]  *( m1cw + mkck ))/N[5])
vr[1]=((T1diffq[1] *( m1cw + mkck ))/N[10])
vr[2]=((T1diffq[2] *( m1cw + mkck ))/N[15])
vr[3]=((T1diffq[3] *( m1cw + mkck ))/N[19])
print (vr)
np.savetxt('datenf/gueteziffer_ref.txt',(unp.nominal_values(vr),unp.std_devs(vr)), header="Gueteziffer-re")
#print (vr)

p,T = np.genfromtxt('daten/Dampfdruckkurve_array.txt', unpack=True)
#R=8.314 4598 J mol-1 K-1
R=8.3144598
T=T+273.15
T=1/T
def f(m,T,C):
 return m * T + C

lnp=np.log(p)
plt.plot(T, lnp , 'rx', label="Temperatur T1")
parameters1, pocv = curve_fit(f, T, lnp)

plt.plot(T, f(T, *parameters1), 'r-', label='Fit T1')

plt.xlabel(r'$\frac{1}{T}/\frac{1}{K}$')
plt.ylabel(r'$ln(\frac{p}{p_0})$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('daten/Dampfdruckkurve.pdf')

np.savetxt('daten/ausglkurve_pT.txt',parameters1, header="m,T,C")
m=parameters1[0]
L= - m *R
print (L)
#np.savetxt('daten/Verdampfungswaerme.txt', L , header="Verdampfungswaerme_L")
