import matplotlib.pyplot as plt
import numpy as np
import random
from pkg_resources import resource_filename
from argparse import ArgumentParser
import eventio

from eventio import IACTFile

parser = ArgumentParser()
parser.add_argument('-i', '--inputfile', dest='inputfile')
parser.add_argument('-e', '--event', dest='event', type=int, default=0)

def main():
    args = parser.parse_args()
    if not args.inputfile:
        args.inputfile = resource_filename('eventio', 'resources/1_gamma_1.dat')

    with IACTFile(args.inputfile) as f:
        
        event = f[args.event]
        photons = event.photon_bunches[0]
        photons = np.random.choice(photons,500000)


        circle1 = plt.Circle((0, 0), 27.485, color='r',fill=False)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.add_patch(circle1)

        a = photons['x']
        b = photons['y']
        k = 0
        n = photons.size

        x= list()
        y= list()

        while k<n:
            r_quad = a[k]**2 + b[k]**2 
            if r_quad <= 27.485**2:
                #print(a[k],b[k])
                #print(np.sqrt(r_quad))
                x.append(a[k])
                y.append(b[k])
            k=k+1
        #print(x)
        #print(y)
        plt.xlim(-27.485,27.485)
        plt.ylim(-27.485,27.485)
        plt.plot(x,y,marker='o',color='black',lw=0, linestyle="",alpha=0.1)
        plt.show()

        targets = np.column_stack([x,y])
        print(targets)
        print()


        np.random.shuffle(targets)
        print(targets)


        #Gesamtplot: (Zeile 22 einkommentieren)
        #plt.plot(photons['x'],photons['y'],marker=',',lw=0, linestyle="",alpha=0.1)
        #plt.show()

if __name__ == '__main__':
    main()
