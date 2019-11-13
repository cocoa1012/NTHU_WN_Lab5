import numpy as np
import matplotlib.pyplot as plt


def ALOHA(G):
    return G * np.exp(-2*G)


def sALOHA(G):
    return G * np.exp(-G)


def nCSMA(G, a=0.5):
    return (G * np.exp(-a * G)) / (G * (1 + 2 * a) + np.exp(-a * G))


def nsCSMA(G, a=0.5):
    return (a * G * np.exp(-a * G)) / (1 - np.exp(-a * G) + a)


def oneCSMA(G, a=0.5):
    return (G * (1 + G + a*G*(1+G+a*G/2)) * np.exp(-G*(1+2*a)))/(G*(1+2*a)-(1-np.exp(-a*G))+(1+a*G)*np.exp(-G*(1+a)))


def onesCSMA(G, a=0.5):
    return (G*(1+a-np.exp(-a*G))*np.exp(-G*(1+a)))/((1+a)*(1-np.exp(-a*G))+a*np.exp(-G*(1+a)))


def showPerformance(G, p1, p2, p3, p4, p5, p6):
    plt.title('Result Analysis')
    plt.plot(G, p1, label='ALOHA')
    plt.plot(G, p2, label='sALOHA')
    plt.plot(G, p3, label='unslotted non-persistent')
    plt.plot(G, p4, label='slotted non-persistent')
    plt.plot(G, p5, label='unslotted one-persistent')
    plt.plot(G, p6, label='slotted one-persistent')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    G = np.array(range(0, 200,), "f") / 10
    tALOHA = ALOHA(G)
    tSALOHA = sALOHA(G)
    tnCSMA = nCSMA(G, 0.1)
    tnsCSMA = nsCSMA(G, 0.1)
    toneCSMA = oneCSMA(G, 0.1)
    tonesCSMA = onesCSMA(G, 0.1)

    showPerformance(G, tALOHA, tSALOHA, tnCSMA, tnsCSMA, toneCSMA, tonesCSMA)
