u'''
Created on Jul 30, 2013

@author: Vootele Rotov
'''
from __future__ import division
import util 
import cvxpy as cv
import numpy as np

u""""
Idea: Observed covariance matrix  is of observed scores. 
That matrix is sum of true score coviarance matrix and error covariance matrix.
As errors don't correlate with anything else than themselves, the last is diagonal matrix.
So, C_obs = C_true + C_error
We look to maximize error (to find the worst possible case).
More can be found in Jackson,Agunwamba,1977 and Woodhouse,Jakson, 1977.
"""

class Glb(object):
    def __init__(self,cov_matrix):
        self._cov_matrix = np.array(cov_matrix)
        self._constraints = []
        self._n = util.check_that_matrix_is_square_and_fix_n(cov_matrix)
        self._generate_matrix_variables()
        self._divide_covariance_matrix_of_into_error_and_true_score()
        self._fix_error_cov_matrix_diagonal_fields_constraints()
        self._error_cov_matrix_non_diagonal_fields_are_0()
        self._prepare_program()
        self._solve_program()
        self._answer = self._calculate_Glb()

    def _generate_matrix_variables(self):
        self._true_cov_matrix = cv.semidefinite(self._n,
         name=u"true_cov_matrix")
        self._error_cov_matrix = cv.Variable(self._n, self._n,
         name=u"error_cov_matrix") 
    
    
    def _divide_covariance_matrix_of_into_error_and_true_score(self):
        u"""
        Constraint that C_obs = C_true + C_error
        """
        self._constraints.append(self._error_cov_matrix+
            self._true_cov_matrix == self._cov_matrix)
        
    def _fix_error_cov_matrix_diagonal_fields_constraints(self):
        u"""
        Error covariance matrix must be semidefinite,
        meaning that all elements on the diagonal must be positive
        """
        for i in xrange(self._n):
            self._constraints.append(self._error_cov_matrix[i,i] >= 0)

    def _error_cov_matrix_non_diagonal_fields_are_0(self):
        u"""
        Covariance between different errors is 0
        """
        for i in xrange(self._n):
            for j in xrange(self._n):
                if (i != j):
                    self._constraints.append(
                        self._error_cov_matrix[i,j] == 0) 

        
    def _prepare_program(self):
        u"""
        Minimize trace of true score covirance matrix
        """
        self._p = cv.Problem(cv.Minimize(
            sum([self._true_cov_matrix[i,i] for i in xrange(self._n)])),
            self._constraints)
        if not self._p.is_dcp():
            raise Exception(u"Non-DCP glb, something went terrible wrong")
            
            
    def _solve_program(self):

        try:
            self._p.solve()
        except:
            raise Exception(u"Program was unable to find glb")
        
    
    def _calculate_Glb(self):
        return 1 - (sum(
            [self._error_cov_matrix.value[i,i] for i in xrange(self._n)])/
            util.calculate_sum_of_covariance_matrix_elements(self._cov_matrix,self._n))
        

    def get_answer(self):
        return self._answer