# MediaPipe_HandTracking
This code is a real-time hand tracking script using OpenCV and MediaPipe in Python.

1. OpenCV (cv2)
Purpose: To access the webcam, capture video frames, process images, and display results.

Key Functions Used:

cv2.VideoCapture() – to start video capture from webcam.

cv2.imshow() – to display the video frames.

cv2.cvtColor() – to convert image color spaces (e.g., BGR to RGB and vice versa).

cv2.flip() – to flip the frame horizontally.

cv2.resize() – to resize the video frame.

cv2.waitKey() – to wait for a key press to break the loop.

2. MediaPipe (mediapipe)
Purpose: Provides ML-powered pipelines for computer vision tasks such as hand tracking, pose detection, face mesh, etc.

Key Submodules Used:

mp.solutions.hands.Hands() – initializes the hand tracking solution.

mp.solutions.drawing_utils – used to draw landmarks.

mp.solutions.drawing_styles – for customizable drawing styles.

before Running the Code , install the neccessary Modules 
pip install opencv-python
pip install mediapipe
