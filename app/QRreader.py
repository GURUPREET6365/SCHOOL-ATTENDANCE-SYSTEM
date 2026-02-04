import cv2
import requests
import time
import pygame
import threading
import time
from datetime import datetime
from rich.live import Live
from rich.table import Table

# print(os.getcwd())

pygame.mixer.init()

can_play = True

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def play_async(file):
    threading.Thread(target=play_sound, args=(file,)).start()

# Creating the data json
data = {
        "id": "",
        "name": "",
        "entry_time": "",
        "exit_time": ""
    }

# This will be initialized first then created the table and will update it.
def generate_table() -> Table:

    table = Table(
        title="[bold cyan]📡 Smart Attendance Scanner[/bold cyan]",
        show_header=True,
        header_style="bold white on blue",
        border_style="bright_blue"
    )

    table.add_column("ID", style="yellow", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Entry Time", style="cyan")
    table.add_column("Exit Time", style="magenta")
    table.add_column("Date", style="white")

    table.add_row(
        f"[bold yellow]{data['id']}[/bold yellow]",
        f"[bold green]{data['name']}[/bold green]",
        f"[cyan]{data['entry_time']}[/cyan]",
        f"[magenta]{data['exit_time']}[/magenta]",
        f"[white]{datetime.now().date()}[/white]"
    )

    return table


def opencv_camera():
   print("Welcome to my smart attendance system where you can mark your presence with accurate timings and also can see your records.")
   capture = cv2.VideoCapture(0)
   detector = cv2.QRCodeDetector()
   
   last_scan = 0   # timestamp cooldown
   with Live(generate_table(), refresh_per_second=4) as live:
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
               
               # Creating a data model so that the data can be stored safely.

               # stop any previous audio
               pygame.mixer.music.stop()

               if response.get('success'):
                  # Here we are updating the data dynamically.
                  data["id"] = str(response.get("id"))
                  data["name"] = response.get("name")
                  data["entry_time"] = str(response.get("entry_time"))
                  data["exit_time"] = str(response.get("exit_time"))

                  live.update(generate_table())

                  if response.get('entry'):
                     play_async("app/sounds/you_may_now_enter.mp3")

                  elif response.get('exit'):
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