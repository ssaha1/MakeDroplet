from unittest import TestCase
from MakeDroplet import GmxTool
import numpy as np


class Test(TestCase):
    def test_com(self):
        data = np.array([[52.18, 60.14, 103.56]])
        mass = np.array([14.007])
        result = GmxTool.com(mass, data)
        self.assertEqual(result[0], 52.18)


    def test_distancefrom_com(self):
        data = np.array([[52.18, 60.14, 103.56]])
        com = np.array([[55.58, 55.65, 55.80]])
        result = np.around(GmxTool.distancefromcom(data, com), 6)
        self.assertEqual(result[0], 48.090932)


    def test_gyratetotal(self):
        data = np.array([[52.18, 60.14, 103.56]])
        com = np.array([[55.58, 55.65, 55.80]])
        mass = np.array([14.007])
        result = np.around(GmxTool.gyratetotal(data, com, mass), 6)
        self.assertEqual(result, 48.090932)
