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
│
├── 📁 app/                  # โฟลเดอร์สำหรับโค้ด Backend
│   ├── __init__.py          # ทำให้ app เป็น Python Package
│   ├── crud.py              # ฟังก์ชัน CRUD (Create/Read/Update/Delete)
│   ├── database.py          # ตั้งค่าการเชื่อมต่อฐานข้อมูล SQLAlchemy
│   ├── models.py            # โครงสร้างตารางฐานข้อมูล (ORM Models)
│   └── schemas.py           # โครงสร้างข้อมูล Pydantic (Request/Response)
│
├── 📁 venv/                 # Virtual Environment (ไม่ push ขึ้น Git)
│
├── ⚙️ .env                  # ตัวแปร Config (เช่น DATABASE_URL)
├── 🔒 .gitignore            # ไฟล์ที่ Git ไม่ต้อง Track
├── 🚀 main.py               # จุดเริ่มต้นของแอป FastAPI
├── 🧪 read_db.py            # สคริปต์ทดสอบ/อ่านฐานข้อมูล
├── 📦 requirements.txt      # รายชื่อไลบรารีที่ใช้
└── 🗄️ sql_app.db           # ไฟล์ฐานข้อมูล SQLite
```

## 📋 คำอธิบายไฟล์

| ไฟล์/โฟลเดอร์ | หน้าที่ |
|---------------|---------|
| `app/` | โฟลเดอร์หลักสำหรับโค้ด Backend |
| `__init__.py` | ทำให้ app เป็น Python Package |
| `crud.py` | ฟังก์ชัน Create, Read, Update, Delete |
| `database.py` | การเชื่อมต่อและตั้งค่าฐานข้อมูล |
| `models.py` | โครงสร้างตารางฐานข้อมูล (SQLAlchemy ORM) |
| `schemas.py` | โครงสร้างข้อมูล Input/Output (Pydantic) |
| `main.py` | จุดเริ่มต้นและ API Routes |
| `read_db.py` | สคริปต์สำหรับทดสอบฐานข้อมูล |
| `.env` | ตัวแปรสภาพแวดล้อม (Database URL, Secret Keys) |
| `.gitignore` | กำหนดไฟล์ที่ไม่ต้องเก็บใน Git |

---

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