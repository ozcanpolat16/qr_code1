import qrcode

# Flask API URL'si
url = "http://127.0.0.1:5000/"

# QR kodunu oluştur
qr = qrcode.make(url)

# QR kodunu kaydet
qr.save("dynamic_qr_code.png")

print("QR kodu oluşturuldu ve kaydedildi: dynamic_qr_code.png")
