from tensorflow.keras.applications import mobilenet_v2
from tensorflow.keras.preprocessing import image
import numpy as np

def process_image(filepath):
    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = mobilenet_v2.preprocess_input(x)
    model = mobilenet_v2.MobileNetV2(weights='imagenet')
    preds = model.predict(x)
    decoded = mobilenet_v2.decode_predictions(preds, top=3)[0]
    return [(i[1], float(i[2])) for i in decoded]
