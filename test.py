# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from twin_distribution import Normal
from twin_distribution import Binomial

class TestNormalClass(unittest.TestCase):
    def setUp(self):
        self.normal_dist = Normal(25, 2)
        self.normal_dist.read_input_file('numbers.txt') 

    def test_initialization(self): 
        self.assertNotEqual(self.normal_dist.mean, 25, 'incorrect mean')
        self.assertNotEqual(self.normal_dist.stdev, 2, 'incorrect standard deviation')

    def test_readdata(self):
        self.assertEqual(self.normal_dist.data,\
         [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.normal_dist.calculate_mean(),\
         sum(self.normal_dist.data) / float(len(self.normal_dist.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.assertEqual(round(self.normal_dist.calculate_stdev(), 2), 92.87, 'sample standard deviation incorrect')
        self.assertEqual(round(self.normal_dist.calculate_stdev(0), 2), 88.55, 'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.normal_dist.pdf(25), 5), 0.00365,\
         'pdf function does not give expected result') 
        self.normal_dist.calculate_mean()
        self.normal_dist.calculate_stdev()
        self.assertEqual(round(self.normal_dist.pdf(75), 5), 0.00429,\
        'pdf function after calculating mean and stdev does not give expected result')

    def test_add(self):
        normal_dist_one = Normal(25, 3)
        normal_dist_two = Normal(30, 4)
        normal_sum = normal_dist_one + normal_dist_two

        self.assertEqual(normal_sum.mean, 55)
        self.assertEqual(normal_sum.stdev, 5)

class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.4, 20)
        self.binomial.read_input_file('numbers_binomial.txt')

    def test_initialization(self):
        self.assertEqual(self.binomial.p, 0.4, 'p value incorrect')
        self.assertEqual(self.binomial.n, 20, 'n value incorrect')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')

    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)

    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,2), 2.19)

    def test_replace_stats_with_data(self):
        p, n = self.binomial.replace_stats_with_data()
        self.assertEqual(round(p,3), .615)
        self.assertEqual(n, 13)

    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.07465)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.01235)

        self.binomial.replace_stats_with_data()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two

        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)


if __name__ == '__main__':
    unittest.main()