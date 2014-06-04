CTT-reliability-estimates
=========================

Implementations of programs to find Guttman's lambda 1, lambda 2, lambda 3, lambda 3 and glb, all estimates of the reliability of a test. All of the methods take as a covariance matrix of the vector of questions in the test as either Numpy array-like structure or Python nested sequence. The input must be square matrix.

The theoretical background can be found in Jackson, P. H., \& Agunwamba, C. C. (1977). Lower Bounds for the Reliability of the Total Score on a Test Composed of Non-Homogeneous Items: I: Algebraic Lower Bounds. Psychometrika, 42(2), 567–578.

### Lambda 1

Gives an estimate based on how much of the variance of total test score can be explained by the sum of the variances of the individual questions.


### Lambda 2

In addition to the information taken into account in lambda 1, lambda 2 takes into consideration the information contained in the 2x2 sub-matricies which main diagonal elements are also main diagonal elemnts of the covariance matrix.

### Lambda 3

Improved lambda 1, can be shown to equal (n-1)/n * lambda 1. Unintuitevely, lambda 1 <= lambda 3 <= lambda 2.

### Lambda 4

Gives an estimate based on all the information in the covariance matrix, doesn't use all possible ways of interpreting it. Can be biased estamte based on sample ( Benton, T. (2013). An empirical assessment of Guttman ’ s Lambda 4 reliability coefficient. Retrieved June 03, 2014, from http://www.cambridgeassessment.org.uk/Images/141299-an-empirical-assessment-of-guttman-s-lambda-4-reliability-coefficient.pdf).

### Glb

Gives an estmate based on all the information in the covariance matrix, best possible estimate. Can be biased if used on the sample covariance matrix (Ten Berge, J. M. F., & Socan, G. (2004). The Greatest Lower Bound to the Reliability of a Test and the Hypothesis of Unidimensionality. Psychometrika, 69(4), 613–625. ). 







