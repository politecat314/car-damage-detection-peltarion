# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 13:42:24 2021

@author: aman9221

moving different classes of images to different folders. Easier to import as a tf.data.Dataset object and class labels are inferred
"""

import pandas as pd
import os

image_folder = "preprocessed/Image"
target_folder = "categorize/Image"

df = pd.read_csv("preprocessed/index.csv")


for index, row in df.iterrows():
    name = row['image'][6:]
    label = row['class']
    subset = row['subset']
    
    folder = 'train'
    if subset == 'V':
        folder = 'validation'
    
    os.replace(image_folder+'/'+name,folder+'/Image/'+label+'/'+name)

# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")