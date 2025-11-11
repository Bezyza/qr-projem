import qrcode

# Base URL
base_url = "https://qr-projem.onrender.com/track"

url_teknosa = f"{base_url}?qr=teknosa"
img1 = qrcode.make(url_teknosa)
img1.save("qr_teknosa.png")
print("Teknosa QR oluşturuldu:", url_teknosa)


url_media = f"{base_url}?qr=mediamarkt"
img2 = qrcode.make(url_media)
img2.save("qr_mediamarkt.png")
print("MediaMarkt QR oluşturuldu:", url_media)