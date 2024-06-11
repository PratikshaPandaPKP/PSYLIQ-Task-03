The provided task involved two components: MNIST Digit Classification using Keras and a Handwritten Digit Recognition GUI using Tkinter and Keras.

### MNIST Digit Classification Using Keras

1. **Data Preprocessing**:
   - The MNIST dataset was loaded.
   - Pixel values were reshaped and normalized.
   - Class vectors were converted to binary class matrices (one-hot encoding).

2. **Model Definition**:
   - A Sequential model was constructed with convolutional layers (Conv2D) and max pooling layers (MaxPooling2D).
   - The output was flattened, and fully connected layers (Dense) with dropout regularization were added.

3. **Compilation**:
   - The model was compiled using categorical cross-entropy loss, Adadelta optimizer, and accuracy metric.

4. **Training**:
   - The model was trained on the training data for 10 epochs with a batch size of 128.
   - Validation was performed on the test data after each epoch.

5. **Evaluation**:
   - The model was evaluated on the test data to obtain the loss and accuracy.
   - The test loss and accuracy were printed.

6. **Saving the Model**:
   - The trained model was saved as `mnist.h5`.

### Handwritten Digit Recognition GUI Using Tkinter and Keras

1. **Dependencies**:
   - Tkinter was utilized for GUI creation.
   - Necessary libraries for capturing and processing images were imported.

2. **Model Loading**:
   - The pre-trained CNN model (`mnist.h5`) was loaded using Keras.

3. **GUI Class Definition**:
   - The App class was defined, inheriting from Tkinter's Tk class.
   - Canvas, label, and buttons were set up for user interaction.

4. **Event Handling**:
   - Click events were handled to initiate digit classification and clear the canvas.
   - Drawn digits were captured, images were processed, and digits were predicted using the loaded model.
   - Lines were drawn on the canvas for capturing user input.

5. **Functionality**:
   - Users could draw digits on the canvas.
   - Drawn digits were recognized upon clicking the Recognize button.
   - The canvas was cleared upon clicking the Clear button.
   - The predicted digit was displayed on the GUI label.

This implementation offered an interactive interface for recognizing handwritten digits, leveraging a CNN model trained on the MNIST dataset.

**Project working:-**

Execute the Jupyter Notebook named "MNIST_DigitRecognition_UsingCNN.ipynb".

Save the weights obtained from the training process as "mnist.h5".

Utilize a graphical user interface to test the trained model by running the script named "main.py".

By following these steps, you will be able to run the provided Jupyter Notebook to train a Convolutional Neural Network (CNN) for recognizing digits from the MNIST dataset.

Video Link:- https://www.loom.com/share/aa29ad4b2642499ca6cb022efdd10b44?sid=40da3b8f-0b99-40bd-93b2-a6ed287f323f
