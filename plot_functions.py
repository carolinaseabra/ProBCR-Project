import numpy
import matplotlib.pyplot as plt


def sigma(x):
    return 1 / (1 + numpy.exp(-x))

def tanh(x):
    return numpy.tanh(x)


plt.figure(figsize=(20, 3))
X = numpy.linspace(-5, 5, 100)
Y = numpy.linspace(-numpy.pi, numpy.pi, 12)

plt.subplot(131)
plt.plot(X, sigma(X), 'b')
plt.ylabel('$\phi(z)$')
plt.xlabel('z')
plt.title('Sigmoid Function')
#plt.grid(color='k', linewidth=0.1)
plt.text(1, 0.5, r'$\phi(z)=\frac{1}{1+e^{-z}}$', fontsize=12)

plt.subplot(132)
plt.plot(Y, sigma(Y), 'r')
plt.ylabel('$\phi(z)$')
plt.xlabel('z')
plt.title('Tanh Function')
#plt.grid(color='k', linewidth=0.1)
plt.text(1, 0.5, r'$\phi(z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}}$', fontsize=12)

plt.show()