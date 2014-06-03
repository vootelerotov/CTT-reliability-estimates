'''
Created on Aug 7, 2013

Using SciPy optimization, cvxpy has bugs when it comes down to quad form.

@author: Vootele Rotov
                  
'''
import numpy as np
import util

def calculate_lambda_4(cov_matrix):
    """
    Lambda 4, based on Guttman, 1945, using the implementation of Jackson,Agunwamba, 1977
    Based on idea that we try to best possible split (u is a vector, with elements either 1 or -1, ones will be in one split, minus ones in another) 
    NAIVE IMPLEMENTATION, works with relativiely low N, better approches available,  see Benton, 2013, 
    """
    
    def objective_function(u):
        return u.T.dot(cov_matrix.dot(u))

    
    def try_vectors():
        """
        Idea : generate half of all possible vectors of length n, such that if vector v is in, vector -v is not. 
        Using binary representation as string, from 2**(n-1) to 2**n, coding "0" to "-1"
        """
        smallest = np.Infinity
        result_vector = []
        l = []
        for i in range(2**(n-1),2**n):
            binary_of_i = np.binary_repr(i,width=n)
            binary_of_i_int = [ 1 if x == "1" else -1 for x in binary_of_i]
            u = np.array(binary_of_i_int)
            result = objective_function(u)
            if result < smallest:
                smallest = result
                result_vector = u
        return smallest
             
    def calc_lambda(smallest):
        return 1 - (smallest/
            util.calculate_sum_of_covariance_matrix_elements(cov_matrix, n))
        
    cov_matrix = np.array(cov_matrix)
    n = util.check_that_matrix_is_square_and_fix_n(cov_matrix)
    return calc_lambda(try_vectors())



    
        
    

