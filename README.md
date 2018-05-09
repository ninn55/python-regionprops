# Python-regionprops

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>

This is a python implement of matlab build-in method `rigionprops`. See also [Measure properties of image regions - MATLAB regionprops](https://www.mathworks.com/help/images/ref/regionprops.html)

## Discription

According to the matlab documentation, the buld in function has 3 sets of main input. The first set stands for
the image input. It can be binary image connected components or label matrix. The second sets means the data type of out put, can be
struct or table. The third set contain which info should the output contains. The major properties are
`Area`, `BoundingBox` ,`Centroid` ,`MajorAxisLength` ,`MinorAxisLength`, `Orientation`, `Perimeter`.

|Property Name|Description|
|--------------|----------|
|'Area'|Actual number of pixels in the region, returned as a scalar. |
|'BoundingBox'|Smallest rectangle containing the region, returned as a 1-by-Q*2 vector, where Q is the number of image dimensions.specifies the upper-left corner and the width of the bounding box|
|'Centroid'|Center of mass of the region, returned as a 1-by-Q vector.|
|'MajorAxisLength'|Length (in pixels) of the major axis of the ellipse that has the same normalized second central moments as the region, returned as a scalar.|
|'MinorAxisLength'|Length (in pixels) of the minor axis of the ellipse that has the same normalized second central moments as the region, returned as a scalar.	|
|'Orientation'|Angle between the x-axis and the major axis of the ellipse that has the same second-moments as the region, returned as a scalar. The value is in degrees.|
|'Perimeter'|Distance around the boundary of the region. returned as a scalar. |

## Intro

I write this script as a personnal challenge. I am planning to add different functionnality as time goes.
Right now i am focousesd on the simple property like area, testing the matlab function and control input output.

## References