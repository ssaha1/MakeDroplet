import numpy as np


def com(elv, xyz):
    '''
    Define centre of mass of the protein
    :param elv: Atomic mass
    :type elv:float
    :param xyz: coordinate of each atom
    :type xyz: numpy array
    :return: Centre of mass
    :rtype: numpy array
    '''
    cofm = np.dot(xyz.T, elv)
    return cofm / np.sum(elv)


def distancefromcom(xyz, cofm):
    '''
    Distance from the centre of mass
    :param xyz: coordinate of each atom
    :type xyz: numpy array
    :param cofm: centre of mass
    :type cofm: numpy array
    :return: distance
    :rtype: float, numpy array
    '''
    dist = np.linalg.norm(xyz - cofm, axis=1)
    return dist


def distance(xyz):
    from scipy.spatial import distance_matrix
    dist = distance_matrix(xyz, xyz)
    print(dist.shape)


def gyratetotal(xyz, cofm, elv):
    '''
    Radius of gyration
    :param xyz: coordinate of each atom
    :type xyz: numpy array
    :param cofm: centre of mass
    :type cofm: numpy array
    :param elv: atomic mass
    :type elv: numpy array
    :return: radius of gyration
    :rtype: float
    '''
    distcom = xyz - cofm  # self.distancefromCom(xyz,com)
    rmat = np.sum(elv * np.power(distcom, 2)) / np.sum(elv)  # np.dot(np.power(distcom,2),elv)/np.sum(elv)
    return np.sqrt(rmat)


def gyratexyz(xyz, cofm, elv):
    '''
    XYZ components of radius of gyration
    :param xyz: coordinate of each atom
    :type xyz: numpy array
    :param cofm: centre of mass
    :type cofm: numpy array
    :param elv: atomic mass
    :type elv: numpy array
    :return: xyz components of radius of gyration
    :rtype: numpy array
    '''
    distcom = xyz - cofm  # distance_matrix(xyz, com)
    distcomx = np.power((distcom[:, 1]), 2) + np.power((distcom[:, 2]), 2)
    distcomy = np.power((distcom[:, 0]), 2) + np.power((distcom[:, 2]), 2)
    distcomz = np.power((distcom[:, 1]), 2) + np.power((distcom[:, 0]), 2)
    gyr = np.zeros(3)
    gyr[0] = np.sqrt(np.sum(elv * distcomx) / np.sum(elv))
    gyr[1] = np.sqrt(np.sum(elv * distcomy) / np.sum(elv))
    gyr[2] = np.sqrt(np.sum(elv * distcomz) / np.sum(elv))
    return gyr
