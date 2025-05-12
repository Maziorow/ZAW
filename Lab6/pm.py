
import numpy as np
import matplotlib.pyplot as plt

def appendimages(im1, im2):
    # Ensure both images are 3-channel (RGB)
    if len(im1.shape) == 2:
        im1 = np.stack([im1] * 3, axis=-1)
    if len(im2.shape) == 2:
        im2 = np.stack([im2] * 3, axis=-1)

    rows1, cols1, ch1 = im1.shape
    rows2, cols2, ch2 = im2.shape

    # Pad shorter image to match height
    if rows1 < rows2:
        pad = np.zeros((rows2 - rows1, cols1, ch1), dtype=im1.dtype)
        im1 = np.concatenate((im1, pad), axis=0)
    elif rows1 > rows2:
        pad = np.zeros((rows1 - rows2, cols2, ch2), dtype=im2.dtype)
        im2 = np.concatenate((im2, pad), axis=0)

    return np.concatenate((im1, im2), axis=1)
   
    
    
def plot_matches(im1,im2,matches):
    colors=['r','g','b','c','m','y']
    im3 = appendimages(im1,im2)
    
    plt.figure()
    plt.imshow(im3)
    
    cols1 = im1.shape[1]
    for i, m in enumerate(matches):
            plt.plot([m[0][1],m[1][1]+cols1],[m[0][0],m[1][0]],colors[i%6], linewidth=0.5)
    plt.axis('off') 