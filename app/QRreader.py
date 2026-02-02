import cv2
import requests
import time
import pygame
import threading
import time
import os

# print(os.getcwd())

pygame.mixer.init()

can_play = True

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def play_async(file):
    threading.Thread(target=play_sound, args=(file,)).start()

def opencv_camera():

    capture = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    last_scan = 0   # timestamp cooldown

    while True:

        ret, frame = capture.read()

        if not ret or frame is None:
            continue

        qr_secret, bbox, _ = detector.detectAndDecode(frame)

        # QR detected + 3 second cooldown
        if qr_secret and (time.time() - last_scan > 3):

            last_scan = time.time()   # cooldown starts IMMEDIATELY

            # print("QR:", qr_secret)

            url = f"http://127.0.0.1:8000/api/mark/attendance/{qr_secret}"
            response = requests.get(url).json()

            # stop any previous audio
            pygame.mixer.music.stop()

            if response.get('success') and response.get('entry'):
               play_async("app/sounds/you_may_now_enter.mp3")

            elif response.get('success') and response.get('exit'):
               play_async("app/sounds/you_may_now_exit.mp3")

            else:
               play_async("app/sounds/access_denied.mp3")

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


opencv_camera()


"""

def qr_Reader():
    # Load image
    img = cv2.imread("trial-qr-code.png")

    detector = cv2.QRCodeDetector()

    # Detect and decode
    data = detector.detectAndDecode(img)


    data = detector.detectAndDecode(img)
    This data contains below data which is in tuple.
    The detector.detectAndDecode() returns tuple


    QR Code data: ('Phdj23xdDKAJl', 
        above is qr code data.

        array([[[ 48.   ,  48.   ],
        [298.992,  48.   ],
        [301.   , 299.   ],
        [ 48.   , 299.   ]]], dtype=float32), 
        above is position of the qr code on screen


       array([[  0,   0,   0,   0,   0,   0,   0, 255,   0, 255,   0, 255, 255,
       255,   0,   0,   0,   0,   0,   0,   0],
       [  0, 255, 255, 255, 255, 255,   0, 255,   0, 255, 255, 255, 255,
        255,   0, 255, 255, 255, 255, 255,   0],
       [  0, 255,   0,   0,   0, 255,   0, 255,   0,   0,   0,   0,   0,
        255,   0, 255,   0,   0,   0, 255,   0],
       [  0, 255,   0,   0,   0, 255,   0, 255, 255,   0, 255, 255,   0,
        255,   0, 255,   0,   0,   0, 255,   0],
       [  0, 255,   0,   0,   0, 255,   0, 255,   0,   0, 255,   0,   0,
        255,   0, 255,   0,   0,   0, 255,   0],
       [  0, 255, 255, 255, 255, 255,   0, 255, 255,   0, 255,   0,   0,
        255,   0, 255, 255, 255, 255, 255,   0],
       [  0,   0,   0,   0,   0,   0,   0, 255,   0, 255,   0, 255,   0,
        255,   0,   0,   0,   0,   0,   0,   0],
       [255, 255, 255, 255, 255, 255, 255, 255, 255,   0,   0, 255,   0,
        255, 255, 255, 255, 255, 255, 255, 255],
       [  0, 255, 255,   0,   0,   0,   0,   0,   0,   0, 255, 255,   0,
          0, 255, 255,   0, 255,   0,   0,   0],
       [  0, 255,   0,   0, 255,   0, 255, 255,   0, 255,   0, 255,   0,
          0,   0, 255, 255, 255, 255, 255, 255],
       [255, 255, 255, 255,   0, 255,   0, 255,   0,   0,   0,   0,   0,
        255,   0, 255, 255,   0,   0,   0,   0],
       [255,   0, 255, 255,   0, 255, 255, 255, 255,   0, 255,   0,   0,
          0, 255, 255,   0, 255,   0, 255, 255],
       [255, 255,   0,   0, 255,   0,   0,   0, 255,   0,   0, 255, 255,
          0,   0,   0, 255,   0, 255,   0,   0],
       [255, 255, 255, 255, 255, 255, 255, 255,   0,   0, 255, 255, 255,
        255,   0,   0,   0,   0,   0, 255,   0],
       [  0,   0,   0,   0,   0,   0,   0, 255,   0,   0, 255,   0,   0,
          0, 255, 255,   0, 255,   0, 255, 255],
       [  0, 255, 255, 255, 255, 255,   0, 255,   0, 255, 255, 255, 255,
          0,   0,   0, 255,   0,   0,   0,   0],
       [  0, 255,   0,   0,   0, 255,   0, 255,   0, 255,   0,   0, 255,
        255,   0,   0, 255,   0, 255,   0, 255],
       [  0, 255,   0,   0,   0, 255,   0, 255,   0,   0, 255,   0,   0,
        255,   0,   0, 255,   0, 255, 255, 255],
       [  0, 255,   0,   0,   0, 255,   0, 255, 255,   0, 255, 255,   0,
        255, 255,   0,   0,   0, 255,   0,   0],
       [  0, 255, 255, 255, 255, 255,   0, 255, 255,   0,   0,   0,   0,
        255,   0, 255,   0, 255,   0,   0,   0],
       [  0,   0,   0,   0,   0,   0,   0, 255,   0, 255,   0, 255,   0,
          0, 255,   0,   0,   0, 255, 255, 255]], dtype=uint8))
        above is the matrix of of the black and white color of qr code where 0==black and 255 == white

    print(location)
    print('here are the division')
    print(bandlmatrix)


    You can also do it with indexing as we do in list.

    
    if data:
        print("QR Code data:", data[0])
    else:
        print("No QR code found")


"""