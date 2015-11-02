import numpy as np
k=1.14
t,pa, pb =np.genfromtxt('daten/Druck_array.txt',float, unpack=True)
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
roh=pa*roh0*T0/(T1*p0)

Nmech=1/(k-1)(pb((pa/pb)**k)-pa)/roh*dm
