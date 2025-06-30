from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, crud
from app.database import SessionLocal, engine, Base

# สร้างตารางในฐานข้อมูล (ถ้ายังไม่มี)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency สำหรับใช้กับ Depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# สร้างข้อมูลใหม่
@app.post("/items", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreated, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

# อ่านข้อมูลจาก ID
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# อ่านข้อมูลทั้งหมด
@app.get("/items", response_model=List[schemas.ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

# อัปเดตข้อมูล
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreated, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# ลบข้อมูล
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
