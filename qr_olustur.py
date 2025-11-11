import qrcode

url = "https://qr-projem.onrender.com/track"


img = qrcode.make(url)

img.save("qr_kodum.png")

print("QR kod başarıyla oluşturuldu: qr_kodum.png")
