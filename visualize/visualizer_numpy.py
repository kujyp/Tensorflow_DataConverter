
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def show_nbyn_images(images, n=5, idx_range=None):
    if idx_range is None:
        idx_range = range(n ** 2)

    for idx in idx_range:
        plt.subplot(n,n,idx+1)
        show_nth_image(images,idx)
        plt.title(str(idx)+'th')
        plt.xticks([]), plt.yticks([])
    plt.show()

def show_nth_image(images,idx=0):
    plt.imshow(images[idx], cmap='gray')