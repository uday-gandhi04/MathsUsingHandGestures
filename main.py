import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import Image

import google.generativeai as genai
apikey="AIzaSyCL8LgznpEVRqIoj0aUvCBanLVJv9FHPNQ"
genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList = hand1["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand1)
        print(fingers)

        return fingers, lmList
    
    return None

def draw(info,prev_pos,canvas):

    fingers, lmList=info
    curr_pos=None

    if fingers==[0,1,0,0,0]:
        curr_pos=lmList[8][0:2]
        if prev_pos==None: prev_pos=curr_pos
        cv2.line(canvas,curr_pos,prev_pos,(255,0,255),10)
    elif fingers==[1,1,1,1,1]:
        canvas=np.zeros_like(img)

    return curr_pos,canvas

def sendToAi(model,canvas,fingers):
    if(fingers==[1,0,0,0,1]):
        pil_img=Image.fromarray(canvas)
        response = model.generate_content(["solve this maths problem",pil_img])
        print(response.text)



prev_pos=None
canvas=None
combined_img=None
# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img=cv2.flip(img,1)
    
    
    if canvas is None:
        canvas=np.zeros_like(img)
        combined_img=img.copy()

    info=getHandInfo(img)

    if info:
        fingers, lmList = info
        print(fingers)

        prev_pos,canvas=draw(info,prev_pos,canvas)
        sendToAi(model,canvas,fingers)

    combined_img=cv2.addWeighted(img,0.7,canvas,0.3,0)

    # Display the image in a window
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    cv2.imshow("Combined", combined_img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)
