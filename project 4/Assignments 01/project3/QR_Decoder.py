import cv2

def decode_qr(filename):
    img = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("Decoded data:", data)
    else:
        print("QR Code not detected or could not be decoded")

decode_qr("qrcode.png")
