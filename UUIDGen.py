import uuid
import qrcode
import os

names = ['Alpha', 'Beta', 'Gamma']

if os.path.exists('signin.txt') is not True:
    for student in names:
        id = uuid.uuid4()
        f = open('signin.txt', 'a')
        f.write(f"{student}: {id}\n")
        values = str(id)
        qr_image = qrcode.make(values)
        qr_image.save(f"{student}.png")
else:
    print("Data Already Exists!")
