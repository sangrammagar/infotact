# Minimal ConvLSTM training skeleton (TensorFlow)
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import ConvLSTM2D, Conv3D, BatchNormalization

def build_convlstm(input_shape):
    model = Sequential()
    model.add(ConvLSTM2D(filters=16, kernel_size=(3,3), input_shape=input_shape, padding='same', return_sequences=True))
    model.add(BatchNormalization())
    model.add(ConvLSTM2D(filters=8, kernel_size=(3,3), padding='same', return_sequences=False))
    model.add(BatchNormalization())
    model.add(Conv3D(filters=1, kernel_size=(3,3,3), activation='sigmoid', padding='same'))
    model.compile(optimizer='adam', loss='binary_crossentropy')
    return model

if __name__ == '__main__':
    # input_shape = (timesteps, rows, cols, channels)
    input_shape = (3, 64, 64, 1)
    model = build_convlstm(input_shape)
    model.summary()
