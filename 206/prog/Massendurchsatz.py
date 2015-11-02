import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
p, T =np.genfromtxt('daten/Dampfdruckkurve_array.txt',float, unpack=True)
#universelle (molare)Gaskonstante
#R=8.314 4598 J mol-1 K-1
#+-0.000 0048 J mol-1 K-1
#ln p = L/(R*T)+const
#R*T*ln(p)-R*T*const=L
T=1/T
R=8.3144598
def f(A,T,B):
 return np.log(A) *T + B

#L=R*T*ln(p)
lnp= np.log(p)
plt.plot((T) , lnp , 'rx', label="Dampfdruckkurve")
parameter, pocv = curve_fit(f, T, lnp)
plt.plot((T), f((T), *parameter), 'r-', label='Fit ln(p)')
plt.xlabel(r'$Temperatur *K$')
plt.ylabel(r'$ln(p)/bar$')
plt.ylim(1,3)

#plt.yscale(np.log, nonposy= 'clip')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Verdampfungswaerme.pdf')
A=parameter[1]
L=-A*R
#np.savetxt('Verdampfungswaerme.txt',L, header="A,B,C")
print (L)



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

#Wärmecapazität wasser + Kupferspule?
mkck=660

Q2=np.array([0,0,0,0], float)
dm=np.array([0,0,0,0], float)

dTdt5, dTdt10, dTdt15, dTdt19  =np.genfromtxt('daten/Diffquo.txt',float,unpack=True)
Q2[0]=((dTdt5[1]  *( m1cw + mkck ))
Q2[1]=((dTdt10[1] *( m1cw + mkck ))
Q2[2]=((dTdt15[1] *( m1cw + mkck ))
Q2[3]=((dTdt19[1] *( m1cw + mkck ))
np.savetxt('daten/DeltaQ1.txt',vr, header="DeltaQ1")
dm[0]=Q2[0]*L
dm[1]=Q2[1]*L
dm[2]=Q2[2]*L
dm[3]=Q2[3]*L
np.savetxt('daten/Massendurchsatz.txt',dm, header="dm/dt")
