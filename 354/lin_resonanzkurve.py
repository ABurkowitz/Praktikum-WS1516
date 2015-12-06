import numpy as np
import scipy.optimize
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
f, uc , a = np.genfromtxt('lin_resonanzkurve.txt', unpack=True)

#L(10.11e-3,0.03e-3)
#C(2.098e-9,0.006e-9)
#R1(48.1,0.1)
#R2(509.5,0.5)
#Rap(3.3e3)

plt.plot(f, uc , 'bx', label="Kondensatorspannung")

plt.xlabel(r'$Frequenz / Hz$')
plt.ylabel(r'$Spannung / V$')

plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Resonanzkurve.pdf')
