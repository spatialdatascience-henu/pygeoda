import unittest
import pygeoda

__author__ = "Xun Li <lixun910@gmail.com>, "

class TestWeights(unittest.TestCase):
    def setUp(self):
        self.guerry = pygeoda.open("../data/Guerry.shp")
        self.nat = pygeoda.open("../data/natregimes.shp")

    def test_queen_weights(self):
        w = pygeoda.weights.queen(self.guerry)

        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_THAT(w->num_obs, 3085);
        EXPECT_THAT(w->GetMinNumNbrs(), 1);
        EXPECT_THAT(w->GetMaxNumNbrs(), 14);
        EXPECT_TRUE(w->is_symmetric);
        EXPECT_DOUBLE_EQ(w->GetSparsity(), 0);
        EXPECT_DOUBLE_EQ(w->GetDensity(), 0.19089598070866245);
        EXPECT_DOUBLE_EQ(w->GetMeanNumNbrs(), 5.8891410048622364);
        """

        self.assertEqual(w.num_obs, 3085)

    def test_rook_weights(self):
        w = pygeoda.weights.rook(self.guerry)
        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_THAT(w->num_obs, 3085);
        EXPECT_THAT(w->GetMinNumNbrs(), 1);
        EXPECT_THAT(w->GetMaxNumNbrs(), 13);
        EXPECT_TRUE(w->is_symmetric);
        EXPECT_DOUBLE_EQ(w->GetSparsity(), 0);
        EXPECT_DOUBLE_EQ(w->GetDensity(), 0.18059886153789576);
        EXPECT_DOUBLE_EQ(w->GetMeanNumNbrs(), 5.571474878444084);
        """

    def test_knn_weights(self):
        k = 4
        w = pygeoda.weights.knn(self.guerry, k)
        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_FALSE(w->is_symmetric);
        EXPECT_THAT(w->num_obs, 3085);
        EXPECT_THAT(w->GetMinNumNbrs(), 4);
        EXPECT_THAT(w->GetMaxNumNbrs(), 4);
        EXPECT_DOUBLE_EQ(w->GetSparsity(), 0);
        EXPECT_DOUBLE_EQ(w->GetDensity(), 0.12965964343598055);
        EXPECT_DOUBLE_EQ(w->GetMeanNumNbrs(), 4);
        """

    def test_distance_threshold_weights(self):
        dist_thres = pygeoda.weights.min_threshold(self.nat)
        w = pygeoda.weights.distance(self.nat, dist_thres)
        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_FALSE(w->is_symmetric);
        EXPECT_THAT(w->num_obs, 3085);
        EXPECT_THAT(w->GetMinNumNbrs(), 1);
        EXPECT_THAT(w->GetMaxNumNbrs(), 85);
        EXPECT_DOUBLE_EQ(w->GetSparsity(), 0);
        EXPECT_DOUBLE_EQ(w->GetDensity(), 1.1939614751148575);
        EXPECT_DOUBLE_EQ(w->GetMeanNumNbrs(), 36.833711507293351);
        """

    def test_kernel_knn_weights(self):
        k = 15
        kernel = "triangular"
        w = pygeoda.weights.kernel(self.nat, k, kernel)
        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        EXPECT_FALSE(w->is_symmetric);
        EXPECT_THAT(w->num_obs, 3085);
        EXPECT_THAT(w->GetMinNumNbrs(), 15);
        EXPECT_THAT(w->GetMaxNumNbrs(), 15);
        EXPECT_DOUBLE_EQ(w->GetSparsity(), 0);
        EXPECT_DOUBLE_EQ(w->GetDensity(), 0.48622366288492708);
        EXPECT_DOUBLE_EQ(w->GetMeanNumNbrs(), 15);
        """

    def test_kernel_distband_weights(self):
        bandwidth = pygeoda.weights.min_threshold(self.nat)
        kernel = "triangular"
        w = pygeoda.weights.kernel_bandwidth(self.nat, bandwidth, kernel)
        """
        todo: convert the following c++ unit test to python unit test
              delete this section when finish
        """