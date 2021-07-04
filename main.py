import qrcode

#qr = qrcode.make('hello world')
#qr.save('myQR.png')

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = 'https://www.youtube.com/watch?v=Fc-fa6cAe2c'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('Kai Mmmh QR Code.png')
