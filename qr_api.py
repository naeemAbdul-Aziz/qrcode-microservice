from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import qrcode
import uuid
import os


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain for security later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the request body structure
class QRRequest(BaseModel):
    url: str

# Home route
@app.get("/")
def root():
    return {"message": "QR Code API by Naeem"}

# Generate QR code
@app.post("/generate_qr")
def generate_qr(qr_req: QRRequest):
    url = qr_req.url
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join("qr_codes", filename)

    # Ensure directory exists
    os.makedirs("qr_codes", exist_ok=True)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath) # type: ignore

    return {
        "message": "QR code generated successfully",
        "file_url": f"/download_qr/{filename}"
    }

# Download the QR code image
@app.get("/download_qr/{filename}")
def download_qr(filename: str):
    filepath = os.path.join("qr_codes", filename)
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type='image/png', filename=filename)
    raise HTTPException(status_code=404, detail="QR code not found")
