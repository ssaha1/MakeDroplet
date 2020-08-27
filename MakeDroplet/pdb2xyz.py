#!/usr/bin/env python
import numpy as np

from MakeDroplet import GmxIO


def pdb2xyz(args):
    ifilename = args.infile
    df = GmxIO.readpdbpanda(ifilename)
    xyz = GmxIO.getxyzel(df)
    print(xyz)
    with open(args.dout, 'a') as outf:
        outf.write(str(xyz.shape[0]) + '\n protein\n')
        # xyz.to_string(outf, index=False, header=False)
        np.savetxt(outf, xyz, fmt='%s %.6f %.6f %.6f')


def pdb2xyzbatch(args):
    import glob
    from pathlib import Path
    ifilepattern = args.infile
    filelist = glob.glob('*'+ifilepattern)
    for i,ifile in enumerate(filelist):
        basename = Path(ifile).stem
        df = GmxIO.readpdbpanda(ifile)
        xyz = GmxIO.getxyzel(df)
        if args.dout is None:
            with open(basename + '.xyz', 'a') as outf:
                outf.write(str(xyz.shape[0]) + '\n protein\n')
                np.savetxt(outf, xyz, fmt='%s %.6f %.6f %.6f')
        else:
            with open(args.dout+str(i) + '.xyz', 'a') as outf:
                outf.write(str(xyz.shape[0]) + '\n protein\n')
                np.savetxt(outf, xyz, fmt='%s %.6f %.6f %.6f')


if __name__ == '__main__':
    '''
    Convert a .pdb structure file to a .xyz format.
    Initialize parser. The default help has poor labeling. See http://bugs.python.org/issue9694 
    '''
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Convert a .pdb file to .xyz')
    subparsers = parser.add_subparsers()
    parser_single = subparsers.add_parser("Single",
                                          help="Convert a single .pdb file to .xyz")
    #
    parser_single.add_argument('-i', dest='infile', help='input .pdb file', type=str)
    parser_single.add_argument('-o', dest='dout', help='Output .xyz file', type=str)
    parser_single.set_defaults(func=pdb2xyz)

    parser_batch = subparsers.add_parser("Batch",
                                         help="Convert a batch of .pdb file to .xyz")
    #
    parser_batch.add_argument('-i', dest='infile', help='input pattern for .pdb file', type=str)
    parser_batch.add_argument('-o', dest='dout', help='Output pattern for .xyz file', type=str)
    parser_batch.set_defaults(func=pdb2xyzbatch)

    args = parser.parse_args()
    print(args)
    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        exit()
    args.func(args)
    pass
