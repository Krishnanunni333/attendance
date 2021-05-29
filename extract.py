from mtcnn.mtcnn import MTCNN
import cv2
import os
from matplotlib import pyplot
from keras.models import load_model
import pandas as pd
import numpy as np
from datetime import datetime
model=load_model('/home/aryan/Downloads/faceDetector.h5')


detector = MTCNN()

def predict_faces():
    d={0:'Akshay', 1:'Alvin',  2:'Amaldeep',  3:'Arjun', 4:'Aryan' ,  5:'Prapanch'}
    pred_list=[]
    for i in os.listdir('./faces/'):
        face=cv2.imread('./faces/'+i)
        if type(face) is np.ndarray:
            face=cv2.resize(face,(224,224))
            #face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
            im=face
            #im=Image.fromarray(face,'RGB')
            img_array=np.array(im)/255
            img_array=np.expand_dims(img_array,axis=0)
            pred=model.predict(img_array)
            print(pred)
            #label = decode_predictions(pred)
            #label = label[0][0]
            # print the classification
            #print('%s (%.2f%%)' % (label[1], label[2]*100))
            classes=np.argmax(pred,axis=1)
            print(d[classes[0]])
            k=[d[classes[0]]]
            pred_list.append(k)
    return pred_list
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
        cv2.imwrite('./faces/{}.jpg'.format(t), data[y1:y2, x1:x2])
        t=t+1
    pred_list = predict_faces()
    
    return pred_list



def home(path):
    pixels = pyplot.imread(path)
    global detector
    faces = detector.detect_faces(pixels)
    pred_list = draw_faces(path, faces)
    return pred_list
  
def fetch(branch, classs):
    name = branch+classs+".csv"
    df = pd.read_csv(name)
    return [i for i in df['names']]
    
def final_save(final, branch, classs, code):
    d = {'names': final}
    df = pd.DataFrame(d) 
    name = "./FINAL/"+branch+"/"+classs+"/"+code+"/"+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.csv'
    df.to_csv(name)
