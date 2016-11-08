import matplotlib.pyplot as plt
from matplotlib import colors
import random
import numpy as np
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
        args.inputfile = resource_filename('eventio', 'resources/1_proton_14.dat')

    with IACTFile(args.inputfile) as f:
        
        event = f[args.event]
        photons = event.photon_bunches[0]
        #photons = np.random.choice(photons,500000)

        circle1 = plt.Circle((0, 0), 27.485, color='r',fill=False)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.add_patch(circle1)

        a = photons['x']
        b = photons['y']
        k = 0
        i = photons.size

        x=list()
        y=list()

        while k<i:
            c = a[k]**2 + b[k]**2 
            if c <= 27.485**2:
                #print(a[k],b[k])
                #print(np.sqrt(c))
                x.append(a[k])
                y.append(b[k])
            k=k+1
        #print(x)
        #print(y)
        plt.xlim(-27.485,27.485)
        plt.ylim(-27.485,27.485)

        color_map = plt.get_cmap('gray')

        plt.hist2d(x,y,bins=100,normed=True,cmap=color_map)
        plt.colorbar()
        plt.show()

        targets = np.column_stack([x,y])
        print(targets)
        print()


        np.random.shuffle(targets)
        print(targets)


        #Gesamtplot:
        #color_map = plt.get_cmap('gray')

        #plt.hist2d(photons['x'],photons['y'],bins=100,normed=True,cmap=color_map)
        #plt.colorbar()
        #plt.show()

if __name__ == '__main__':
    main()
