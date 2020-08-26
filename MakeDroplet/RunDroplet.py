#!/usr/bin/env python
from MakeDroplet import GmxIO
from MakeDroplet import GmxTool
# import GmxIO
# import GmxTool
import numpy as np
import pandas as pd


class RunDroplet:
    def findwaterinsphere(self, com, waterdf, layer):
        '''
        Find coordinates of water molecule within a specific radius
        :param com: Center of mass of the protein
        :type com: numpy array
        :param waterdf: Dataframe containing the coordination of water molecules
        :type waterdf: Pandas Dataframe
        :param layer: Thickness of the water layer surrounding the protein
        :type layer: float
        :return: Coordinates of water molecules within the layer
        :rtype: numpy array
        '''
        watershell = []  # np.empty((1, 3))
        xyz = GmxIO.getxyz(waterdf)
        xyzel = GmxIO.getxyzel(waterdf)
        # print(xyz.shape)
        # print(xyz[1, 0:3])
        # print(com)
        # print(self.distancefromCom(xyz,com))
        for i in range(xyz.shape[0]):
            dist = GmxTool.distancefromcom(xyz[i, :], com)
            if dist < layer:
                watershell.append(xyzel[i, :])
            else:
                pass
                # print(xyz[i,:])
        coord = np.squeeze(np.asarray(watershell), axis=(1,))
        return coord  # np.stack((elname,coord),axis=1)

    def getradius(self, row):
        return np.sqrt(row['x'] ** 2 + row['y'] ** 2 + row['z'] ** 2)

    # noinspection PyShadowingNames
    def getwaterspherepanda(self, df, com, layer):
        pd.options.mode.chained_assignment = None  # default='warn'
        # print(df[df.count==[2712]])
        # import multiprocessing
        print('getting water inside the sphere')
        # df['distFromCom'] = df.apply(lambda row: droplet.distancefromCom([row['x'], row['y'], row['z']], com),
        #                                      axis=1)
        # start_time = time.time()
        df['distFromCom'] = df.apply(lambda row: GmxTool.distancefromcom([row.x, row.y, row.z], com),
                                     axis=1)
        # print("--- %s seconds ---" % (time.time() - start_time))
        watercutdf = df.query('distFromCom < @layer & atname=="OW"')
        watercutidx=watercutdf['count']
        water=df.loc[df['count'].isin(watercutidx)]
        # print(water)
        return water.drop(columns='distFromCom')
        # return water.style.set_properties(**{'text-align': 'right'})


    def writepdb(self, protein, watershell, outfile):
        '''
        :param protein: DataFrame containing structure and coordination data of the protein
        :param watershell: Thickness of the water layer surrounding the protein
        :param outfile: Name of the output file where protein and water data in PDB format is written
        :type outfile: PDB
        :return: None
        :rtype:
        '''
        # import functools
        header = "REMARK    GENERATED BY TRJCONV\nTITLE     Protein in water\n"\
                 "REMARK    THIS IS A SIMULATION BOX\n"\
                 "CRYST1  111.219  111.219  111.219  90.00  90.00  90.00 P 1           1\n"\
                 "MODEL        1\n"
        footer = "\nTER\nENDMDL"
        #
        #
        #
        # dtypec = dict(ATOM=str, index=int, atname=str, residue=str, count=int, x=float, y=float, z=float,
        #              occ=float, temp=float, elname=str)
        #
        # FLOAT_COLUMNS=('x','y','z','occ','temp')
        # INT_COLUMNS=('index')
        # def left_justified2(df,f):
        #     formatters = {}
        #
        #     # Pass a custom pattern to format(), based on
        #     # type of data
        #     for li in list(df.columns):
        #         if li in FLOAT_COLUMNS:
        #             form = "{{!s:<10}}".format()
        #         elif li in INT_COLUMNS:
        #             form = "{{!s:<8}}".format()
        #         else:
        #             max = df[li].str.len().max()
        #             form = "{{:<{}s}}".format(max)
        #         formatters[li] = functools.partial(str.format, form)
        #     return df.to_string(f,formatters=formatters, index=False,header=False)
        #
        # protein.iloc[:, 0] = (lambda s: s.str.ljust(s.str.len().max()))(protein.iloc[:, 0])
        # watershell.iloc[:, 0] = (lambda s: s.str.ljust(s.str.len().max()))(watershell.iloc[:, 0])
        # protein = protein.stack().str.lstrip().unstack()
        # watershell = watershell.stack().str.lstrip().unstack()
        # # protein.style.set_properties(**{'text-align': 'right'})
        # # protein['ATOM'] = protein['ATOM'].str.lstrip()
        # print(protein['ATOM'].dtype)
        # # watershell['ATOM'] = watershell['ATOM'].str.lstrip()
        # formatters = {}
        # # for li in list(protein.columns):
        # #     max = protein[li].str.len().max()
        # #     form = "{{:<{}s}}".format(max)
        # #     formatters[li] = functools.partial(str.format, form)
        # max = protein['ATOM'].str.len().max()
        # form = "{{:<{}s}}".format(max-1)
        # formatters['ATOM'] = functools.partial(str.format, form)

        # sp=protein.values.tolist()
        # wp=watershell.values.tolist()
        with open(outfile, 'a') as f:
            f.write(header,)
            # left_justified2(protein,f)
            # dtypec = dict(ATOM=str, index=int, atname=str, residue=str, count=int, x=float, y=float, z=float,
            #              occ=float, temp=float, elname=str)
            protein.to_string(f, index=False, header=False, col_space=[4, 4, 5, 5, 5, 8, 8, 8, 6, 6, 2])
            # np.savetxt(f,protein.values,fmt=['%s', '%4d', '%5s', '%5s', '%5d', '%8.2f', '%8.2f', '%8.2f', '%6.2f', '%6.2f', '%2d'])
            # f.write(proteintxt,)
            # towrite='\n'.join(sp)
            # f.write(towrite)
            f.write('\n')
            # towritew='\n'.join(wp)
            # f.write(wp)
            # left_justified2(watershell,f)
            watershell.to_string(f,header=False,  index=False, col_space=[4, 4, 5, 5, 5, 8, 8, 8, 6, 6, 2])
            # np.savetxt(f,watershell.values,fmt=['%4s', '%4d', '%5s', '%5s', '%5d', '%8.2f', '%8.2f', '%8.2f', '%6.2f', '%6.2f', '%2d'])
            # f.write(watertxt,)
            f.write(footer,)
            f.close()

    def makepdb(self, args):
        print('Making pdb file')
        ifilename = args.infile
        df = GmxIO.readpdbpanda(ifilename)
        dfp = GmxIO.proteinpdb(df)
        dfw = GmxIO.waterpdb(df)
        xyz = GmxIO.getxyz(dfp)
        elv = GmxIO.elementmass(dfp)
        com = GmxTool.com(elv, xyz)
        gyrT = GmxTool.gyratetotal(xyz, com, elv)
        layer = gyrT + args.shell
        print('layer: ', layer)
        watershell = self.getwaterspherepanda(dfw, com, layer)
        self.writepdb(dfp, watershell, args.dout)

    def makexyz(self, args):  # dfp,dfw,shell,outfile):
        ifilename = args.infile
        df = GmxIO.readpdbpanda(ifilename)
        dfp = GmxIO.proteinpdb(df)
        # dfp.style.set_properties(**{'text-align': 'right'})
        dfw = GmxIO.waterpdb(df)
        xyz = GmxIO.getxyz(dfp)
        elv = GmxIO.elementmass(dfp)
        com = GmxTool.com(elv, xyz)
        gyrt = GmxTool.gyratetotal(xyz, com, elv)
        layer = gyrt + args.shell

        watershellxyz = self.findwaterinsphere(com, dfw, layer)
        proteinxyz = GmxIO.getxyzel(dfp)
        print(proteinxyz.shape)
        print(watershellxyz.shape)
        proteinindroplet = np.concatenate((proteinxyz, watershellxyz), axis=0)

        with open(args.dout, 'a') as outf:
            outf.write(str(proteinindroplet.shape[0]) + '\n protein\n')
            np.savetxt(outf, proteinindroplet, fmt='%s %.6f %.6f %.6f')

    def pdb2xyz(self, args):
        ifilename = args.infile
        df = GmxIO.readpdbpanda(ifilename)
        xyz = GmxIO.getxyzel(df)
        with open(args.dout, 'a') as outf:
            outf.write(str(xyz.shape[0]) + '\n protein\n')
            np.savetxt(outf, xyz, fmt='%s %.6f %.6f %.6f')


