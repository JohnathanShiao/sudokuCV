import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Activation, Flatten, Dense, Dropout

class sudokunet:
    @staticmethod
    def build(width,height,depth,classes):
        #initialize the model
        model = Sequential()
        inputShape = (height,width,depth)

        #first set of CONV=>RELU=>POOL
        model.add(Conv2D(32, (5,5), padding="same",input_shape=inputShape))
        model.add(Activation ("relu"))
        model.add(MaxPooling2D(pool_size=(2,2)))

        #second set of CONV=>RELU=>POOL
        model.add(Conv2D(32, (3,3), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2)))

        #first set of FC=>RELU
        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))

        #second set of FC=>RELU
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))

        #softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        #return the constructed architecture
        return model