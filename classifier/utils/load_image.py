import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input


def load_image(path, label=None, image_size=(512, 512)):
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, image_size)
    img = preprocess_input(img)

    return (img, label) if label is not None else img
