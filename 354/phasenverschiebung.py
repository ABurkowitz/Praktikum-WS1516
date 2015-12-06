import numpy as np
import matplotlib.pyplot as plt
#a: Abstand der Nulldurchgaenge
#f: Frequenz
f, Uc, a = np.genfromtxt('messwerte_phasenverschiebung.txt', unpack=True)
b=1/f
def phi(a,b):
    return (a/b)*2*np.pi
plt.xscale('log')
plt.plot(f,phi(a,b),'rx')
plt.savefig('phasenverschiebung.pdf')
print(phi(a,b))
#plt.savefig('phasenverschiebung.pdf')
print(1.50e-6/(1/10000)*2*np.pi)
  #0.
  #0.
  #0.
  #0.
  #0.09424777
  #0.19603538
  #0.24881414
  #0.42474333
  #0.41494156
  #0.47500881
  #0.5629734
  #0.64194048
  #0.64465481
  #0.72382295
  #0.69240702
  #0.72288047
  #0.7115079
  #0.75398224
  #0.8022371
  #0.89598222
  #1.02918575
  #1.22522113
  #1.12594681
  #1.28553971
  #1.47340695
  #1.62357508
  #1.69080517
  #1.87364586
  #1.80327418
  #1.99051311
  #2.18529185
  #2.19660158
  #2.25440689
  #2.56353961
  #2.63893783
  #2.89026524
  #3.01592895
  #3.0787608
  #3.01592895
  #2.76460154
