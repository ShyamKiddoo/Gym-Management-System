import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
# To capture video from webcam. 
#cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture('SSNGym.mp4')

while True:
    # Read the frame
    ret,frame=cap.read()
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=10, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    #detect eyes
    #eyes = eye_cascade.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 4)
    # Draw the rectangle around each face

    #for (x, y, w, h) in eyes:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    img=cv2.putText(img,"Number of faces detected :"+str(len(faces)),(50,40),font,1,(0,0,255),2)
    if len(faces)==0:
        cv2.putText(img,"Gym Equipment is free for usage",(50,80),font,1,(255,0,0),2)
    cv2.imshow("Frame",img)
    # Display
     
    #n=str(len(faces))
    #cv2.imshow("Eyes Detected", img)
    
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
