import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_img = draw_bbox(frame, bbox, label, conf)
    
    cv2.imshow("Deteksi Object", output_img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break