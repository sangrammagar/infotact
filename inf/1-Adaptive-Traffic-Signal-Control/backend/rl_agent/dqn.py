# Simple DQN network using TensorFlow Keras (starter)
import numpy as np
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Input

def build_dqn(state_dim, action_dim, lr=1e-3):
    inputs = Input(shape=(state_dim,))
    x = Dense(64, activation='relu')(inputs)
    x = Dense(64, activation='relu')(x)
    outputs = Dense(action_dim, activation='linear')(x)
    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mse')
    return model

if __name__ == '__main__':
    model = build_dqn(5, 2)
    print(model.summary())
