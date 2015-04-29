#LCAV-31: A Dataset for Light Field Object Recognition

We present LCAV-31, a multi-view object recognition dataset designed specifically for benchmarking light field image analysis tasks. The principal distinctive factor of LCAV-31 compared to similar datasets is its design goals and availability of novel visual information for more accurate recognition (i.e. light field information).

 
Light field imaging has received increased attention in recent years mostly due to availability of consumer light field cameras such as Lytro and Raytrix. In this emerging imaging technology rays from multiple views are captured from a scene. The improved sensing capability and the extra information captured by a light field camera enables novel lines of research in order to significantly improve current vision tasks such as object recognition, reconstruction depth mapping.
 
Many light field processing algorithms have been proposed in recent year due to the increased attention toward this area. The need to evaluate different aspects of these algorithms has led to various light field image sets proposed so far. The structure and associated ground truth information of any of these datasets have been optimized for a specific task such as reconstruction or depth estimation. 
 
On the other side, many object recognition benchmarks are already known among the computer vision community. There is a huge diversity regarding the objectives, scope, capturing setup and other properties between these datasets. However, they mostly consist of traditional color or grayscale images. This restricts their use in evaluation of algorithms which utilize data of modern sensors such as depth or light fields. This issue and other drawbacks of current object recognition datasets such as bias and lack of object diversity bold the need to construct a novel dataset with more information available per object than traditional color images.
 
LCAV-31 is the first light field object recognition dataset which provides a unified framework for benchmarking light field retrieval, object recognitions and tracking systems. It provides the possibility to evaluate effectiveness of different sensed information such as color and light field in object recognition accuracy. 
 
The dataset is composed of 31 object categories captured from ordinary household objects. We captured the color and light field images using the recently popularized Lytro consumer camera. Different views of each object have been provided as well as various poses and illumination conditions. 
 
The images have been processed and converted from Lytro format to the popular JPG format. Each image is actually a grid of 10x10 subviews. 
 
For any comments or problems, feel free to contact alireza.ghasemi@epfl.ch.
