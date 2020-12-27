from flask import Flask,render_template,request
import requests
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
from numpy import mean
from numpy import std
from matplotlib import pyplot
from sklearn.model_selection import KFold
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt



#from temp import action

app = Flask(__name__)
#we make the instance of clss flask in app

#action = action()
#x = action[0]


@app.route('/')
def index():
    #you can write any name to that function
    return render_template('home.html')


@app.route('/about')
def about():
    return x


@app.route('/pixel_array', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        #print(request.get_json()['array'])
        #print(request.get_json().shape)
        pixel_array = request.get_json()['array'] # parse as JSON
        #array = np.zeros([280,280,3], dtype=np.uint8)
        temp = np.array((1,) , dtype=np.uint8)
        arr = np.append(temp , pixel_array)
        g = np.delete(arr , 0);
        new = g.reshape(280 , 280)
        #print(new.shape)
        #new = im.reshape(280, 280) #let M and N be the dimensions of your image
        im = Image.fromarray(np.uint8(new))
        #im = Image.open(r"testgrey.png")
        im = im.resize((28 , 28))
        im.save('testgrey.png')
        #im.show()

        #request.environ.setdefault('log_context', dict())
        #request.environ['log_context']['error'] = error.__class__.__name__
        model = load_model('final_model.h5')
        img = load_img('testgrey.png',color_mode = "grayscale", target_size=(28, 28))
        # convert to array
        img = img_to_array(img)

        #reshape into a single sample with 1 channel
        img = img.reshape(1, 28, 28, 1)
        # prepare pixel data
        img = img.astype('float32')
        img = img / 255.0


        digit  = np.argmax(model.predict(img), axis=-1)
        print(digit[0])


        return str(digit[0]) , 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers





if __name__ == '__main__':
    app.run(debug=True)
#Put simply, __name__ is a variable defined for each script that defines whether the script is being run as the main module or it is being run as an imported module.
