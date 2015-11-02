import numpy as np
t, pa, pb =np.genfromtxt('daten/Druck_array.txt', unpack=True)
pa=pa+1   #Kg/(ms²)
pb=pb+1   #Kg/(ms²)
p=1       #Kg/(ms²)
T0=273.15 #K
k=1.14    #
p0=1      #Kg/(ms²)
roh0=5.51 #g/l kg/m³
dmdt =np.genfromtxt('daten/Massendurchsatz.txt', unpack=True)
#t, T1 , T2 = np.genfromtxt('daten/Temperatur_array.txt',float, unpack=True)
#ideales gasgesetz
# pV=nRT
# pV/T=RT
#nR=const
#p0V0/T0=p1V1/T1
#roh*V=m
#p0m/(T0roh0)=p1m/(T1roh1) :/m
#mit pa=p1
#und roh=roh1
#daher gilt
#p0/(roh0T0)=pa(T1/roh)
#roh=paroh0T0/T1p0


#roh=np.array([0,0,0,0], float)
#
#roh_0=(pa*roh0*T0/(T1[5] *p0))
#roh_1=(pa*roh0*T0/(T1[10]*p0))
#roh_2=(pa*roh0*T0/(T1[15]*p0))
#roh_3=(pa*roh0*T0/(T1[19]*p0))
#roh[0]=roh_0
#roh[1]=roh_1
#roh[2]=roh_2
#roh[3]=roh_3
#Nmech=np.array([0,0,0,0], float)
#Nmech=1/(k-1)(pb*((pa/pb)**(1/k)) -pa)/roh*dmdt
#Nmech1=1/(k-1)(pb*((pa/pb)**(1/k)) -pa)/(pa*roh0*T0/(T1[5] *p0))*dmdt[0]
#Nmech2=1/(k-1)(pb*((pa/pb)**(1/k)) -pa)/(pa*roh0*T0/(T1[10]*p0))*dmdt[1]
#Nmech3=1/(k-1)(pb*((pa/pb)**(1/k)) -pa)/(pa*roh0*T0/(T1[15]*p0))*dmdt[2]
#Nmech4=1/(k-1)(pb*((pa/pb)**(1/k)) -pa)/(pa*roh0*T0/(T1[19]*p0))*dmdt[3]
#print (Nmech1)
#print (Nmech2)
#print (Nmech3)
#print (Nmech4)
#
#np.savetxt('daten/Kompressorleistung.txt',Nmech,header="Kompressorleistung")
