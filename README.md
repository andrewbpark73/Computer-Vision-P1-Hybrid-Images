# CS5670 Computer Vision

## Project 1: Hybrid Images

### Introduction

Creating hybrid images using a series of image filters. Hybrid images are static, but show different images depending on how far you are away from the picture.

* High pass filtered version of picture 1
* Low pass filtered version of picture 2
* Blended hybrid image of aligned picture 1 and 2

Detailed project description can be found [here](https://www.cs.cornell.edu/courses/cs5670/2024sp/projects/pa1/index.html).

### Steps

1. cross_correlation_2d
2. convolve_2d
3. gaussian_blur_kernel_2d
4. low_pass
5. high_pass
  
### Structure

| Name                  | Function                                           |
| ------------          | -------------------------------------------------- |
| /resources            | Images used to create hybrid                       |
| adjust_brightness.py  | Adjust brightness of resulting image               |
| hybrid.py             | Apply the five filters to the two images and blend |
| test.py               | Test cases provided to test and debug our code     |
| gui.py                | Gui provided to create panorama                    |

#### Libraries used

* matplotlib=3.8.0
* numpy=1.21.5
* opencv=4.6.0
* pillow=10.0.1
* py-opencv=4.6.0
* pyparsing=3.0.9
* python=3.9
* pyttk=0.3.2
* scipy=1.7.3
* tk=8.6.12


### Result: Shoe-Man

## Images Used

- **First Image**: left_shoe.png (image of a shoe) -> Low Pass Filter
- **Second Image**: right_JinminOfBTS.png (image of Jimin of BTS yawning) -> High Pass Filter

## Parameters

- **Low Pass Filter Parameters** (Applied to 'left_shoe.png'):
  - Kernel Size: 18
  - Kernel Sigma: 6.0
  - Low Frequencies Mode
- **High Pass Filter Parameters** (Applied to 'right_JinminOfBTS.png'):
  - Kernel Size: 25
  - Kernel Sigma: 10.0
  - High Frequencies Mode
- **Mix-in Ratio**: 0.8 (favoring the high-frequency components of right_JinminOfBTS.png image)
- **scale_factor**: 2.8

## Correspondance

- First Image Points:
  - [251.03789126853377,238.1852551984877],[549.6408566721582,71.45557655954632],[455.831960461285,254.06427221172024]
- Second Image Points:
  - [270.4586330935252,262.13991769547323],[537.3111510791367,43.20987654320987],[468.07374100719426,237.65432098765433]

#### Input
| <img src="/results/left_shoe.png" height="400px">  | <img src="/results/right_JiminofBTS.png" height="400px">  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

#### Hybrid Image

| <img src="/results/hybrid.png" height="400px">    | <img src="/results/hybrid.png" height="50px"> 
| ---------------------------------------------------------------- | --------------------------------------- |