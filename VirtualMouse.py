import cv2
import numpy as np
import pyautogui
import time
import HandTrackingModule as htm
import math

# ======================
# Setup
# ======================
wCam, hCam = 640, 480
frameR = 100
smoothening = 7

plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector(maxHands=1)
screen_w, screen_h = pyautogui.size()

# ======================
# Main Loop
# ======================
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=True)

    if len(lmList) != 0:
        # Get finger tips
        x_index, y_index = lmList[8][1:]   # Index tip
        x_middle, y_middle = lmList[12][1:]  # Middle tip
        x_thumb, y_thumb = lmList[4][1:]   # Thumb tip

        # Detect distances
        distance_index_thumb = math.hypot(x_index - x_thumb, y_index - y_thumb)
        distance_middle_thumb = math.hypot(x_middle - x_thumb, y_middle - y_thumb)

        # Move Mouse with Index Finger
        x3 = np.interp(x_index, (frameR, wCam - frameR), (0, screen_w))
        y3 = np.interp(y_index, (frameR, hCam - frameR), (0, screen_h))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening
        pyautogui.moveTo(clocX, clocY)
        plocX, plocY = clocX, clocY

        # Left Click - Pinch (Index + Thumb)
        if distance_index_thumb < 30:
            pyautogui.click()
            time.sleep(0.3)

        # Right Click - Pinch (Middle + Thumb)
        elif distance_middle_thumb < 30:
            pyautogui.rightClick()
            time.sleep(0.3)

        # Scroll - Drag with (Middle + Thumb)
        elif distance_middle_thumb < 50:
            scroll_amount = int((y_middle - y_thumb) / 2)
            pyautogui.scroll(-scroll_amount)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
