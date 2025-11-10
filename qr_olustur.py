import qrcode

url = "https://www.archerobotics.com/"

img = qrcode.make(url)

img.save("qr_kodum.png")

print("QR kod başarıyla oluşturuldu: qr_kodum.png")
