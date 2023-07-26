import qrcode
from PIL import Image
import re

# Pide al usuario que ingrese el URL
url = input("Por favor, ingresa el URL: ")

# Genera el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=600,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

# Prepara un nombre de archivo seguro
filename = re.sub(r'\W+', '', url) + '.png'  # Elimina caracteres no seguros

# Guarda como PNG
img.save(filename)