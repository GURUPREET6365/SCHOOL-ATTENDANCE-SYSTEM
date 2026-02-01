import segno
"""
This is the library used for creating the qr code.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
"""
This is the base directory i created so that i can move on.
"""


def gen_QR_code(token:str, standard:int, streamORsection:str, student_id:int):
    # Generating qr code and storing into qr-code.
    # error is used to make the qr more reliable and able to scan even when damaged or get rubbed.
    # print('making the folder path...')
    folder = BASE_DIR/'StudentQRcode'/f'class-{standard}'/f'streamORsection-{streamORsection}'/f'{student_id}'

    print('making the path')
    folder.mkdir(parents=True, exist_ok=True)
    # parents=True is used for creating the missing folder.

    qrcode = segno.make(f'{token}', micro=False, error='h')
    # Saving the qr code.
    qrcode.save(f'{folder}/{student_id}.png', scale=12,
    border=4,
    dark="black",
    light="white")

    print(f'{folder}/{student_id}.png')

    return f'{folder}/{student_id}.png'


# gen_QR_code()
# qr_Reader()


