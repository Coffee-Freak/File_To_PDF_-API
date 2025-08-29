# **FastAPI Image-to-PDF Service**

This project provides a **FastAPI-based microservice** that converts images from a folder into a single compressed PDF file.
It supports both **Base64 JSON responses** and **direct PDF downloads**, with error reporting for unsupported or failed images.

---

## 📂 **Project Structure**

```
project/
│── main.py                  # FastAPI app entry point
│── controllers/
│    └── pdf_controller.py   # API routes
│── services/
│    └── pdf_service.py      # Business logic (PDF generation)
│── utils/
│    └── file_utils.py       # Helper functions
│── README.md                # Project documentation
```

---

## ⚙️ **Installation**

1. **Clone this repository**

   ```bash
   https://github.com/Coffee-Freak/File_To_PDF_-API.git
   cd File_To_PDF_-API
   ```

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv NotPython
   source NotPython/bin/activate     # Linux / Mac
   NotPython\Scripts\activate        # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install fastapi uvicorn reportlab
   ```

---

## ▶️ **Running the App**

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

* Server will run at:
  👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📑 **Endpoints**

### 1. **Generate PDF (Base64 Response)**

```http
GET /pdf/generate
```

* Converts all images in the configured folder into a PDF.
* Returns a JSON response containing:

  * `pdf_bytes` (base64 string of PDF)
  * File statistics (total, converted, errors)
  * Error map

📌 Example Response:

```json
{
  "Number of Files": 10,
  "File Converted": 8,
  "Error Count": 2,
  "Error Map": [["badfile.txt", "Skipped: Not a supported image format"]],
  "Status": "99",     // "00" if all files are converted successfully
  "pdf_bytes": "JVBERi0xLjMKJcTl..."
}
```

## 🖼️ **Image Support**

Supported extensions:
`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.gif`, `.tiff`

---

## 🛠️ **Configuration**

* Default image folder is set in:
  `services/pdf_service.py → FOLDER_PATH`

Change it to your desired folder:

```python
FOLDER_PATH = "__[Local-storage-address]__"
# Working only with the local storage (Future feature reading files directly from cloud storage)

```

---

## 🚀 **Future Improvements**

* [ ] Accept dynamic folder paths via query parameters
* [ ] Support direct image uploads via `POST`
* [ ] Add async support for better performance

---

## 👨‍💻 **Contributing**

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---