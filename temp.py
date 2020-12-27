





                        (trainX, trainY), (testX, testY) = tf.keras.datasets.mnist.load_data()
                        # reshape dataset to have a single channel

                        trainX = trainX.reshape((trainX.shape[0],28,28,1))
                        testX = testX.reshape((testX.shape[0],28,28,1))

                        # one hot encode target values
                        trainY = to_categorical(trainY)
                        testY = to_categorical(testY)


                        trainX = trainX.astype('float32')
                        testX = testX.astype('float32')

                        trainX = trainX / 255.0
                        testY = testY / 255.0


                        model = Sequential()
                        model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
                        model.add(MaxPooling2D((2, 2)))
                        model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
                        model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
                        model.add(MaxPooling2D((2, 2)))
                        model.add(Flatten())
                        model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
                        model.add(Dense(10, activation='softmax'))
                        # compile model
                        opt = SGD(lr=0.01, momentum=0.9)
                        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])


                        history = model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY), verbose=0)
                        # evaluate model
                        _,acc = model.evaluate(testX, testY, verbose=0)
                        print(acc);




                        model.save('final_model.h5')
