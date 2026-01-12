## QR Code Generator in Python

import pyqrcode 
import png 
from pyqrcode import QRCode 

# s = "https://rai-deepak-07.github.io/raideepak07/"
complete_url = input("Enter the URL or text to generate QR Code: ")

url = pyqrcode.create(complete_url) 

format_choice = input("Enter the format to save the QR Code (svg/png): ").strip().lower()

if format_choice == 'svg':
    url.svg("qrcode.svg", scale = 8)
    print("QR Code saved as qrcode.svg")
elif format_choice == 'png':
    url.png('qrcode.png', scale = 6)
    print("QR Code saved as qrcode.png")
else:
    print("Invalid format choice. Please choose 'svg' or 'png'.")