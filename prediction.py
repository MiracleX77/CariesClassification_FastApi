from PIL import Image
from io import BytesIO
import tensorflow as tf
import numpy as np



input_shape = (224, 224, 3)
input_shape2 = (224, 224)
decode_predictions = tf.keras.applications.imagenet_utils.decode_predictions
def load_model():
    model = tf.keras.applications.MobileNetV2(input_shape)
    return model

_model = load_model()



def read_image(image_encoded):
    image_encoded = image_encoded.file.read()
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image

def preprocess(image: Image.Image):
    image = image.resize(input_shape2)
    image = np.asfarray(image)
    image = image / 127.5 -1.0
    image = np.expand_dims(image, axis=0)
    return image



def predict(image: np.ndarray):
    predictions = _model.predict(image)
    predictions = decode_predictions(predictions, top=3)[0]
    return predictions