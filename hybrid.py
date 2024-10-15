import sys
import cv2
import numpy as np

def cross_correlation_2d(img, kernel):
    '''Given a kernel of arbitrary m x n dimensions, with both m and n being
    odd, compute the cross correlation of the given image with the given
    kernel, such that the output is of the same dimensions as the image and that
    you assume the pixels out of the bounds of the image to be zero. Note that
    you need to apply the kernel to each channel separately, if the given image
    is an RGB image.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN

    kernel_height, kernel_width = kernel.shape
    pad_height, pad_width = kernel_height // 2, kernel_width // 2

    # Padding the image to handle edges
    if len(img.shape) == 3:  # RGB image
        padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), 'constant', constant_values=0)
    else:  # Grayscale image
        padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width)), 'constant', constant_values=0)

    output = np.zeros_like(img)

    # Iteration Order (y → x), following the iteration order of image processing
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if len(img.shape) == 3:  # RGB image
                for channel in range(img.shape[2]):
                    region = padded_img[y:y+kernel_height, x:x+kernel_width, channel]
                    output[y, x, channel] = np.sum(region * kernel)
            else:  # Grayscale image
                region = padded_img[y:y+kernel_height, x:x+kernel_width]
                output[y, x] = np.sum(region * kernel)
    return output

    # TODO-BLOCK-END

def convolve_2d(img, kernel):
    '''Use cross_correlation_2d() to carry out a 2D convolution.

    Inputs:
        img:    Either an RGB image (height x width x 3) or a grayscale image
                (height x width) as a numpy array.
        kernel: A 2D numpy array (m x n), with m and n both odd (but may not be
                equal).

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    
    # Flip the kernel for convolution
    kernel_flipped = np.flip(kernel, axis=(0, 1))
    
    kernel_height, kernel_width = kernel_flipped.shape
    pad_height, pad_width = kernel_height // 2, kernel_width // 2

    # Padding the image to handle edges
    if img.ndim == 3:  # RGB image
        padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), 'constant', constant_values=0)
    else:  # Grayscale image
        padded_img = np.pad(img, ((pad_height, pad_height), (pad_width, pad_width)), 'constant', constant_values=0)

    output = np.zeros_like(img)
    
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if len(img.shape) == 3:  # RGB image
                for channel in range(img.shape[2]):
                    region = padded_img[y:y+kernel_height, x:x+kernel_width, channel]
                    output[y, x, channel] = np.sum(region * kernel_flipped)  # Use flipped kernel here
            else:  # Grayscale image
                region = padded_img[y:y+kernel_height, x:x+kernel_width]
                output[y, x] = np.sum(region * kernel_flipped)  # And here
    return output
    
    
    # TODO-BLOCK-END

def gaussian_blur_kernel_2d(sigma, height, width):
    '''Return a Gaussian blur kernel of the given dimensions and with the given
    sigma. Note that width and height are different.

    Input:
        sigma:  The parameter that controls the radius of the Gaussian blur.
                Note that, in our case, it is a circular Gaussian (symmetric
                across height and width).
        width:  The width of the kernel.
        height: The height of the kernel.

    Output:
        Return a kernel of dimensions height x width such that convolving it
        with an image results in a Gaussian-blurred image.
    '''
    # TODO-BLOCK-BEGIN
    
    ax = np.linspace(-(width - 1) / 2., (width - 1) / 2., width)
    ay = np.linspace(-(height - 1) / 2., (height - 1) / 2., height)
    xx, yy = np.meshgrid(ax, ay)
    kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
    return kernel / np.sum(kernel)
    
    # TODO-BLOCK-END

def low_pass(img, sigma, size):
    '''Filter the image as if its filtered with a low pass filter of the given
    sigma and a square kernel of the given size. A low pass filter supresses
    the higher frequency components (finer details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    
    low_pass_kernel = gaussian_blur_kernel_2d(sigma, size, size)
    return convolve_2d(img, low_pass_kernel)
    
    # TODO-BLOCK-END

def high_pass(img, sigma, size):
    '''Filter the image as if its filtered with a high pass filter of the given
    sigma and a square kernel of the given size. A high pass filter suppresses
    the lower frequency components (coarse details) of the image.

    Output:
        Return an image of the same dimensions as the input image (same width,
        height and the number of color channels)
    '''
    # TODO-BLOCK-BEGIN
    
    low_passed = low_pass(img, sigma, size)
    return img - low_passed

    # TODO-BLOCK-END

def create_hybrid_image(img1, img2, sigma1, size1, high_low1, sigma2, size2,
        high_low2, mixin_ratio, scale_factor):
    '''This function adds two images to create a hybrid image, based on
    parameters specified by the user.'''
    high_low1 = high_low1.lower()
    high_low2 = high_low2.lower()

    if img1.dtype == np.uint8:
        img1 = img1.astype(np.float32) / 255.0
        img2 = img2.astype(np.float32) / 255.0

    if high_low1 == 'low':
        img1 = low_pass(img1, sigma1, size1)
    else:
        img1 = high_pass(img1, sigma1, size1)

    if high_low2 == 'low':
        img2 = low_pass(img2, sigma2, size2)
    else:
        img2 = high_pass(img2, sigma2, size2)

    img1 *=  (1 - mixin_ratio)
    img2 *= mixin_ratio
    hybrid_img = (img1 + img2) * scale_factor
    return (hybrid_img * 255).clip(0, 255).astype(np.uint8)

