from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

#Messung von Rx=Wert 11
#x1=ufloat(494.7683109,2.43841555)
#x2=ufloat(500,2.5)
#x3=ufloat(479.9092496,2.399546248)
#491.6+/-1.4

#Messung von Rx=Wert 14
#x1=ufloat(904.7619047619,4.5238095238)
#x2=ufloat(924.4897959184,4.6224489796)
#x3=ufloat(878.4586288416,4.3922931442)
#902.6+/-2.6

#Messung von Cx = Wert 1
#x1=ufloat(6.55651105651106e-007,3.27825552825553E-009)
#x2=ufloat(6.49346555323591e-007,3.24673277661795E-009)
#x3=ufloat(6.53107794361526e-007,3.26553897180763E-009)
#(6.527+/-0.019)e-07


#Messung von Cx = Wert 6
#x1=ufloat(3.49736842105263e-006,1.74868421052632E-008)
#x2=ufloat(0.000003492,1.74602054794521E-008)
#x3=ufloat(3.51709090909091e-006,1.75854545454545E-008)
#(3.502+/-0.010)e-06


#Messung von Cx,Rx = Wert 8 (verlustbehafteter Kondensator)
#Fehler: R2: 3.0%, R3/R4: 0.5%
#r2_1=ufloat(940,28.2)
#r3r4_1=ufloat(0.6366612111,3.183306056e-3)
#rx1=r2_1*r3r4_1
#x1=ufloat(rx1.n,rx1.s)
#r2_2=ufloat(910,27.3)
#r3r4_2=ufloat(0.64203612479,0.003210180623)
#rx2=r2_2*r3r4_2
#x2=ufloat(rx2.n,rx2.s)
#r2_3=ufloat(990,29.7)
#r3r4_3=ufloat(0.6025641,0.0030128205)
#rx3=r2_3*r3r4_3
#x3=ufloat(rx3.n,rx3.s)
#593.1+/-10.4
#x1=ufloat(7.0681233933162E-007,3.5340616966581E-009)
#x2=ufloat(9.29854219948849E-007,4.64927109974425E-009)
#x3=ufloat(1.64629787234043E-006,8.23148936170213E-009)
#(1.0943+/-0.0034)e-06

#Messung von Lx,Rx = Wert 19 (verlustbehaftete Spule)
#Fehler: R2, R3, R4: 3.0%
#r2_1=ufloat(66,1.98)
#r3r4_1=ufloat(1.84090909,0.0092045)
#rx1=r2_1*r3r4_1
#x1=ufloat(rx1.n,rx1.s)
#r2_2=ufloat(78,2.34)
#r3r4_2=ufloat(1.34741784037,0.006737089201)
#rx2=r2_2*r3r4_2
#x2=ufloat(rx2.n,rx2.s)
#113.3+/-2.4
#l2_1=ufloat(0.0146,0)
#r3r4_1=ufloat(1.84090909,0.0092045)
#rx1=l2_1*r3r4_1
#x1=ufloat(rx1.n,rx1.s)
#l2_2=ufloat(0.0201,0)
#r3r4_2=ufloat(1.34741784037,0.006737089201)
#rx2=l2_2*r3r4_2
#x2=ufloat(rx2.n,rx2.s)
#0.02698+/-0.00010

#Messung von Lx,Rx = Wert 19 (verlustbehaftete Spule) – Maxwell-Brücke -
#r2_1=ufloat(1000,30)
#r3_1=ufloat(69,2.07)
#r4_1=ufloat(640,19.2)
#rx1=r2_1*(r3_1/r4_1)
#x1=ufloat(rx1.n,rx1.s)
#print(x1)
#r2_2=ufloat(332,9.96)
#r3_2=ufloat(206,6.18)
#r4_2=ufloat(636,19.08)
#rx2=r2_2*(r3_2/r4_2)
#x2=ufloat(rx2.n,rx2.s)
#print(x2)
#r2_3=ufloat(664,19.92)
#r3_3=ufloat(104,3.12)
#r4_3=ufloat(639,19.17)
#rx3=r2_3*(r3_3/r4_3)
#x3=ufloat(rx3.n,rx3.s)
#print(x3)
#107.8+/-3.2

#r2_1=ufloat(1000,30)
#r3_1=ufloat(69,2.07)
#c4_1=ufloat(0.000000399,0)
#rx1=r2_1*r3_1*c4_1
#x1=ufloat(rx1.n,rx1.s)
#r2_2=ufloat(332,9.96)
#r3_2=ufloat(206,6.18)
#c4_2=ufloat(0.000000399,0)
#rx2=r2_2*r3_2*c4_2
#x2=ufloat(rx2.n,rx2.s)
#r2_3=ufloat(664,19.92)
#r3_3=ufloat(104,3.12)
#c4_3=ufloat(0.000000399,0)
#rx3=r2_3*r3_3*c4_3
#x3=ufloat(rx3.n,rx3.s)

#Wien-Robinson-Brücke
#Mittelwert Us
x1=ufloat(7.44,0.1116)
x2=ufloat(7.12,0.1068)
x3=ufloat(6.8,0.102)
x4=ufloat(6.4,0.096)

#x1=ufloat()
#x2=ufloat()
#x3=ufloat()
m=(1/4)*(x1+x2+x3+x4)

print(m)