if __name__ == '__main__':
    '''
    Create droplet from bulk structure.
    Initialize parser. The default help has poor labeling. See http://bugs.python.org/issue9694 
    '''
    droplet = RunDroplet()
    from argparse import ArgumentParser

    #
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_XYZ = subparsers.add_parser("XYZ",
                                       help="Make an XYZ structure of protein surrounded \
                                       by a water shell of given thickness")
    parser_XYZ.add_argument('-i', dest='infile', help='input data file', type=str)
    parser_XYZ.add_argument('-o', dest='dout', help='Output .xyz file', type=str)
    parser_XYZ.add_argument('-s', dest='shell', help='Thickness of the water layer surrounding the protein', type=float)
    parser_XYZ.set_defaults(func=droplet.makexyz)

    parser_PDB = subparsers.add_parser("PDB",
                                       help="Make an PDB file with structure of protein \
                                       surrounded by a water shell of given thickness")
    parser_PDB.add_argument('-i', dest='infile', help='input data file', type=str)
    parser_PDB.add_argument('-o', dest='dout', help='Output .pdb file', type=str)
    parser_PDB.add_argument('-s', dest='shell', help='Thickness of the water layer surrounding the protein', type=float)
    parser_PDB.set_defaults(func=droplet.makepdb)
    args = parser.parse_args()
    print(args)
    try:
        getattr(args, "func")
    except AttributeError:
        parser.print_help()
        exit()
    args.func(args)
    pass
