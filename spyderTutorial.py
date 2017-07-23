#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:29:38 2017

@author: vijaypatha
"""

'''def hello():
    print("hello world")
hello()'''

import numpy as np
import pandas as pd

if True:
    array = np.array ([1,4,5,8], float)
    print array
    print ""
    array = np.array([[1,2,3],[4,5,6]],float)
    print array
    
if True:
    data = {'years': [2010,2011,2012,2011,2012,2010,2011,2012],
            'team': ["Breas","Bears","Bears","Packers","Packers","Lions","Lions","Lions"],
            'wins':[11,8,10,15,11,6,10,4],
            'losses':[5,8,6,1,5,10,6,12]}
    football = pd.DataFrame(data)
    print football
    
    
