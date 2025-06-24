from hand_tracker import HandTracker
from gesture_control import GestureController
import cv2

cap = cv2.VideoCapture(0)
tracker = HandTracker()
controller = GestureController()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    hand_data = tracker.process(img)
    img = controller.apply_controls(img, hand_data)

    cv2.imshow("NextGesture", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
