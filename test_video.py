import cv2
import os

path = r"backend\datasets\traffic_sample.mp4"

print("FILE EXISTS:", os.path.exists(path))

video = cv2.VideoCapture(path)

print("VIDEO OPENED:", video.isOpened())

while True:

    success, frame = video.read()

    print(success)

    if not success:
        print("FAILED TO READ FRAME")
        break

    cv2.imshow("Traffic Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()