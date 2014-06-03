'''
Created on Jul 25, 2013

Calculates Cronbach's alfa.

@author: Vootele Rotov
'''

from util import fix_number_of_rows
from lambda_1 import calculate_lambda_1
import numpy as np
        
 
def calculate_lambda_3(cov_matrix):
    cov_matrix = np.array(cov_matrix)
    number_of_items = len(cov_matrix)
    return (number_of_items/(number_of_items-1))*calculate_lambda_1(cov_matrix)      

        
        
        
        
        
        
    

