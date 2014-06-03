'''
Created on Aug 1, 2013

@author: Vootele Rotov
'''
import sys
sys.path.append("../python2")
import unittest
from glb import Glb
import logging

class Test(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        logging.basicConfig(filename="./test_log.log",
                        level=logging.DEBUG,
                        format="%(asctime)s -%(levelname) -8s  %(message)s")
        cls.log = logging.getLogger()
        


    def testGlb(self):
        """
        Test based on ten Berge, Socan, 2004
        """
        self.log.debug("--------------------------- Glb test based on ten Berge ---------------------------")
        corr_matrix = [[1,0.446,0.462,0.398,0.583,0.516],[0.446,1,0.38,0.241,0.536,0.483],[0.462,0.380,1,0.589,0.569,0.417],[0.398,0.241,0.589,1,0.459,0.403],[0.583,0.536,0.569,0.459,1,0.514],[0.516,0.483,0.417,0.403,0.514,1]]
        glb = Glb(corr_matrix)
        self.assertAlmostEqual(glb.get_answer(), 0.885, 3, "Not equal")

    def testGlbSijtsma1(self):
        """
        Based on first covariance matrix of Sijtsma,2009: 117
        """
        self.log.debug("------------------------ Glb test number 1 based on Sijtsma ---------------------------")
        cov_matrix = [[0.25,0.2,0,0,0,0],[0.2,0.25,0,0,0,0],[0,0,0.25,0.2,0,0],[0,0,0.2,0.25,0,0],[0,0,0,0,0.25,0.2],[0,0,0,0,0.2,0.25]]
        glb = Glb(cov_matrix)
        self.assertAlmostEqual(glb.get_answer(), 0.889, 3, "Not equal")
        
    def testGlbSijtsma2(self):
        """
        Based on second covariance matrix of Sijtsma,2009: 117
        """
        self.log.debug("-------------------------- Glb test number 2 based on Sijtsma ---------------------------")
        cov_matrix = [[0.25,0.1,0.1,0,0,0],[0.1,0.25,0.1,0,0,0],[0.1,0.1,0.25,0,0,0],[0,0,0,0.25,0.1,0.1],[0,0,0,0.1,0.25,0.1],[0,0,0,0.1,0.1,0.25]]
        glb = Glb(cov_matrix)
        self.assertAlmostEqual(glb.get_answer(), 0.667, 3, "Not equal")
    def testGlbSijtsma3(self):
        """
        Based on third covariance matrix of Sijtsma,2009: 117
        """
        self.log.debug("---------------------- Glb test number 3 based on Sijtsma ----------------------------")
        cov_matrix = [[0.25,0.04,0.04,0.04,0.04,0.04],[0.04,0.25,0.04,0.04,0.04,0.04],[0.04,0.04,0.25,0.04,0.04,0.04],[0.04,0.04,0.04,0.25,0.04,0.04],[0.04,0.04,0.04,0.04,0.25,0.04],[0.04,0.04,0.04,0.04,0.04,0.25]]
        glb = Glb(cov_matrix)
        self.assertAlmostEqual(glb.get_answer(), 0.533, 3, "Not equal")
        
    def testGlbTenBergSocan(self):
        """
        Based on correlation matrix (12), Socan,Ten Berg, 2004, [622]
        Data to be compared with taken from Revelle,Zinbarg, 2008 (TB&S)
        """
        self.log.debug("---------------------- glb test number 4 based on Ten Berge and Socan ----------------------------")
        cov_matrix = [[1,0.446,0.462,0.398,0.583,0.516],[0.446,1,0.38,0.241,0.536,0.483],[0.462,0.38,1,0.589,0.569,0.417],[0.398,0.241,0.589,1,0.459,0.403],[0.583,0.536,0.569,0.459,1,0.514],[0.516,0.483,0.417,0.403,0.514,1]]
        glb = Glb(cov_matrix)
        self.assertAlmostEqual(glb.get_answer(), 0.885, 3, "Not equal")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()