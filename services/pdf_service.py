import os
import io
import base64
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from utils.file_utils import is_valid_image

FOLDER_PATH = "C://Users//sagar//Desktop//Demo_Folder"

def generate_pdf_from_images():
    page_w, page_h = A4
    buffer = io.BytesIO()
    canv = canvas.Canvas(buffer, A4)

    error_map = {}
    error_count = 0
    file_read = 0
    file_count = 0

    for filename in os.listdir(FOLDER_PATH):
        fullpath = os.path.join(FOLDER_PATH, filename)
        file_count += 1

        if not is_valid_image(filename):
            error_map[filename] = "Skipped: Not a supported image format"
            error_count += 1
            continue

        try:
            img = ImageReader(fullpath)
            img_w, img_h = img.getSize()
            scale = min(page_w / img_w, page_h / img_h)
            new_w = img_w * scale
            new_h = img_h * scale
            x = (page_w - new_w) / 2
            y = (page_h - new_h) / 2
            canv.drawImage(fullpath, x, y, width=new_w, height=new_h, preserveAspectRatio=True, anchor='c')
            canv.showPage()
            file_read += 1
        except Exception as e:
            error_map[filename] = str(e)
            error_count += 1

    canv.save()
    buffer.seek(0)

    pdf_string = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return {
        'Number of Files': file_count,
        'File Converted': file_read,
        'Error Count': error_count,
        'Error Map': [(key, value) for key, value in error_map.items()],
        'Status': '00' if file_count == file_read else '99',
        'pdf_bytes': pdf_string
    }
