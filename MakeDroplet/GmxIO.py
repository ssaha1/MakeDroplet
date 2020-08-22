

import numpy as np
import pandas as pd


# import dask.dataframe as dd
# import swifter
# import time


def readpdbnp(filename):
    data = np.genfromtxt(filename, skip_header=5, skip_footer=2,
                         names='ATOM,index,atname,res,count,x,y,z,occ,temp,elname',
                         dtype=['S4', int, 'S3', 'S3', int, float, float, float, float, float, 'S2'])
    return data


def readpdbpanda(filename):
    try:
        print(filename)
        names = ['ATOM', 'index', 'atname', 'res', 'count', 'x', 'y', 'z', 'occ', 'temp', 'elname']
        dtype = dict(ATOM=str, index=int, atname=str, residue=str, count=int, x=float, y=float, z=float,
                     occ=float, temp=float, elname=str)

        col = [(0, 4), (5, 12), (12, 17), (17, 20), (22, 27), (28, 38), (39, 46), (47, 54), (55, 60), (61, 66),
               (75, 78)]
        df = pd.read_fwf(filename, header=4, skipfooter=2, colspecs=col, dtypes=dtype, names=names)  # ,names=names)
        return df
    # except:
    #     print('Cannot open file')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print("Unexpected error; Cannot open file")
        raise


def proteinpdb(df):
    protein = df[(df.res != 'SOL') & (df.elname != 'Na') & (df.elname != 'Cl')]
    # print(protein.tail())
    return protein


def waterpdb(df):
    water = df[(df.res == 'SOL') & (df.atname !='MW')]
    print(water.tail())
    return water


def getxyzel(df):
    df = df[df.atname !='MW']
    xyz = np.asmatrix(df[['elname', 'x', 'y', 'z']].values)
    return xyz


def getxyz(df):
    xyz = np.asmatrix(df[['x', 'y', 'z']].values)
    return xyz


def elementmass(df):
    mdict = {'H': 1.008, 'B': 10.81, 'C': 12.011, 'O': 15.999, 'N': 14.007, 'F': 18.998, 'Na': 22.990, 'S': 32.06,
             'Cl': 35.45}
    # print(df.dtypes)
    elmass = df['elname'].map(mdict)
    elv = elmass.values
    return elv
