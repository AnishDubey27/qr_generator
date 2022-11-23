import qrcode

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)

    name = input("Enter the name of the file: ")
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(name + ".png")

url = input("Enter the URL: ")
generate_qr_code(url)