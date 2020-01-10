import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestLISA(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("../data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        self.crm_prp = guerry.GetIntegerCol("Crm_prp")

    def test_local_moran(self):
        lisa = pygeoda.local_moran(self.queen_w, self.crm_prp)
        lms = lisa.GetLISAValues()
        self.assertEqual(lms[0], 0.015431978309803657)
        self.assertEqual(lms[1], 0.3270633223656033)
        self.assertEqual(lms[2], 0.3270633223656033)
        # todo

    def test_local_geary(self):
        lisa = pygeoda.local_geary(self.queen_w, self.crm_prp)
        lms = lisa.GetLISAValues()
        # todo