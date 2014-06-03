'''
Created on Aug 5, 2013

@author: Voss
'''
import sys
sys.path.append('../python3')
import unittest
import logging
import lambda_1
import numpy as np

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls): 
        logging.basicConfig(filename="./test_log.log",
                        level=logging.DEBUG,
                        format="%(asctime)s -%(levelname) -8s  %(message)s")
        cls.log = logging.getLogger()

    def testLambda1Sijtsma1(self):
        """
        Based on first covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2a)
        """
        self.log.debug("------------------------ l_2 test number 1 based on Sijtsma ---------------------------")
        cov_matrix = np.array([[0.25,0.2,0,0,0,0],[0.2,0.25,0,0,0,0],[0,0,0.25,0.2,0,0],[0,0,0.2,0.25,0,0],[0,0,0,0,0.25,0.2],[0,0,0,0,0.2,0.25]])
        self.assertAlmostEqual(lambda_1.calculate_lambda_1(cov_matrix), 0.444, 3, "Not equal")
        
    def testLambda1Sijtsma2(self):
        """
        Based on second covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2b)
        """
        self.log.debug("-------------------------- l_2 test number 2 based on Sijtsma ---------------------------")
        cov_matrix = np.array([[0.25,0.1,0.1,0,0,0],[0.1,0.25,0.1,0,0,0],[0.1,0.1,0.25,0,0,0],[0,0,0,0.25,0.1,0.1],[0,0,0,0.1,0.25,0.1],[0,0,0,0.1,0.1,0.25]])
        self.assertAlmostEqual(lambda_1.calculate_lambda_1(cov_matrix), 0.444, 3, "Not equal")
    def testLambda1Sijtsma3(self):
        """
        Based on third covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2c)
        """
        self.log.debug("---------------------- l_2 test number 3 based on Sijtsma ----------------------------")
        cov_matrix = np.array([[0.25,0.04,0.04,0.04,0.04,0.04],[0.04,0.25,0.04,0.04,0.04,0.04],[0.04,0.04,0.25,0.04,0.04,0.04],[0.04,0.04,0.04,0.25,0.04,0.04],[0.04,0.04,0.04,0.04,0.25,0.04],[0.04,0.04,0.04,0.04,0.04,0.25]])
        self.assertAlmostEqual(lambda_1.calculate_lambda_1(cov_matrix), 0.444, 3, "Not equal")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()