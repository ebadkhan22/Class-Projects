import qrcode

def create_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,  # Controls size (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

create_qr("https://example.com")
