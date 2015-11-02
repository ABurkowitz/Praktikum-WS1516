import numpy as np

t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt',float, unpack=True)
T1= T1+273.15
T2= T2+273.15

vi=np.array([0,0,0,0], float)
vi[0]=T1[5]/(T1[5]-T2[5])
vi[1]=T1[10]/(T1[10]-T2[10])
vi[2]=T1[15]/(T1[15]-T2[15])
vi[3]=T1[19]/(T1[19]-T2[19])
np.savetxt('daten/gueteziffer_id.txt',vi, header="Gueteziffer-id")


t, N =np.genfromtxt('daten/Leistung_array.txt',float,unpack=True)
vr=np.array([0,0,0,0], float)


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

#Wärmecapazität wasser + Kupferspule
mkck=660

#∆Q1/∆t= (m1 cw + mk ck )∆ T 1/∆ t
dTdt5, dTdt10, dTdt15, dTdt19  =np.genfromtxt('daten/Diffquo.txt',float,unpack=True)
#v_real=dQ1/dt/N= (m1 cw + mk ck )dT1/dt/N
vr[0]=((dTdt5[0]  *( m1cw + mkck ))/N[5])
vr[1]=((dTdt10[0] *( m1cw + mkck ))/N[10])
vr[2]=((dTdt15[0] *( m1cw + mkck ))/N[15])
vr[3]=((dTdt19[0] *( m1cw + mkck ))/N[19])

np.savetxt('daten/gueteziffer_re.txt',vr, header="Gueteziffer-re_vorlaeufig")
