# car-damage-detection-peltarion
Car damage detection trained on peltarion dataset using Keras

hdf5 file of 82.94% accuracy model available at https://drive.google.com/file/d/1LaGm3aXrPWSWNQrTW8ridMiUWFGZZ2b4/view?usp=sharing

For trying out the model: 
1. download hdf5 file above and place inside src/model/<br>
2. Replace the images in src/test_images with your own<br>
3. Open src/demo.ipynb run<br>


Image input size is 224x224x3 (RGB). Model classifies images to one of the classes:
0: 'bumper_dent'
1:'bumper_scratch'
2:'door_dent'
3:'door_scratch'
4:'glass_shatter'
5:'head_lamp'
6:'no_damage'
7:'smash'
8:'tail_lamp'<br>

**How model was trained:**
ResNet50 model pretrained on ImageNet is loaded. 2 dense layers added. ResNet50 layers are frozen and the 2 dense layers are trained on peltarian dataset. Refer to `\src\Transfer_ResNet50.ipynb` for details.