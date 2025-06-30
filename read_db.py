import sqlite3

conn = sqlite3.connect("sql_app.db")
cursor = conn.cursor()

# ดึงชื่อคอลัมน์
cursor.execute("PRAGMA table_info(items);")
columns = [col[1] for col in cursor.fetchall()]

# ดึงข้อมูล
cursor.execute("SELECT * FROM items;")
rows = cursor.fetchall()

# แสดงผลแบบสวยงาม
print(" | ".join(columns))
print("-" * 50)
for row in rows:
    print(" | ".join(str(x) for x in row))

conn.close()
