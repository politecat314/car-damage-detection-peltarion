# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import pandas as pd
import random

peltarion = "preprocessed/Image"
df = pd.read_csv('preprocessed/index.csv')

test_number = 5



classes = {0:'unknown', 1:'door_dent',2:'door_scratch',3:'glass_shatter',
4:'tail_lamp',5:'head_lamp',6:'bumper_dent',7:'bumper_scratch'}


correct = 0
wrong_labels = {'unknown':0, 'door_dent':0,'door_scratch':0,'glass_shatter':0,
'tail_lamp':0,'head_lamp':0,'bumper_dent':0,'bumper_scratch':0}



for i in range(test_number):
    index = random.randint(0, len(df)-1)
    
    image_file_name = df['image'][index][6:]
    
    # display the image
    pic = Image.open('preprocessed/Image/'+image_file_name)
    pic.show()
    
    actual_class = df.loc[df['image'] == 'image/'+image_file_name]['class']
    
    print(classes)
    chosen_val = int(input('what class does this image belong to?: '))
    chosen_class = classes[chosen_val]
    
    if str(chosen_class) == str(actual_class):
        correct += 1
        print("Correct!")
    else:
        print("Wrong, actual class is: " + str(actual_class.value))
    
    print()
    

print("Percentage correct: ", (correct/test_number))
print(wrong_labels)