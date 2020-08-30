# Invariant_Moments
# What's Image Moment?
Image Moment is a particular weighted average of image pixel intensities, with the help of which we can find some specific properties of an image, like radius, area, centroid etc. To find the centroid of the image, we generally convert it to binary format and then find its center.
# Central moment 
Notice that the above central moments are translation invariant. In other words, no matter where the blob is in the image, if the shape is the same, the moments will be the same.
# Central Normalized moment 
Normalized central moments  are used  to make the central moment invariant to scale.
# What are Hu Moments ?
Hu moments are a set of 7 numbers calculated using central moments that are invariant to image transformations.
The first 6 moments have been proved to be invariant to translation, scale and reflection while the 7th moment’s sign changes for image reflection.
The 7 moments are calculated using the Following formulae 
<img src="https://www.learnopencv.com/wp-content/ql-cache/quicklatex.com-bed773267cd52c029f069695b1aa6c05_l3.png">


In the table below we have 6 images and their Hu moments :
<img src="https://www.learnopencv.com/wp-content/uploads/2018/12/HuMoments-Shape-Matching.png">
*	Translation (between s0 and s1)
*	Scale(between s1 and s2)
*	Rotation(between s2 and s3)
*	Reflection (between s3 and s4, except the sign of last Hu moment of S4 is flipped
# Zernike Moments
We consider the use of Zernike moments (ZMs) for rotation-and scale-invariant classification of images. It is well known that ZMs are rotation-invariant only. We make use of the major benefit of the Fourier-Mellin (FM) transformation, which changes the rotation and the scale into translation. 
