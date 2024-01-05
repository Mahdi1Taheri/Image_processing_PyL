# Assignment32(6th)
## Applying Convolution filters on image
to apply different filters on image, we use 2d arrays called kernels.<br>
In image convolution, involves a kernel that is applied over the input image’s pixels to generate an output image.<br>
EXAMPLES:<br>
![img convolution](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_kernel1.png)<br>
![img convolution](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_kernel2.png)<br>
![img convolution](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_kernel3.png)<br>
![img convolution](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_kernel4.png)<br>
![img convolution](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_kernel5.png)<br>

## Average filter
we have a simple image with hidden thing inside the image. we have to apply average filter on image to reveal hidden things.<br>
**Orginal image:**<br>
[img original](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/input/1.tif)<br>
**And the result:**<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/fig_magic.png)<br>
## Median filter
The median filter is an algorithm that is useful for the removal of impulse noise.<br>
we use `cv2.medianBlur()` to apply median filter.<br>
<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_median1.png)<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_median2.png)<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_median3.png)<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_median4.png)<br>
![img result](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/result_median5.png)<br>

## Histogram equalization
Histogram Equalization is a computer image processing technique used to improve contrast in images.<br>
using `cv2.equalizeHist()` we can equalize the image histogram and improve the contrast.<br>
<br>
![histogram equalization](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/equalize1.png)<br>
![histogram equalization](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/equalize2.png)<br>
another algorithm for histogram equalization is CLAHE. <br>
The CLAHE algorithm has three major parts: tile generation, histogram equalization, and bilinear interpolation.<br>
using CLAHE algorithm gives better results.<br>
in opencv, we have `cv2.createCLAHE()` to use CLAHE algorithm.<br>
<br>
![histogram equalization](https://github.com/Mahdi1Taheri/Image_processing_PyL/blob/main/Assignment32/output/equalize_clahe.png)<br>

