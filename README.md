# FastAPI Project

📝 **Created by:** Sareef Masamaeng | Student ID: 6510110115

## 🔧 การตั้งค่าเริ่มต้น

### 1. สร้างและเปิดใช้งาน Virtual Environment

```bash
py -m venv venv
.\venv\Scripts\activate
```

### 2. ติดตั้ง Dependencies

```bash
pip install "fastapi[standard]"
pip install pydantic
pip install sqlalchemy
pip install python-dotenv
```

### 3. รันเซิร์ฟเวอร์

```bash
uvicorn main:app --reload
```

หรือ

```bash
fastapi dev main.py
```

## ⚙️ การตั้งค่า VS Code

1.  **เปิด Command Palette:** `Ctrl+Shift+P`
2.  **พิมพ์:** `Python: Select Interpreter`
3.  **เลือกไฟล์:** `.\venv\Scripts\python.exe`

## 🗄️ การใช้งานฐานข้อมูล

```bash
python read_db.py
```

## 📁 โครงสร้างไฟล์

```
FASTAPI-LAB-TEST/
├── 📁 venv/             # Virtual Environment
├── 📄 main.py           # แอปพลิเคชัน FastAPI หลัก
├── 📄 read_db.py        # สคริปต์อ่านฐานข้อมูล
├── 🗄️ sql_app.db        # ไฟล์ฐานข้อมูล SQLite
└── 📄 .gitignore        # ไฟล์ Git ignore

```

## 🚀 Quick Commands

คำสั่ง

คำอธิบาย

เปิด virtual environment

```bash
.\venv\Scripts\activate
```

รันเซิร์ฟเวอร์ FastAPI

```bash
uvicorn main:app --reload
```

อ่านข้อมูลฐานข้อมูล

```bash
python read_db.py
```

ปิด virtual environment

```bash
deactivate
```

## 📖 API Documentation

🌐 **เซิร์ฟเวอร์รันที่:** `http://localhost:8000`

-   **Swagger UI:** `http://localhost:8000/docs`
-   **ReDoc:** `http://localhost:8000/redoc`

----------

✅ **พร้อมใช้งาน!** สามารถเริ่มพัฒนา API ได้เลย 🎉