from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
from flask_ngrok import run_with_ngrok
from flask import Flask
from PIL import Image
from flask import request
import cv2
import os
app = Flask(__name__)
UPLOAD_FOLDER = './upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
run_with_ngrok(app)
# draw each face separately
def draw_faces(filename, result_list):
# load the image
    data = pyplot.imread(filename)
# plot each face as a subplot
    t=0
    for i in range(len(result_list)):
# get coordinate
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
# define subplot
        cv2.imwrite('/content/resultmtcnn1/{}.jpg'.format(t), data[y1:y2, x1:x2])
        '''pyplot.subplot(1, len(result_list), i+1)
        pyplot.axis('off')
# plot face
        pyplot.imshow(data[y1:y2, x1:x2])
# show the plot
        pyplot.show()'''
        t=t+1
@app.route("/" , methods=["GET","POST"])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'there is no file in form!'
        file1 = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        pixels = pyplot.imread(path)
        detector = MTCNN()
        faces = detector.detect_faces(pixels)
        draw_faces(path, faces)
        return path

        return 'ok'
    return '''
    <form method="post" enctype="multipart/form-data">
      <p>Test upload field that open device's camera.</p>
<input type="file" name="file" accept="image/*" capture="camera" />
<input type="submit">
    </form>
    '''
  
app.run()
