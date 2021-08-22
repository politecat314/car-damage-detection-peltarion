# car-damage-detection-peltarion
Car damage detection trained on peltarion dataset using Keras

hdf5 file of model available at https://drive.google.com/file/d/1UpGFBdEjSNMeg506yzecg3BMbBSfN0_B/view?usp=sharing

Image input size is 224x224x3 (RGB). Model classifies images to one of the classes:
0: 'bumper_dent'
1:'bumper_scratch'
2:'door_dent'
3:'door_scratch'
4:'glass_shatter'
5:'head_lamp'
6:'tail_lamp'
7:'unknown'

Model architecture:
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
_________________________________________________________________
resnet50 (Functional)        (None, None, None, 2048)  23587712  
_________________________________________________________________
global_average_pooling2d (Gl (None, 2048)              0         
_________________________________________________________________
dropout (Dropout)            (None, 2048)              0         
_________________________________________________________________
flatten (Flatten)            (None, 2048)              0         
_________________________________________________________________
batch_normalization (BatchNo (None, 2048)              8192      
_________________________________________________________________
dense (Dense)                (None, 1024)              2098176   
_________________________________________________________________
dense_1 (Dense)              (None, 8)                 8200      
_________________________________________________________________
Total params: 25,702,280
Trainable params: 2,110,472
Non-trainable params: 23,591,808
_________________________________________________________________


ResNet50 model pretrained on ImageNet is loaded. 2 dense layers added. ResNet50 layers are frozen and the 2 dense layers are trained on peltarian dataset.
