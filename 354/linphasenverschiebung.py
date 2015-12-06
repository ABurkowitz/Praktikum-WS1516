import numpy as np
import matplotlib.pyplot as plt
#a: Abstand der Nulldurchgaenge
#f: Frequenz
f, Uc, a = np.genfromtxt('linmesswerte_phasenverschiebung.txt', unpack=True)
b=1/f
def phi(a,b):
    return (a/b)*2*np.pi

plt.plot(f,phi(a,b),'rx')
plt.savefig('linphasenverschiebung.pdf')
