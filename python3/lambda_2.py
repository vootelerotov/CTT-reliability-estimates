'''
Created on Aug 5, 2013

@author: Vootele Rotov
                  
'''

import logging
from lambda_1 import calculate_lambda_1
from util import calculate_sum_of_covariance_matrix_elements

def calculate_lambda_2(cov_matrix):
    """
    Using Guttman,1945,[259] definition
    """
    def sum_of_squares_of_non_diagonal_matrix_elements():
        summ = 0
        for i in range(n):
            for j in range(i):
                    summ += cov_matrix[i,j]**2 
        return 2*summ
    
    n = len(cov_matrix)
    l1 = calculate_lambda_1(cov_matrix)
    sum_of_squares = sum_of_squares_of_non_diagonal_matrix_elements()
    under_square_root =((n)/(n-1)* sum_of_squares)**(1/2)

    return l1 + (under_square_root/
        calculate_sum_of_covariance_matrix_elements(cov_matrix))
    
    
    
