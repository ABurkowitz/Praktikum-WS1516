import numpy as np
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

Q2dt=np.array([0,0,0,0], float)
dmdt=np.array([0,0,0,0], float)

dTdt5, dTdt10, dTdt15, dTdt19  =np.genfromtxt('daten/Diffquo.txt',float,unpack=True)

Q2dt[0]=(dTdt5[1]  *( m1cw + mkck ))
Q2dt[1]=(dTdt10[1] *( m1cw + mkck ))
Q2dt[2]=(dTdt15[1] *( m1cw + mkck ))
Q2dt[3]=(dTdt19[1] *( m1cw + mkck ))
np.savetxt('daten/Q2dt.txt',Q2dt, header="Q2dt")

#L= 23406.2040997 J/mol
L= 23406.2040997
dmdt[0]=Q2dt[0]/L
dmdt[1]=Q2dt[1]/L
dmdt[2]=Q2dt[2]/L
dmdt[3]=Q2dt[3]/L
np.savetxt('daten/Massendurchsatz.txt',dmdt, header="dm/dt")
