import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, test_frame = cap.read()   # read one frame to get webcam size
background = cv2.imread("Background.jpg")

# Resize background to webcam frame size
if ret:
    background = cv2.resize(background, (test_frame.shape[1], test_frame.shape[0]))

while cap.isOpened():
    ret, current_frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)
        
        # lower red
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        
        # upper red
        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        
        red = mask1 + mask2
        red = cv2.morphologyEx(red, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=10)
        red = cv2.morphologyEx(red, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
        
        # Now both background and red have the same size ✅
        part1 = cv2.bitwise_and(background, background, mask=red)
        red_free = cv2.bitwise_not(red)
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=red_free)

        cv2.imshow("cloak", part1+part2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
