import os
from google.cloud import vision
import io

# Set path to your JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "visual-search-project-464117-f86d643c717b.json"  # <-- Replace

def detect_labels_local(image_path):
    client = vision.ImageAnnotatorClient()
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    results = []
    for label in labels[:5]:
        results.append((label.description, round(label.score * 100, 2)))
    return results
