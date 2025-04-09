import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils #it is used to draw a lndmark points on image
mp_drawing_styles = mp.solutions.drawing_styles #it is used for custom colors thickness and line which can be further used 
mp_hand = mp.solutions.hands #this function is used for hand detection

cap = cv2.VideoCapture(0)
p = mp_hand.Hands(static_image_mode=True,max_num_hands=2,min_detection_confidence=0.5)#main function that capture hands with some % of confidence 
while True:
    r,frame = cap.read()
    if r == True:
        frame = cv2.resize(frame,(500,500))
        frame = cv2.flip(frame,1)
        img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)#converting CV2BGR TO RGB bcz Media pipeline accept only RGB
        final = p.process(img) #frame will be detected and saved in final.multi_hand_landmarks
        frame = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)#CONVERSION OF rgb2bgr fOR cv2 purpose
        if final.multi_hand_landmarks: #1st it will check the hands in frame
            for hand in final.multi_hand_landmarks: #if so then 
                mp_drawing.draw_landmarks(frame,hand,mp_hand.HAND_CONNECTIONS) #draw the landmarks on hand 
        
        cv2.imshow("Frame",frame)
        if cv2.waitKey(25) & 0xff==ord("p"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
