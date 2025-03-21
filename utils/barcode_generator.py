import barcode
from barcode.writer import ImageWriter
import io

def generate_store_barcode(store, barcode_num, price=None):
    # Your barcode generation logic here
    return f"{store}-{barcode_num}-{price}"

def generate_barcode_image(code):
    writer = ImageWriter()
    barcode_obj = barcode.get('code128', code, writer=writer)
    img_io = io.BytesIO()
    barcode_obj.write(img_io, options={'write_text': False})
    img_io.seek(0)
    return img_io
