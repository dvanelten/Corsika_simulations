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
        #photons = np.random.choice(photons,500000,replace=False)

        circle1 = plt.Circle((0, 0), 27.485, color='r',fill=False)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.add_patch(circle1)

        r = np.sqrt(photons['x']**2 + photons['y']**2)
        mask = r < 27.485
        selected_photons = photons[mask]

        plt.xlim(-27.485,25.35)
        plt.ylim(-27.485,27.485)

        color_map = plt.get_cmap('gray')

        plt.hist2d(selected_photons['x'], selected_photons['y'],bins=100,normed=True,cmap=color_map)
        plt.colorbar()
        plt.show()

        np.random.shuffle(selected_photons)

        #Gesamtplot:
        #color_map = plt.get_cmap('gray')

        #plt.hist2d(photons['x'],photons['y'],bins=100,normed=True,cmap=color_map)
        #plt.colorbar()
        #plt.show()

if __name__ == '__main__':
    main()
