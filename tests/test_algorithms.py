import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("../data/Guerry.shp")
        self.queen_w = pygeoda.weights.queen(self.guerry)
        self.crm_prp = guerry.GetIntegerCol("Crm_prp")
        select_vars = ["Crm_prs", "Crm_prp", "Litercy", "Donatns", "Infants", "Suicids"]
        self.data = [self.guerry.GetRealCol(v) for v in select_vars]

    def test_PCA(self):
        pass
        #result = pygeoda.pca(self.data)

        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_STRCASEEQ(result->getMethod().c_str(), "svd");
        EXPECT_THAT(result->getStandardDev(),
                ElementsAre(1.46303403, 1.09581947, 1.04978454, 0.816680014, 0.740725815, 0.583970726));
        EXPECT_THAT(result->getPropOfVar(),
                    ElementsAre(0.356744826, 0.200136751, 0.183674619, 0.111161061, 0.0914457887, 0.0568369664));
        EXPECT_THAT(result->getCumProp(),
                    ElementsAre(0.356744826, 0.556881547, 0.74055618, 0.851717234, 0.943163037, 1.000000));
        EXPECT_FLOAT_EQ(result->getKaiser(), 3.0);
        EXPECT_FLOAT_EQ(result->getThresh95(), 5.0);
        EXPECT_THAT(result->getEigenValues(),
                    ElementsAre(2.1404686, 1.20082033, 1.10204756, 0.666966259, 0.548674762, 0.341021806));
        """