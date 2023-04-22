import pyqrcode
import png
from pyqrcode import QRCode

s=input("Enter Your Text : ")
name=input("Enter name for save : ")

url=pyqrcode.create(s)

url.png(str(name)+".png", scale=6)
print('Save QR')