import cv2
import os
import numpy as np

#Turn a image into gray scale
def grayConversion(img):
    return gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




#Return a list of detected faces in the gray scale
def detectFace(img):
    #Convert image to gray scale
    gray = grayConversion(img)
    #load OpenCV face detector(LBP)
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    processed_faces = []
    if faces is not None:
        for (x,y,w,h) in faces:
            processed_faces.append(gray[y:y+w, x:x+h])
    return processed_faces


#Prepare training data from all persons' profile image folder
def prepareTrainingData(profile_data_folder_path):
    faces = []
    labels = []
    for folder_name in os.listdir(profile_data_folder_path):
        label = folder_name
        folder_path = profile_data_folder_path + "/" + folder_name
        image_names = os.listdir(folder_path)
         for image_name in image_names:
             #Ignore system files
            if image_name.startwith("."):
                continue;
                image_path = profile_data_folder_path + "/" + image_name
                image = cv2.imread(image_path)
                face = detectFace(image)
                if face is not None:
                    faces.append(face)
                    labels.append(label)
     return faces, labels
face_recognzer = cv2.face.createLBPHFaceRecognzer()

#Train recognizer
def trainRecognizer(profile_data_folder_path):
    faces, labels = prepareTrainingData(profile_data_folder_path)
    face_recognizer.train(faces, np.array(labels))


#Matching function. Return a list of matched labels.
def match(input_image):
    face = detectFace(input_image)
    label = face_recognizer.predict(face)
    return label


