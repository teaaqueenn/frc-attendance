import face_recognition
import cv2
import numpy as np
import datetime
import socket

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

drBayImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\drbay.jpg")
drBayFaceCode = face_recognition.face_encodings(drBayImage)[0]

mrFagenImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\stephenpeng.png")
mrFagenFaceCode = face_recognition.face_encodings(mrFagenImage)[0]

mrPatelImage = face_recognition.load_image_file(r"C:\Users\27GracieF\Documents\GitHub\frc-attendance\practicePhotos\stephenpeng.png")
mrPatelFaceCode = face_recognition.face_encodings(mrPatelImage)[0]

# Create arrays of known face encodings and their names
knownFaceCode = [
    cadenWuFaceCode,
    emmanuelFaceCode,
    graceFillbachFaceCode,
    jasperWuFaceCode,
    leannKanFaceCode,
    maxChengFaceCode,
    mollyChenFaceCode,
    stephenPengFaceCode,
    drBayFaceCode,
    mrFagenFaceCode,
    mrPatelFaceCode
]
knownFaceNames = [
    "Caden Wu",
    "Emmanuel",
    "Grace Fillbach",
    "Jasper Wu",
    "Leann Kan",
    "Max Cheng ",
    "Molly Chen",
    "Stephen Peng",
    "Dr. Bay",
    "Mr. Fagen",
    "Mr. Patel"
]

cap = cv2.VideoCapture(0)

print("[INFO] Creating Server...")

# Create a socket object
s = socket.socket()

# Set up the ESP32-CAM connection
esp32_cam_ip = "192.168.1.100"  # Replace with your ESP32-CAM's IP address
esp32_cam_port = 8080
s.connect((esp32_cam_ip, esp32_cam_port))

print("[INFO] Server Created.")

detectedNames = set()

process_this_frame = True

while True:
    ret, frame = cap.read()

    # Detect face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        if(process_this_frame):
            # Initialize name and confidence score
            name = "Unknown"
            confidence_score = 0
            
            # Compare the face encoding with known face encodings
            matches = face_recognition.compare_faces(knownFaceCode, face_encoding)
            face_distances = face_recognition.face_distance(knownFaceCode, face_encoding)

            # Find the best match
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = knownFaceNames[best_match_index]
                # Calculate the confidence score
                confidence_score = 1 - face_distances[best_match_index]

            confidence_score *= 100

            # Send the detection result to the ESP32-CAM
            message = f"*{name}'s face has been detected at {datetime.datetime.now()}*"
            s.send(message.encode())

            # Print name and confidence scorex`x`
            print(f"Name: {name}, Confidence Score: {confidence_score}")

            if confidence_score > 61 and name not in detectedNames:
                # Write name and current date to text file
                with open("detectedNames.txt", "a") as file:
                    file.write(f"{name} - {datetime.datetime.now()}\n")
                # Add name to detected names set
                detectedNames.add(name)

            # Draw rectangle around the face and display name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, f"{name} ({confidence_score:.2f})", (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    
    process_this_frame = not process_this_frame

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()