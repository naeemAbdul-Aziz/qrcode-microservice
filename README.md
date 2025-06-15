# 🚀 QR Code Generator Microservice

A lightweight, containerized FastAPI microservice that accepts a URL and returns a downloadable QR code image via REST API.

**Live Demo:** https://qrcode-microservice.onrender.com  
**Frontend Companion:** Coming soon...

## 📦 Features

- 🔗 Accepts any URL via JSON POST
- 📷 Generates a scannable QR code
- 📁 Saves and serves QR image as downloadable PNG
- 🐳 Fully Dockerized for cloud deployment
- ⚡ Fast, async-ready Python API using FastAPI
- 🔓 CORS enabled for frontend integration

## 🔧 Tech Stack

- **Backend Framework:** FastAPI
- **QR Generation:** qrcode Python library
- **Image Processing:** Pillow (via qrcode)
- **Containerization:** Docker
- **Hosting:** Render.com / Railway
- **Language:** Python 3.11+

## 📂 Project Structure

```bash
qrcode-microservice/
│
├── qr_api.py           # FastAPI app (main service logic)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker instructions
├── qr_codes/           # Folder where QR images are saved (generated at runtime)
└── README.md           # This file
```

## 🚀 Getting Started

### ✅ 1. Clone the repo

```bash
git clone https://github.com/naeemAbdul-Aziz/qrcode-microservice.git
cd qrcode-microservice
```

### ✅ 2. Install dependencies (for local testing)

```bash
pip install -r requirements.txt
```

### ✅ 3. Run locally with FastAPI

```bash
uvicorn qr_api:app --reload
```

Go to:
- http://127.0.0.1:8000/docs for interactive Swagger UI

## 🐳 Docker Deployment

### 🔨 Build Docker Image

```bash
docker build -t qr_api .
```

### 🚀 Run the Container

```bash
docker run -d -p 8000:8000 qr_api
```

Visit http://localhost:8000

## 📬 API Usage

### ▶️ POST /generate_qr

Generates a QR code from a URL.

**Request Body (JSON):**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "message": "QR code generated successfully",
  "file_url": "/download_qr/<filename>.png"
}
```

### 🖼 GET /download_qr/{filename}

Downloads or displays the QR code image.

**Example:**
```
GET /download_qr/bd47c1ab.png
```

## 🌐 CORS Enabled

Supports cross-origin requests for frontend integration.

You can limit CORS in `qr_api.py`:
```python
allow_origins=["https://your-frontend.com"]
```

## 📡 Deployment

This app is easily deployable on:
- 🔷 Render
- 🔶 Railway
- ⚙️ Any VPS (e.g. DigitalOcean, EC2, etc.)

## 🛠 Environment Config (optional)

For production:
- Add logging
- Add cleanup cron jobs for old QR files
- Use cloud file storage (e.g., AWS S3)

## 📜 License

MIT License — use freely, credit appreciated 💜

## 💡 Future Ideas

- Upload your own logo inside the QR
- User login to track QR history
- Database logging (PostgreSQL or Firebase)
- Email QR to users after generation
- Auto-delete QR codes after 24 hours
