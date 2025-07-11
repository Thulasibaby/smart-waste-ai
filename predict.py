import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing import image

# Load trained model
model = load_model('model.h5')

# Load and preprocess image
img_path = 'test_image.jpg'  # replace with your test image
img = image.load_img(img_path, target_size=(64, 64))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Predict
pred = model.predict(img_array)
classes = ['Organic', 'Plastic', 'Metal', 'Paper', 'Other']
print("Predicted Waste Type:", classes[np.argmax(pred)])
