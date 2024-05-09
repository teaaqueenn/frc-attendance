import face_recognition
import cv2
import numpy as np

# Get a reference to webcam #0 (the default one)
cap = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
cadenWuImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\cadenwu.png")
cadenWuFaceCode = face_recognition.face_encodings(cadenWuImage)[0]

emmanuelImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\emmanuel.png")
emmanuelFaceCode = face_recognition.face_encodings(emmanuelImage)[0]

graceFillbachImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\gracefillbach.png")
graceFillbachFaceCode = face_recognition.face_encodings(graceFillbachImage)[0]

jasperWuImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\jasperwu.png")
jasperWuFaceCode = face_recognition.face_encodings(jasperWuImage)[0]

leannKanImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\leannkan.png")
leannKanFaceCode = face_recognition.face_encodings(leannKanImage)[0]

maxChengImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\maxcheng.png")
maxChengFaceCode = face_recognition.face_encodings(maxChengImage)[0]\

mollyChenImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\mollychen.png")
mollyChenFaceCode = face_recognition.face_encodings(mollyChenImage)[0]

stephenPengImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\stephenpeng.png")
stephenPengFaceCode = face_recognition.face_encodings(stephenPengImage)[0]



# Create arrays of known face encodings and their names
knownFaceCode = [
    cadenWuFaceCode,
    emmanuelFaceCode,
    graceFillbachFaceCode,
    jasperWuFaceCode,
    leannKanFaceCode,
    maxChengFaceCode,
    mollyChenFaceCode,
    stephenPengFaceCode
]
knownFaceNames = [
    "Caden Wu",
    "Emmanuel",
    "Grace Fillbach",
    "Jasper Wu",
    "Leann Kan",
    "Max Cheng ",
    "Molly Chen",
    "Stephen Peng"
]
cap = cv2.VideoCapture(0)

process_this_frame = True

while True:

    ret, frame = cap.read()
    

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(knownFaceCode, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(knownFaceCode, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = knownFaceNames[best_match_index]

        print(name)
    
    process_this_frame = not process_this_frame

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
