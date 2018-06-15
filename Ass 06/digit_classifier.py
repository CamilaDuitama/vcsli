# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:10:14 2018

@author: gorgi
"""

import mnist_loader
import network
import numpy as np
from matplotlib import pyplot

########################################################
# To Do: Read training_data, validation_data, test_data 
########################################################

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=validation_data)
    
########################################################
# To Do: Visualize accuracy over 30 epochs.
########################################################
