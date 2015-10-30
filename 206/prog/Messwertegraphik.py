import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

t, T1 , T2 = np.genfromtxt('Temperatur_array.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15

plt.plot(t, T1 , 'rx', label="Temperatur1")
plt.plot(t, T2 , 'bx', label="Temperatur2")
plt.xlabel(r'$Zeit$')
plt.ylabel(r'$Tempratur()$')
plt.tight_layout()
plt.legend(loc='best')
plt.savefig('Temperaturgraphik.pdf')
