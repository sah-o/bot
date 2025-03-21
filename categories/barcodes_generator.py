import barcode
from barcode.writer import ImageWriter
import io

def generate_store_barcode(store, barcode_num, price=None):
    store = store.lower()
    if store == "morrisons":
        return f"92{barcode_num.zfill(13)}00113300027"
    elif store == "ms":
        return f'821{barcode_num.zfill(8)}{int(price):07d}'
    elif store == "waitrose":
        return f'10{barcode_num.zfill(13)}00{int(price):02d}'
    elif store == "savers":
        return f'97{barcode_num.zfill(13)}{int(price):03d}0'
    elif store == "sainsburys":
        return f'91{barcode_num.zfill(12)}{int(price):03d}0'
    else:
        return barcode_num  # Fallback for unknown stores

def generate_barcode_image(code):
    writer = ImageWriter()
    barcode_obj = barcode.get('code128', code, writer=writer)
    img_io = io.BytesIO()
    barcode_obj.write(img_io, options={'write_text': False})
    img_io.seek(0)
    return img_io
