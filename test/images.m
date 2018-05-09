clear all; close all; clc;

my_area()



function my_area()
    a = imread('..//assets//text.png');
    b = rgb2gray(a);
    bw = imbinarize(b, 'global');
    ar = regionprops('table', bw, 'Area');
    disp(ar)
    disp(strcat('There are ', num2str(height(ar)), ' chars'))
end

function my_