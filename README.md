# 3D-image-understanding-Construction
Predicting the depth of the objects, construct 3D images from 2D images

## DEPTH ESTIMATION
**Dataset**
[NYU V2](https://tinyurl.com/nyu-data-zip)

**Pretrained models** are available at:
[PyTorch](https://drive.google.com/file/d/1wvhQhs2CAGumRslknNkPBRCNNKMOHw78/view?usp=sharing)
[Tensorflow](https://drive.google.com/file/d/1wvhQhs2CAGumRslknNkPBRCNNKMOHw78/view?usp=sharing)

[Models I trained](https://drive.google.com/drive/folders/1C88ENnOCOi_5eeusYJcFNieDSWYgawCk?usp=sharing) models have been saved in folders with names in the format "architecturename_shapeofinput_numberofepochs" (full refers to 480x640 input shape)
Results of each of these models are below.
Run the evaluate notebook in evaluate directory using appropriate model and input-size for evaluation
Evaluation was done on the [nyutest_data](https://s3-eu-west-1.amazonaws.com/densedepth/nyu_test.zip) compiled in .npy format
Results obtained 
+------------------------------------------+-------------+--------+--------+--------+
| Model                                    | epochs      | a1     | a2     | a3     |
+------------------------------------------+-------------+--------+--------+--------+
| Offical DenseNet(TF1.x and Multiple GPU) | 50 on 2 GPU | 0.8407 | 0.9721 | 0.9937 |
+------------------------------------------+-------------+--------+--------+--------+
| Our DenseNet169                          | 4           | 0.3276 | 0.6319 | 0.8283 |
+------------------------------------------+-------------+--------+--------+--------+
| Our MobileNetV2                          | 6           | 0.4022 | 0.7135 | 0.8800 |
+------------------------------------------+-------------+--------+--------+--------+
| Our EfficientNetB0                       | 6           | 0.3339 | 0.6327 | 0.8250 |
+------------------------------------------+-------------+--------+--------+--------+
Work is based on [High Quality Monocular Depth Estimation via Transfer Learning](https://arxiv.org/abs/1812.11941)
Ibraheem Alhashim and Peter Wonka

## 3D from rgb and depth
Run either of the notebooks in the 3D Reconstruction directory (one uses o3d and is faster, other is slow and customisable and doesnot require any external library)
Point clouds generated can be downloaded and viewed using softwares like Meshlab
