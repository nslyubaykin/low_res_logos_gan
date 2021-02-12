import pickle
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


IMG_HW=256


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
    
def norm_abs_one(image):
    image = tf.math.subtract(tf.math.multiply(image, 2), 1)
    image = tf.math.minimum(image, tf.ones(tf.shape(image)[-1]))
    image = tf.math.maximum(image, -tf.ones(tf.shape(image)[-1]))
    return image

def parse_image(image_filename, image_class, img_hw=IMG_HW, preprocess=True):
    image = tf.io.read_file(image_filename)
    image = tf.image.decode_jpeg(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    if tf.shape(image)[-1] == 1:
        image = tf.image.grayscale_to_rgb(image)
    image = tf.image.resize(image, [img_hw, img_hw])
    image = tf.reshape(image, [img_hw, img_hw, 3])
    if preprocess:
        image = norm_abs_one(image)
    return image, image_class

def parse_image_autoenc(image_filename, img_hw=IMG_HW):
    image = tf.io.read_file(image_filename)
    image = tf.image.decode_jpeg(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    if tf.shape(image)[-1] == 1:
        image = tf.image.grayscale_to_rgb(image)
    image = tf.image.resize(image, [img_hw, img_hw])
    image = tf.reshape(image, [img_hw, img_hw, 3])
    image = norm_abs_one(image)
    return image, image

def read_image_batch(album_dirs, img_hw=IMG_HW, preprocess=True):
    image_batch = []
    for dir_i in album_dirs:
        image_batch.append(parse_image(dir_i, None, img_hw, preprocess=preprocess)[0][tf.newaxis, :, :, :])
    image_batch = tf.concat(image_batch, axis=0)
    return image_batch

def show(image):
    plt.figure()
    plt.imshow(image.numpy())
    plt.axis('off')
    
def show_tf_batch(tf_batch, imtype='rgb', n_img=25, to_print=None):
    images = tf_batch.numpy()
    sqrtn = int(np.ceil(np.sqrt(n_img)))
    # select subset
    images = images[:n_img]
    # set grid
    fig = plt.figure(figsize=(sqrtn, sqrtn))
    gs = gridspec.GridSpec(sqrtn, sqrtn)
    gs.update(wspace=0.05, hspace=0.05)
    
    for i, img in enumerate(images):
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')        
        if imtype == 'rgb':
            plt.imshow(img)
        else:
            plt.imshow(img[:, :, 0], cmap='gray')
    if to_print is not None:
        print(to_print)
    return
