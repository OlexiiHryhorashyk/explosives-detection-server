from flask import Flask, request, render_template, send_file, Response
from werkzeug.utils import secure_filename
from flasgger import Swagger, swag_from
import io

import numpy as np
from PIL import Image
import cv2
import os
from swagger import image_endpoint_form, video_endpoint_form
from detection import YoloDetection, gen_frames

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'
app.config['SWAGGER'] = {
    'title': "Explosives Detection Server",
    'uiversion': 3,
    'version': "0.0.1",
    'description': "Server that detects explosives of images and in video feed"
}
swagger = Swagger(app)  # Initialize Flasgger
detector = YoloDetection(model_name="exp_yolo.pt")


@app.route('/')
def index():
    return render_template('image.html')


@app.route('/video')
def index_video():
    return render_template('video.html')


@app.route('/image-detection', methods=['POST'])
@swag_from(image_endpoint_form)
def apply_detection():
    """Endpoint for uploading an image and detect explosives on them"""
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        img = Image.open(file_path).convert("RGB")
        img = np.array(img)
        img = cv2.resize(img, (512, 512))
        img = detector.detect_from_image(img)
        output = Image.fromarray(img)

        buf = io.BytesIO()
        output.save(buf, format="PNG")
        buf.seek(0)

        os.remove(file_path)
        return send_file(buf, mimetype='image/png')

@app.route('/video-feed', methods=["GET"])
@swag_from(video_endpoint_form)
def video_feed():
    """Endpoint for real time explosives detection"""
    return Response(gen_frames(detector), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
