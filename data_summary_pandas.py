# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

peltarion = "preprocessed\index.csv"

df = pd.read_csv(peltarion)

print(df['class'].value_counts())