--ดึงข้อมูลภาพรวม 10 แถวแรกมาตรวจเช็ก
SELECT UniqueID, disbursed_amount, asset_cost
FROM train
LIMIT 10;

--กรองเฉพาะกลุ่มลูกค้าที่มีประวัติเครดิตบูโร (Inquiries > 0)
SELECT UniqueID, disbursed_amount, "NO.OF_INQUIRIES"
FROM train
WHERE "NO.OF_INQUIRIES" > 0;

--จัดกลุ่มเพื่อหาจำนวนลูกค้าและค่าเฉลี่ยวงเงินแยกตามประเภทอาชีพ
SELECT
    "Employment.Type",
    COUNT(*) AS total_customers,
    AVG(disbursed_amount) AS avg_loan_amount
FROM train
GROUP BY "Employment.Type"
ORDER BY total_customers DESC;