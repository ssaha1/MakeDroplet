import numpy as np


def com(elv, xyz):
    cofm = np.dot(xyz.T, elv)
    return cofm / np.sum(elv)


def distancefromcom(xyz, cofm):
    dist = np.linalg.norm(xyz - cofm, axis=1)
    return dist


def distance(xyz):
    from scipy.spatial import distance_matrix
    dist = distance_matrix(xyz, xyz)
    print(dist.shape)


def gyratetotal(xyz, cofm, elv):
    distcom = xyz - cofm  # self.distancefromCom(xyz,com)
    rmat = np.sum(elv * np.power(distcom, 2)) / np.sum(elv)  # np.dot(np.power(distcom,2),elv)/np.sum(elv)
    return np.sqrt(rmat)


def gyratexyz(xyz, cofm, elv):
    distcom = xyz - cofm  # distance_matrix(xyz, com)
    distcomx = np.power((distcom[:, 1]), 2) + np.power((distcom[:, 2]), 2)
    distcomy = np.power((distcom[:, 0]), 2) + np.power((distcom[:, 2]), 2)
    distcomz = np.power((distcom[:, 1]), 2) + np.power((distcom[:, 0]), 2)
    gyr = np.zeros(3)
    gyr[0] = np.sqrt(np.sum(elv * distcomx) / np.sum(elv))
    gyr[1] = np.sqrt(np.sum(elv * distcomy) / np.sum(elv))
    gyr[2] = np.sqrt(np.sum(elv * distcomz) / np.sum(elv))
    return gyr
