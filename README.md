# car-damage-detection-peltarion
Car damage detection trained on peltarion dataset using Keras (82.84% accuracy on validation set)

hdf5 file of 82.94% accuracy model available at https://drive.google.com/file/d/1LaGm3aXrPWSWNQrTW8ridMiUWFGZZ2b4/view?usp=sharing
<br>
<h3><b>For trying out the model:</b></h3> 
1. download hdf5 file above and place inside src/model/<br>
2. Replace the images in src/test_images with your own<br>
3. Open src/demo.ipynb run<br>
<br>

![Alt text](src/demo.jpg?raw=true "Demo")
<br><br>
<h3><b>Info about the dataset</b></h3> 
Dataset available for download here: https://peltarion.com/knowledge-center/documentation/terms/dataset-licenses/car-damage<br>

Image input size is 224x224x3 (RGB). Model classifies images to one of the classes:<br>
0: 'bumper_dent'<br>
1:'bumper_scratch'<br>
2:'door_dent'<br>
3:'door_scratch'<br>
4:'glass_shatter'<br>
5:'head_lamp'<br>
6:'no_damage'<br>
7:'smash'<br>
8:'tail_lamp'<br>
<br>
<h3><b>How model was trained</b></h3>
ResNet50 model pretrained on ImageNet is loaded. 2 dense layers added. ResNet50 layers are frozen and the 2 dense layers are trained on peltarian dataset. Refer to \src\Transfer_ResNet50.ipynb for details.<br>
<br>
<h3><b>Requirements</b></h3>
Tensorflow 2.6<br>
Pillow 8.3.1
