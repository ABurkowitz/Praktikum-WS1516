import numpy as np
import matplotlib.pyplot as plt
#a: Abstand der Nulldurchgaenge
#f: Frequenz
f, Uc, a = np.genfromtxt('linmesswerte_phasenverschiebung.txt', unpack=True)
b=1/f
def phi(a,b):
    return (a/b)*2*np.pi
errX=0.1
errY=0.001
#plt.errorbar(f,uc,xerr=errX, yerr=errY,fmt='none')
plt.plot(f,phi(a,b),'r+')
plt.plot(f,phi(a,b),'r.')
plt.savefig('linphasenverschiebung.pdf')
