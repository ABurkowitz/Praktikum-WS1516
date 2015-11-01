import numpy as np

t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt',float, unpack=True)

vi=np.array([0,0,0,0], float)
vi[0]=T1[5]/(T1[5]-T2[5])
vi[1]=T1[10]/(T1[10]-T2[10])
vi[2]=T1[15]/(T1[15]-T2[15])
vi[3]=T1[19]/(T1[19]-T2[19])
np.savetxt('daten/gueteziffer_id.txt',vi, header="Gueteziffer-id")


t, N =np.genfromtxt('daten/Leistung_array.txt',float,unpack=True)
vr=np.array([0,0,0,0], float)
m1cw=1
mkck=1
#∆Q1/∆t= (m1 cw + mk ck )∆ T 1/∆ t
vr[0]=((T1[5] -T1[0])/t[5]) *( m1cw + mkck )
vr[1]=((T1[10]-T1[0])/t[10])*( m1cw + mkck )
vr[2]=((T1[15]-T1[0])/t[15])*( m1cw + mkck )
vr[3]=((T1[19]-T1[0])/t[19])*( m1cw + mkck )

np.savetxt('daten/gueteziffer_re.txt',vr, header="Gueteziffer-re_vorläufig")
