# Hybrid Image Project

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

## Observations and Conclusions

In combining high-pass and low-pass images, I found that selecting images with similar framing or correspondence was crucial. In this case, I personally increased the challenge by merging an image of a person with a shoe, which led to significant changes in the outcome even with slight differences in the three correspondent points. Through this assignment, I gained valuable hands-on experience by observing how Gaussian filter parameters, such as kernel size and sigma, directly affect the appearance of high-pass and low-pass images. Adjusting the mix-in ratio was also key to achieving a more natural-looking hybrid image. This process enhanced my understanding of image filtering and the synthesis of different images.