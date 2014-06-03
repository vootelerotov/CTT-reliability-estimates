'''
Created on Aug 8, 2013

@author: Voss
'''
import sys
sys.path.append("../python3")
import unittest
import logging
import numpy as np
import lambda_4


class Test(unittest.TestCase):


    @classmethod
    def setUpClass(cls): 
        logging.basicConfig(filename="./test_log.log",
                        level=logging.DEBUG,
                        format="%(asctime)s -%(levelname) -8s  %(message)s")
        cls.log = logging.getLogger()

    def testLambda4Sijtsma1(self):
        """
        Based on first covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2a)
        """
        self.log.debug("------------------------ l_4 test number 1 based on Sijtsma ---------------------------")
        cov_matrix = np.array([[0.25,0.2,0,0,0,0],[0.2,0.25,0,0,0,0],[0,0,0.25,0.2,0,0],[0,0,0.2,0.25,0,0],[0,0,0,0,0.25,0.2],[0,0,0,0,0.2,0.25]])
        self.assertAlmostEqual(lambda_4.calculate_lambda_4(cov_matrix), 0.889, 3, "Not equal")
        
    def testLambda4Sijtsma2(self):
        #NOT WORKING, FAULT WITH REFRENCE?
        # My result goes with Revelles own R package result, error in the paper!
        # Answer in paper : 0.647
        # Answer : 0.59
        """
        Based on second covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2b)
        """
        self.log.debug("-------------------------- l_4 test number 2 based on Sijtsma ---------------------------")
        cov_matrix = np.array([[0.25,0.1,0.1,0,0,0],[0.1,0.25,0.1,0,0,0],[0.1,0.1,0.25,0,0,0],[0,0,0,0.25,0.1,0.1],[0,0,0,0.1,0.25,0.1],[0,0,0,0.1,0.1,0.25]])
        self.assertAlmostEqual(lambda_4.calculate_lambda_4(cov_matrix), 0.59, 2, "Not equal")
    def testLambda4Sijtsma3(self):
        """
        Based on third covariance matrix of Sijtsma,2009: 117
        Data to be compared with taken from Revelle,Zinbarg, 2008 (S-2c)
        """
        self.log.debug("---------------------- l_4 test number 3 based on Sijtsma ----------------------------")
        cov_matrix = np.array([[0.25,0.04,0.04,0.04,0.04,0.04],[0.04,0.25,0.04,0.04,0.04,0.04],[0.04,0.04,0.25,0.04,0.04,0.04],[0.04,0.04,0.04,0.25,0.04,0.04],[0.04,0.04,0.04,0.04,0.25,0.04],[0.04,0.04,0.04,0.04,0.04,0.25]])
        self.assertAlmostEqual(lambda_4.calculate_lambda_4(cov_matrix), 0.533, 3, "Not equal")
        
    def testLambda4TenBergSocan(self):
        """
        Based on correlation matrix (12), Socan,Ten Berg, 2004, [622]
        Data to be compared with taken from Revelle,Zinbarg, 2008 (TB&S)
        """
        self.log.debug("---------------------- l_4 test number 4 based on Ten Berge and Socan ----------------------------")
        cov_matrix = np.array([[1,0.446,0.462,0.398,0.583,0.516],[0.446,1,0.38,0.241,0.536,0.483],[0.462,0.38,1,0.589,0.569,0.417],[0.398,0.241,0.589,1,0.459,0.403],[0.583,0.536,0.569,0.459,1,0.514],[0.516,0.483,0.417,0.403,0.514,1]])
        self.assertAlmostEqual(lambda_4.calculate_lambda_4(cov_matrix), 0.884, 2, "Not equal")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()