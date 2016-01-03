import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
L=ufloat(0.023954,0.000001)
C=ufloat(0.0000000007932,0.0000000000001)
Csp=ufloat(0.000000000028,0.000000000001)
C1=C+Csp
Ck1=ufloat(0.0000000120,0.0000000024)
Ck2=ufloat(0.0000000100,0.0000000020)
Ck3=ufloat(0.0000000082,0.00000000164)
Ck4=ufloat(0.0000000068,0.00000000136)
Ck5=ufloat(0.0000000047,0.00000000094)
Ck6=ufloat(0.0000000027,0.00000000054)
Ck7=ufloat(0.0000000022,0.00000000044)
Ck8=ufloat(0.0000000010,0.0000000002)
vp=1/(2*np.pi*unp.sqrt(L*C1))
print('v+')
print(vp)
vm1=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck1)))
vm2=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck2)))
vm3=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck3)))
vm4=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck4)))
vm5=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck5)))
vm6=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck6)))
vm7=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck7)))
vm8=1/(2*np.pi*unp.sqrt(L/(1/C1+2/Ck8)))
print('v- 1-8')
print(vm1)
print(vm2)
print(vm3)
print(vm4)
print(vm5)
print(vm6)
print(vm7)
print(vm8)
#subtrahiert
vdiff1=vm1-vp
vdiff2=vm2-vp
vdiff3=vm3-vp
vdiff4=vm4-vp
vdiff5=vm5-vp
vdiff6=vm6-vp
vdiff7=vm7-vp
vdiff8=vm8-vp
#addiert
vadd1=vm1+vp
vadd2=vm2+vp
vadd3=vm3+vp
vadd4=vm4+vp
vadd5=vm5+vp
vadd6=vm6+vp
vadd7=vm7+vp
vadd8=vm8+vp
#verhältnisse
ver1=vadd1/(2*vdiff1)
ver2=vadd2/(2*vdiff2)
ver3=vadd3/(2*vdiff3)
ver4=vadd4/(2*vdiff4)
ver5=vadd5/(2*vdiff5)
ver6=vadd6/(2*vdiff6)
ver7=vadd7/(2*vdiff7)
ver8=vadd8/(2*vdiff8)
print('Verhältnis v++v-/v--v+')
print(ver1)
print(ver2)
print(ver3)
print(ver4)
print(ver5)
print(ver6)
print(ver7)
print(ver8)
#frequenzen mit methode aus c
fa=ufloat(9.690,0.001)
fe=ufloat(111600,100)
fd=fe-fa
dt18=ufloat(0.296,0.001)
dt17=ufloat(0.304,0.001)
dt16=ufloat(0.300,0.001)
dt15=ufloat(0.300,0.001)
dt14=ufloat(0.296,0.001)
dt13=ufloat(0.298,0.001)
dt12=ufloat(0.300,0.001)
dt11=ufloat(0.300,0.001)
f11=dt11*fd+fa
f12=dt12*fd+fa
f13=dt13*fd+fa
f14=dt14*fd+fa
f15=dt15*fd+fa
f16=dt16*fd+fa
f17=dt17*fd+fa
f18=dt18*fd+fa
dt28=ufloat(0.720,0.001)
dt27=ufloat(0.540,0.001)
dt26=ufloat(0.508,0.001)
dt25=ufloat(0.432,0.001)
dt24=ufloat(0.394,0.001)
dt23=ufloat(0.382,0.001)
dt22=ufloat(0.366,0.001)
dt21=ufloat(0.354,0.001)
f21=dt21*fd+fa
f22=dt22*fd+fa
f23=dt23*fd+fa
f24=dt24*fd+fa
f25=dt25*fd+fa
f26=dt26*fd+fa
f27=dt27*fd+fa
f28=dt28*fd+fa
print('c v+')
print(f11)
print(f12)
print(f13)
print(f14)
print(f15)
print(f16)
print(f17)
print(f18)
print('c v-')
print(f21)
print(f22)
print(f23)
print(f24)
print(f25)
print(f26)
print(f27)
print(f28)

abw11=(35884-33490)/35884
abw12=(35884-33490)/35884
abw13=(35884-33260)/35884
abw14=(35884-33040)/35884
abw15=(35884-33490)/35884
abw16=(35884-33490)/35884
abw17=(35884-33930)/35884
abw18=(35884-33040)/35884

abw21=(38300-39510)/38300
abw22=(38700-40850)/38700
abw23=(39300-42640)/39300
abw24=(40000-43980)/40000
abw25=(41700-48220)/41700
abw26=(45500-56700)/45500
abw27=(47400-60270)/47400
abw28=(58000-80350)/58000
print('abweichungv+')
print(abw11)
print(abw12)
print(abw13)
print(abw14)
print(abw15)
print(abw16)
print(abw17)
print(abw18)
print('abweichungv-')
print(abw21)
print(abw22)
print(abw23)
print(abw24)
print(abw25)
print(abw26)
print(abw27)
print(abw28)
#vdiff1=-36.51+38.85
#vdiff2=-36.51+39.30
#vdiff3=-36.51+39.89
#vdiff4=-36.51+40.55
#vdiff5=-36.51+42.23
#vdiff6=-36.51+46.00
#vdiff7=-36.51+47.90
#vdiff8=-36.51+58.72
#
#vadd1=36.51+38.85
#vadd2=36.51+39.30
#vadd3=36.51+39.89
#vadd4=36.51+40.55
#vadd5=36.51+42.23
#vadd6=36.51+46.00
#vadd7=36.51+47.90
#vadd8=36.51+58.72
#
#ver1=vadd1/vdiff1
#ver2=vadd2/vdiff2
#ver3=vadd3/vdiff3
#ver4=vadd4/vdiff4
#ver5=vadd5/vdiff5
#ver6=vadd6/vdiff6
#ver7=vadd7/vdiff7
#ver8=vadd8/vdiff8
#print('Verhältnis v++v-/v--v+')
#print(ver1)
#print(ver2)
#print(ver3)
#print(ver4)
#print(ver5)
#print(ver6)
#print(ver7)
#print(ver8)
#
