import numpy as np
pb1= 7.3+1
pb2= 9.4+1
pb3=11.0+1
pb4=12.5+1
pa1=2.1+1
pa2=2.1+1
pa3=2.2+1
pa4=2.2+1
T1=28.0+273.15
T2=36.9+273.15
T3=45.2+273.15
T4=-50.7+273.15
#pa=pa+1   #Kg/(ms²)
#pb=pb+1   #Kg/(ms²)
p=1       #Kg/(ms²)
T0=273.15 #K
k=1.14    #
k1=1/k
p0=1      #Kg/(ms²)
roh0=5.51 #g/l kg/m³
#druck
#5  2.1  	 7.3
#10  2.1  	 9.4
#15  2.2  	11.0
#19  2.2  	12.5
roh1=(pa1*roh0*T0/(T1*p0))
roh2=(pa2*roh0*T0/(T2*p0))
roh3=(pa3*roh0*T0/(T3*p0))
roh4=(pa4*roh0*T0/(T4*p0))
dmdt1=-1.394630925991996971e-02
dmdt2=-1.318260986553914521e-02
dmdt3=-1.241891047115831551e-02
dmdt4=-1.180795095565365452e-02
Nmech1=1/(k-1)*(pb1*(pa1/pb1)**k1-pa1)/roh1*dmdt1
Nmech2=1/(k-1)*(pb2*(pa2/pb2)**k1-pa2)/roh2*dmdt2
Nmech3=1/(k-1)*(pb3*(pa3/pb3)**k1-pa3)/roh3*dmdt3
Nmech4=1/(k-1)*(pb4*(pa4/pb4)**k1-pa4)/roh4*dmdt4

print (roh1)
print (roh2)
print (roh3)
print (roh4)
