import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestSpatialClustering(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("../data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]
        self.bound_vals = self.guerry.GetRealCol("Pop1831")
        self.min_bound = 3236.67 # 10% of Pop1831

    def test_SKATER(self):
        k = 4
        clusters = pygeoda.skater(k, self.queen_w, self.data)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertEqual(ratio, 0.3156446659311204)

    def test_REDCAP(self):
        k = 4
        clusters = pygeoda.redcap(k, sel.queen_w, self.data, "fullorder-completelinkage")
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertEqual(ratio, 0.1905641377254551)

    def test_REDCAP(self):
        method = "greedy"
        clusters = pygeoda.maxp(self.queen_w, self.data, self.bound_vals, self.min_bound, method)
        betweenss = pygeoda.between_sumofsquare(clusters, self.data)
        totalss = total_sumofsquare( self.data)
        ratio =  betweenss / totalss

        self.assertEqual(ratio, 0.507018079733202)