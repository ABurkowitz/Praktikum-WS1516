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
#plt.plot(t, T1 , 'rx', label="Temperatur T1")
#plt.plot(t, T2 , 'bx', label="Temperatur T2")
parameters1, cov1 = curve_fit(f, t, T1)
parameters2, cov2 = curve_fit(g, t, T2)
fehler1= np.sqrt(np.diag(cov1))
fehler2= np.sqrt(np.diag(cov2))
#plt.plot(t, f(t, *parameters1), 'r-', label='Fit T1')
#plt.plot(t, f(t, *parameters2), 'b-', label='Fit T2')
#plt.xlabel(r'$Zeit / s$')
#plt.ylabel(r'$Tempratur / K$')
#plt.tight_layout()
#plt.legend(loc='best')
#plt.savefig('Temperaturgraphik.pdf')
paras1=unp.uarray(parameters1,fehler1)
paras2=unp.uarray(parameters2,fehler2)
np.savetxt('datenf/ausglkurve_T1.txt',unp.nominal_values(paras1), header="A,B,C")
np.savetxt('datenf/ausglkurve_T2.txt',unp.nominal_values(paras2), header="a,b,c")
np.savetxt('datenf/ausglkurve_T1f.txt',unp.std_devs(paras1) , header="fehler ABC")
np.savetxt('datenf/ausglkurve_T2f.txt',unp.std_devs(paras2) , header="fehler abc")
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

np.savetxt('datenf/gueteziffer_ref.txt',(unp.nominal_values(vr),unp.std_devs(vr)), header="Gueteziffer-re")
#print (vr)


#Verdampfungswärme///////////////////////////////////////////


p,T = np.genfromtxt('daten/Dampfdruckkurve_array.txt', unpack=True)
#R=8.314 4598 J mol-1 K-1
#+-0.000 0048 J mol-1 K-1
R=ufloat(8.3144598,0.0000048)
T=T+273.15
T=1/T
def h(m,T,C):
 return m * T + C

lnp=np.log(p)
plt.plot(T, lnp , 'rx', label="Temperatur T1")
parameters3, covL = curve_fit(h, T, lnp)

plt.plot(T, h(T, *parameters3), 'r-', label='Fit T1')
plt.xlabel(r'$\frac{1}{T}/\frac{1}{K}$')
plt.ylabel(r'$ln(\frac{p}{p_0})$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('daten/Dampfdruckkurve.pdf')
fehlerL= np.sqrt(np.diag(covL))
m= ufloat(parameters3[0],fehlerL[0])
np.savetxt('datenf/ausglkurve_pTf.txt',parameters3, header="m,T,C")
L=- m *R
#print (L)
np.savetxt('datenf/Verdampfungswaerme.txt', (unp.nominal_values(L),unp.std_devs(L)) , header="Verdampfungswaerme_L")
#print(fehlerL)
#print(parameters1)


#universelle (molare)Gaskonstante
#R=8.314 4598 J mol-1 K-1
#+-0.000 0048 J mol-1 K-1
#ln p = L/(R*T)+const
#R*T*ln(p)-R*T*const=L


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
m1cw=Dichte*3*Cp
#m1cw=12525.668459999999

#Wärmecapazität Kupferspirale Behälter?
mkck=660



Q2dt=(T2diffq  *( m1cw + mkck ))

np.savetxt('datenf/Q2dt.txt',(unp.nominal_values(Q2dt),unp.std_devs(Q2dt)), header="Q2dt")

#L= 23406.2040997 J/mol

dmdtm=-Q2dt/L
#print(dmdtm)
#print(L)
#molecularweight 18.0153
#Molare Masse of Cl2F2C is 120,9135 g/mol
mw=ufloat(120.9135,0)
dmdtg=dmdtm*mw
np.savetxt('datenf/Massendurchsatzm.txt',(unp.nominal_values(dmdtm),unp.std_devs(dmdtm)), header="dm/dt")
np.savetxt('datenf/Massendurchsatzg.txt',(unp.nominal_values(dmdtg),unp.std_devs(dmdtg)), header="dm/dt")


pb1=ufloat(8.3,0.1)
pb2=ufloat(10.4,0.1)
pb3=ufloat(12.0,0.1)
pb4=ufloat(13.5,0.1)
pa1=ufloat(3.1,0.1)
pa2=ufloat(3.1,0.1)
pa3=ufloat(3.2,0.1)
pa4=ufloat(3.2,0.1)



#pa=pa+1   #Kg/(ms²)
#pb=pb+1   #Kg/(ms²)
p=1       #Kg/(ms²)
T0=ufloat(273.15,0) #K
k=1.14    #
k1=ufloat(1/k,0)
p0=ufloat(1,0)      #Kg/(m²)
roh0=ufloat(5.51,0) #g/l kg/m³
#druck
#5  2.1  	 7.3
#10  2.1  	 9.4
#15  2.2  	11.0
#19  2.2  	12.5

roh1=(pa1*roh0*T0/(T1f[5]*p0))   #15.492861198738169
roh2=(pa2*roh0*T0/(T1f[10]*p0))   #15.048137880986937
roh3=(pa3*roh0*T0/(T1f[15]*p0))   #15.12857169781687
roh4=(pa4*roh0*T0/(T1f[19]*p0))   #21.65062171274444
#dmdt1=-1.394630925991996971e-02
#dmdt2=-1.318260986553914521e-02
#dmdt3=-1.241891047115831551e-02
#dmdt4=-1.180795095565365452e-02
np.savetxt('datenf/Dichte.txt',(unp.nominal_values(roh1),unp.std_devs(roh1),
unp.nominal_values(roh2),unp.std_devs(roh2),
unp.nominal_values(roh3),unp.std_devs(roh3),
unp.nominal_values(roh4),unp.std_devs(roh4)), header="N_mech")

Nmech1=1/(k-1)*(pb1*(pa1/pb1)**k1-pa1)/roh1*dmdtg[0]
Nmech2=1/(k-1)*(pb2*(pa2/pb2)**k1-pa2)/roh2*dmdtg[1]
Nmech3=1/(k-1)*(pb3*(pa3/pb3)**k1-pa3)/roh3*dmdtg[2]
Nmech4=1/(k-1)*(pb4*(pa4/pb4)**k1-pa4)/roh4*dmdtg[3]
print (roh1)
#print (dmdtm)
#print (dmdtg)
#print (Nmech1)
#print (Nmech2)
#print (Nmech3)
#print (Nmech4)
np.savetxt('datenf/Mech_Kompressorleistung.txt',(unp.nominal_values(Nmech1),unp.std_devs(Nmech1),
unp.nominal_values(Nmech2),unp.std_devs(Nmech2),
unp.nominal_values(Nmech3),unp.std_devs(Nmech3),
unp.nominal_values(Nmech4),unp.std_devs(Nmech4)), header="N_mech")
#15.492861198738169
#15.048137880986937
#15.12857169781687
#21.65062171274444

#-0.002562619075583121
#-0.003108734012963867
#-0.0033067864314812686
#-0.0024106078604203382
