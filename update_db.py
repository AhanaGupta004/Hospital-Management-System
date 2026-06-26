import sqlite3

conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# 🔥 GET EXISTING COLUMNS
cursor.execute("PRAGMA table_info(appointments)")
columns = [col[1] for col in cursor.fetchall()]

# 🔥 ADD payment_status IF NOT EXISTS
if "payment_status" not in columns:
    cursor.execute("""
    ALTER TABLE appointments 
    ADD COLUMN payment_status TEXT DEFAULT 'pending'
    """)
    print("✅ payment_status added")
else:
    print("⚠️ payment_status already exists")

# 🔥 ADD refund_status IF NOT EXISTS
if "refund_status" not in columns:
    cursor.execute("""
    ALTER TABLE appointments 
    ADD COLUMN refund_status TEXT DEFAULT 'none'
    """)
    print("✅ refund_status added")
else:
    print("⚠️ refund_status already exists")

# 🔥 FIX OLD DATA (VERY IMPORTANT)
cursor.execute("""
UPDATE appointments 
SET payment_status='pending' 
WHERE payment_status IS NULL
""")

cursor.execute("""
UPDATE appointments 
SET refund_status='none' 
WHERE refund_status IS NULL
""")

conn.commit()
conn.close()

print("🔥 Database fully updated successfully!")