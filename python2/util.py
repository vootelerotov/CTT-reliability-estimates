u'''
Created on Jul 30, 2013

@author: Vootele Rotov
                  
'''

def check_that_matrix_is_square_and_fix_n(input_matrix):      
    def check_that_matrix_is_square():   
        for row in input_matrix:
            if len(row) != n:
                raise Exception(u"Matrix not square or missing data")  
    n = len(input_matrix) 
    check_that_matrix_is_square()
    return n

def fix_number_of_rows(input_matrix):
    def check_that_matrix_is_complete():   
        for row in input_matrix:
            if len(row) != n:
                raise Exception(u"Matrix not square or missing data")
    n = len(input_matrix[0])
    check_that_matrix_is_complete()
    return n
    

def calculate_sum_of_covariance_matrix_elements(cov_matrix,n = None):
    if n == None:
        n = check_that_matrix_is_square_and_fix_n(cov_matrix)
    summ = 0
    for i in xrange(n):
        for j in xrange(n):
            summ += cov_matrix[i,j]
    return summ

