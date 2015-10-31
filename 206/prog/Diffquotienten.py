import numpy as np
Paras1= np.genfromtxt('daten/ausglkurve_T1.txt', unpack=True)
Paras2= np.genfromtxt('daten/ausglkurve_T2.txt', unpack=True)
A=Paras1[0]
B=Paras1[1]
C=Paras1[2]
a=Paras2[0]
b=Paras2[1]
c=Paras2[2]



T1diffq = np.array([5 ,10 ,15 ,19])
T2diffq = np.array([5 ,10 ,15 ,19])
T1diffq=2*A *T1diffq +B
T2diffq=2*a *T2diffq +b


np.savetxt( 'daten/Diffquo.txt' ,(T1diffq ,T2diffq),
header="diffquotienten fuer t (5,10,15,19) T1 (28.0 ,36.9 ,45.2 ,50.7) T2 (21.8 ,17.6 ,9.0 ,1.6 ,-1.0)")
