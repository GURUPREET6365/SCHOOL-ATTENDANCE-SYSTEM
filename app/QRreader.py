import cv2
import requests
import winsound
import time


def opencv_camera():

   capture = cv2.VideoCapture(0)
   detector = cv2.QRCodeDetector()

   last_scan = 0
   last_secret = None
   while True:

      ret, frame = capture.read()

      if not ret or frame is None:
         continue

      qr_secret, bbox, _ = detector.detectAndDecode(frame)

      if (qr_secret and time.time() - last_scan > 3):

         last_scan = time.time()

         print("QR:", qr_secret)

         url = f"http://127.0.0.1:8000/api/mark/attendance/{qr_secret}"

         response = requests.get(url).json()
         print(type(response['success']))

         if response['success']:

            winsound.Beep(1200, 700) 
         
         else:
            winsound.Beep(1200, 1500) 

      cv2.imshow("Camera", frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
         break

   capture.release()
   cv2.destroyAllWindows()

   """
   When you do:

   cv2.imshow("Camera", frame)


   OpenCV creates its own window.

   When your loop ends, that window is STILL open in memory.

   So we must tell OpenCV:

   🧹 “Clean up everything.”

   That’s what this does.
   """

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