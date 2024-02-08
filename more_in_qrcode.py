import qrcode
from PIL import Image
qr = qrcode.QRCode(version = 1,error_correction = qrcode.ERROR_CORRECT_H,box_size = 10,border = 20)

qr.add_data ("https://www.google.com/index.html")
qr.make(fit= True)
img = qr.make_image(fill_color = "white",back_color = "blue")
img.save ("google.png")