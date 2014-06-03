'''
Created on Jul 31, 2013

@author: Voss
'''
import sys
sys.path.append("../python3")
import unittest
import logging
from lambda_3 import calculate_lambda_3
import numpy as np

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):     
        logging.basicConfig(filename="./test_log.log",
                        level=logging.DEBUG,
                        format="%(asctime)s -%(levelname) -8s  %(message)s")
        cls.log = logging.getLogger()
    

    def testCronBach(self):
        """
        Based on first covariance matrix of Sijtsma,2009: 117
        """
        self.log.debug("------------------------ Cronbach test number 1 based on Sijtsma ---------------------------")
        cov_matrix = np.array([[0.25,0.2,0,0,0,0],[0.2,0.25,0,0,0,0],[0,0,0.25,0.2,0,0],[0,0,0.2,0.25,0,0],[0,0,0,0,0.25,0.2],[0,0,0,0,0.2,0.25]])
        self.assertAlmostEqual(calculate_lambda_3(cov_matrix), 0.533, 3, "Not equal")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()