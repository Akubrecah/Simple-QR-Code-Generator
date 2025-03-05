import qrcode as qr
import os
from PIL import Image

qr = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://github.com/Akubrecah')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('qr.png')
    