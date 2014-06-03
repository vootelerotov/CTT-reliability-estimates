'''
Created on Aug 5, 2013

@author: Vootele Rotov
                  
'''
import util
import logging
import numpy as np


def calculate_lambda_1(cov_matrix):
    """ 
    Based on Guttman,1945, for calculations using Jackson,Aguvwamba,1977,[569]
    """

    def sum_of_main_diagonal():
        summ = 0
        for i in range(n):
            summ += cov_matrix[i,i]
        return summ

    cov_matrix = np.array(cov_matrix)
    n = util.check_that_matrix_is_square_and_fix_n(cov_matrix) 

    return 1 - (sum_of_main_diagonal()/
    	util.calculate_sum_of_covariance_matrix_elements(cov_matrix, n))