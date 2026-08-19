import pandas as pd
df = pd.read_csv('test1(Sheet1).csv')
# Data Exploration
print("--- โครงสร้างข้อมูลภาพรวม ---")
df.info()
print("\n--- ตัวอย่างข้อมูล 5 แถวแรก ---")
print(df.head())
# Data Cleaning
#Strip Whitespace
df['Employment.Type'] = df['Employment.Type'].str.strip()
# เปลี่ยนชื่อคอลัมน์ให้ไม่มีจุด และเป็นพิมพ์เล็กทั้งหมด
df.columns = df.columns.str.replace('.', '_', regex=False).str.lower()
#Drop Duplicates
duplicate_count = df.duplicated().sum()
print(f"\nพบข้อมูลซ้ำซ้อนกันทั้งหมด: {duplicate_count} แถว")
# ลบแถวที่ซ้ำทิ้งไป (ถ้ามี) และอัปเดตใส่ตารางเดิม
df.drop_duplicates(inplace=True)
#บันทึกไฟล์cleaning
df.to_csv('clean_loan_data.csv', index=False)
print("\n--- ทำความสะอาดเสร็จสิ้น! บันทึกไฟล์ใหม่เรียบร้อยแล้ว ---")