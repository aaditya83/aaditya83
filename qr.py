import qrcode as qr

q=qr.QRCode(version=10,box_size=100,border=5)
q.add_data("https://www.google.com")
q.make(fit=True)
img=q.make_image(fill_color="red",back_color="white")
img.show()
print("QR Code Generated Successfully")
