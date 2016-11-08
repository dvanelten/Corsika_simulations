import matplotlib.pyplot as plt
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
        photons = np.random.choice(photons,500000)

        plt.plot(photons['x'],photons['y'],marker=',',lw=0, linestyle="",alpha=0.1)
        plt.show()

if __name__ == '__main__':
    main()
