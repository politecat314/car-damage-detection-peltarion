# car-damage-detection-peltarion
Car damage detection trained on peltarion dataset using Keras (82.84% accuracy on validation set)

hdf5 file of model available at https://drive.google.com/file/d/1LaGm3aXrPWSWNQrTW8ridMiUWFGZZ2b4/view?usp=sharing
<br>
<h3><b>Inference</b></h3> 
1. download hdf5 file above and place inside src/model/<br>
2. Replace the images in src/test_images with your own<br>
3. Open src/demo.ipynb run<br>
<br>

<h3><b>For training the model</b></h3> 
1. for each category of images, make a folder inside src/dataset/train/ and place images there<br>
2. Create directory src/model<br>
3. Run src/Transfer_ResNet152v2.ipynb<br>
4. Models are saved inside src/model<br>
5. Follow inference steps above to test the model<br>
<br>
<br>
For testing this model, create a dir for each category in src/dataset/test<br>
In each categorie's dir, create a dir called Image and keep the images there. For example, 1.jpg will be stored in: src/dataset/test/category1/Image/1.jpg. This is a necessary workaround due to problems with the ```tf.keras.preprocessing.image_dataset_from_directory``` function.<br>
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
