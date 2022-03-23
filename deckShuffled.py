# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:49:33 2022

@author: João - Local
"""


import csv
import random


with open(r'maindeck.csv', 'r') as f:
    reader = csv.reader(f)
    deckId = [line[0] for line in reader]
    
random.shuffle(deckId)
    
