import mediapipe as mp
import cv2
from google.protobuf.json_format import MessageToDict

class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.75)
        self.mpDraw = mp.solutions.drawing_utils

    def process(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        
        left, right = [], []
        handedness = results.multi_handedness
        landmarks = results.multi_hand_landmarks

        if handedness and landmarks:
            for i, hand in enumerate(handedness):
                label = MessageToDict(hand)['classification'][0]['label']
                lmList = []
                for lm in landmarks[i].landmark:
                    h, w, _ = img.shape
                    lmList.append([int(lm.x * w), int(lm.y * h)])
                if label == 'Left':
                    left = lmList
                elif label == 'Right':
                    right = lmList
                self.mpDraw.draw_landmarks(img, landmarks[i], self.mpHands.HAND_CONNECTIONS)
        return {'img': img, 'left': left, 'right': right}
