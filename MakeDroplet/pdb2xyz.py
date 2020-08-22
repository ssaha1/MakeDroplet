#!/usr/bin/env python
import numpy as np

from MakeDroplet import GmxIO


def pdb2xyz(args):
    ifilename = args.infile
    df = GmxIO.readpdbpanda(ifilename)
    xyz = GmxIO.getxyzel(df)
    with open(args.dout, 'a') as outf:
        outf.write(str(xyz.shape[0]) + '\n protein\n')
        np.savetxt(outf, xyz, fmt='%s %.6f %.6f %.6f')


if __name__ == '__main__':
    '''
    Convert a .pdb structure file to a .xyz format.
    Initialize parser. The default help has poor labeling. See http://bugs.python.org/issue9694 
    '''
    from argparse import ArgumentParser

    #
    parser = ArgumentParser()
    parser.add_argument('-i', dest='infile', help='input data file', type=str)
    parser.add_argument('-o', dest='dout', help='Output .xyz file', type=str)
    parser.set_defaults(func=pdb2xyz)

    args = parser.parse_args()
    print(args)
    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        exit()
    args.func(args)
    pass
