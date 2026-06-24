import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE appointments ADD COLUMN refund_status TEXT DEFAULT 'none'
""")

conn.commit()
conn.close()

print("✅ refund_status column added")