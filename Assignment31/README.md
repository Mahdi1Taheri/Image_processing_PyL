# Assignment 31
## Histogram
This program calculates the histogram of an image then shows the figur(graph) of image histogram<br>
using `matplotlib` library.<br>
+ image histogram using `plt.bar`<br>
![bar](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/baca92446367c17fb62b5bf3a1a8638a4dcbbff9/Assignment31/output/histogram_bar.png)
<br>

+ image histogram using `plt.hist`<br>
![hist](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/b92f6920b87bb045ab7475b462262a20a26f0b61/Assignment31/output/histogram_hist.png)
<br>

+ image histogram using `plt.plot`<br>
![plot](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/b92f6920b87bb045ab7475b462262a20a26f0b61/Assignment31/output/histogram_plot.png)
<br>

## Foreground focus, blur background
this program will blur background of a white object. like the below example<br>

+ Input:<br>

![flower_input](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/a38d79827a46f5477561fa20231408cac9161ebb/Assignment31/input/flower_input.jpg)
<br>

+ Output:<br>

![flower-output](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/a38d79827a46f5477561fa20231408cac9161ebb/Assignment31/output/foreground_focus.png)

## Edge detection
This program will show the edges using [kernels](https://medium.com/swlh/image-processing-with-python-convolutional-filters-and-kernels-b9884d91a8fd).<br>
+ input
![input](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/a38d79827a46f5477561fa20231408cac9161ebb/Assignment31/input/lion.png)

+ output
![output](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/a38d79827a46f5477561fa20231408cac9161ebb/Assignment31/output/edge_detect.png)

## Vertical and horizontal edge detection
we have an image of a building. this program can detect vertical and horizontal edges of that building.<br>
+ input<br>
![input](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/2964cfe41f540fda1c34ec1e2879df376e1e117a/Assignment31/input/building.png)

+ output horizontal<br>
![output](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/2964cfe41f540fda1c34ec1e2879df376e1e117a/Assignment31/output/horizontal.png)

+ output vertical<br>
![output_vertical](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/2964cfe41f540fda1c34ec1e2879df376e1e117a/Assignment31/output/vertical.png)<br>

## Noise reduction

In many cases, especially medical photos, it is very necessary to reduce additional noise.<br>
This program does this in a simple way.
Mean filtering is a simple and easy to implement method of smoothing images. It is often used to reduce noise in images.<br>
The mean filter is computed using a convolution. The idea of mean filtering is simply to replace each pixel value in an image<br> 
with the mean (average) value of its neighbors, including itself.<br> 
Often a 3×3 square kernel is used, although larger kernels (e.g. 5×5 squares) can be used for more severe smoothing.<br> 
+ image 1<br>
![input](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/5dfcf397e87be0d61daf4f8ae833152bfaf450dd/Assignment31/input/board_noisy.png)
+ output 1<br>
![output1](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/5dfcf397e87be0d61daf4f8ae833152bfaf450dd/Assignment31/output/board_noise_reduced.png)<br>

+ image 2 <br>
![input2](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/5dfcf397e87be0d61daf4f8ae833152bfaf450dd/Assignment31/input/image_noisy.png)<br>
+ output 2 <br>
![output2](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/5dfcf397e87be0d61daf4f8ae833152bfaf450dd/Assignment31/output/circle_noise_reduced.png)



