from flask import Flask, render_template, request
import os
from utils.image_processing import process_image
from utils.vision_api import detect_labels_local
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    info = [
        ("Google Lens", "Real-time object, text, plant & animal identification."),
        ("Pinterest Lens", "Visual search with 'Shop the Look' & related ideas."), 
        ("CamFind", "Image recognition + shopping results via CloudSight API.")
    ]
    return render_template('about.html', info=info)



@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded'
    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath) 
    results = process_image(filepath)  # You will define this
    return render_template('result.html', image=file.filename, result=results)

if __name__ == '__main__':
    app.run(debug=True)
