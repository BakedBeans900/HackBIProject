import cv2
import os
import numpy as np

subject = ["Nicholas_Cage", "Jacksfilms"]



#Return a list of detected faces in the gray scale
def detectFace(folder_path, img):
    #Convert image to gray scale
    os.chdir(folder_path)
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    gray = np.array(image, 'uint8')
    #load OpenCV face detector(LBP)
    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml')
    faces = face_cascade.detectMultiScale(gray);
    processed_faces = []
    if faces is not None:
        for (x,y,w,h) in faces:
            processed_faces.append(gray[y:y+w, x:x+h])
    return processed_faces


#Prepare training data from all persons' profile image folder
def prepareTrainingData(profile_data_folder_path):
    faces = []
    labels = []
    os.chdir(profile_data_folder_path)
    for folder_name in os.listdir(profile_data_folder_path):
        os.chdir(profile_data_folder_path + "/" + folder_name)
        label = int(folder_name)
        folder_path = profile_data_folder_path + "/" + folder_name
        image_names = os.listdir(folder_path)
        for image_name in image_names:
            #Ignore system files
            if not image_name.startswith("."):
                os.chdir(folder_path)
                face = detectFace(folder_path, image_name)
                temp = np.array(face, 'uint8')
                if face is not None:
                    faces.append(temp[0])
                    labels.append(label)
    os.chdir('..')
    return faces, labels

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#Train recognizer
def trainRecognizer(profile_data_folder_path):
    faces, labels = prepareTrainingData(profile_data_folder_path)
    for item in faces:
        item = np.array(item, 'uint8')
    face_recognizer.train(faces, np.array(labels))


#Matching function. Return a list of matched labels
def match(directory, input_image):
        face = detectFace(directory, input_image)
        label = face_recognizer.predict(face[0])
        return label
