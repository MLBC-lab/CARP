import argparse
import tensorflow as tf
import cv2
import numpy as np

def main(args):

    model_path = '_cnn.h5'
    
    model = tf.keras.models.load_model(model_path)

    img = cv2.imread(args.file_path)
    img = img/255

    resize = tf.image.resize(img, (256,256))
    pred = model.predict(np.expand_dims(resize/255, 0))

    if pred>0.5:
        print('Cranberry is sound')
    else:
        print('Cranberry is rotten')


if __name__ == '__main__':
    ######################
    # Adding Arguments
    #####################

    p = argparse.ArgumentParser(description='Cranberry Assessment for Rot Prediction')

    p.add_argument('-fp', '--file_path', type=str, help='~/file_name.png', default='test_data/rot/5.png')

    args = p.parse_args()

    main(args)