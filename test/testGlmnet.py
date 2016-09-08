# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:39:55 2016

@author: bbalasub
"""

import sys
sys.path.append('../test')
sys.path.append('../lib')

import scipy
import glmnet 
import importlib
import pprint

importlib.reload(glmnet)

# parameters
baseDataDir= '../data/'
testType = 'multinomial'

# call test functions
if testType == 'gaussian':
    ##  elnet caller 
    y = scipy.loadtxt(baseDataDir + 'QuickStartExampleY.dat', dtype = scipy.float64)
    x = scipy.loadtxt(baseDataDir + 'QuickStartExampleX.dat', dtype = scipy.float64)
    fit = glmnet.glmnet(x = x, y = y, family = 'gaussian')
    #fit = glmnet.glmnet(x = x, y = y, family = 'gaussian', alpha = 0.5)
    print('fit:')
    pprint.pprint(fit)

if testType == 'binomial':
    # lognet caller
    x = scipy.loadtxt(baseDataDir + 'BinomialExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'BinomialExampleY.dat', dtype = scipy.float64)
    fit = glmnet.glmnet(x = x, y = y, family = 'binomial')
    print('fit:')
    pprint.pprint(fit)

if testType == 'multinomial':
    # coxnet caller
    x = scipy.loadtxt(baseDataDir + 'MultinomialExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'MultinomialExampleY.dat', dtype = scipy.float64, delimiter = ',')
    fit = glmnet.glmnet(x = x, y = y, family = 'multinomial')
    print('fit:')
    pprint.pprint(fit)    

if testType == 'cox':
    # coxnet caller
    x = scipy.loadtxt(baseDataDir + 'CoxExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'CoxExampleY.dat', dtype = scipy.float64, delimiter = ',')
    fit = glmnet.glmnet(x = x, y = y, family = 'cox')
    print('fit:')
    pprint.pprint(fit)

if testType == 'mgaussian':
    # coxnet caller
    x = scipy.loadtxt(baseDataDir + 'MultiGaussianExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'MultiGaussianExampleY.dat', dtype = scipy.float64, delimiter = ',')
    fit = glmnet.glmnet(x = x, y = y, family = 'mgaussian')
    print('fit:')
    pprint.pprint(fit)    
    
if testType == 'poisson':
    # coxnet caller
    x = scipy.loadtxt(baseDataDir + 'PoissonExampleX.dat', dtype = scipy.float64, delimiter = ',')
    y = scipy.loadtxt(baseDataDir + 'PoissonExampleY.dat', dtype = scipy.float64, delimiter = ',')
    fit = glmnet.glmnet(x = x, y = y, family = 'poisson')
    print('fit:')
    pprint.pprint(fit)

    
