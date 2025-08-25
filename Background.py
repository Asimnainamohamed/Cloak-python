import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,background = cap.read()
    if ret:
        cv2.imshow("Background",background)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("Background.jpg",background)
            break
cap.release()
cv2.destroyAllWindows()