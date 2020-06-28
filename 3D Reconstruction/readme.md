Use either of these codes to reconstruct a 3D image from 2D rgb and Depth images.

reconstruction_tensorflow.ipynb - uses only tensorflow models for depthmap and segmentation 
o3d.ipynb                       - uses tensorflow for depthmap and mx-net pretrained model for segmentation
Both of the above the o3d library to construct point cloud

3d.ipynb - does not use external library but takes lot longer time to produce 3d view angles.
Increase STEP size while generating a 3D structure to get more points at the cost of execution time.
