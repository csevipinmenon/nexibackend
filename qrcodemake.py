import qrcode
qr_imgr=qrcode.make('https://beneficiary.nha.gov.in/')
qr_imgr.save("qr_imgr.jpg")


qr_imgr.show()