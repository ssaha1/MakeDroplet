from unittest import TestCase
from MakeDroplet import GmxTool

import numpy as np


class TestGmxTool(TestCase):
    def test_distancefrom_com(self):
        data = np.array([[52.18, 60.14, 103.56]])
        com = np.array([[55.57834289, 55.64878043, 55.80385546]])
        result = np.around(GmxTool.distancefromcom(data, com), 6)
        self.assertEqual(result[0], 48.087099)
