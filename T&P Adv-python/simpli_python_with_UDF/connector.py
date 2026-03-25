import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sahil@7848",
    port=3306,
    database="GIETU"
)

cursor = conn.cursor()

def run_query(query, description):
    print(f"\n{description}")
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
run_query("SELECT * FROM GIETU;", "1. All data from gietu")
run_query("SELECT name FROM GIETU;", "2. Only name column")
run_query("SELECT name, address FROM GIETU;", "3. Name and address")
run_query("SELECT rollno, salary FROM GIETU;", "4. Employee ID and salary")
run_query("SELECT * FROM GIETU WHERE name='aman';", "5. Name = aman")
run_query("SELECT * FROM GIETU WHERE address='delhi';", "6. Address = delhi")
run_query("SELECT * FROM GIETU WHERE gender='M';", "7. Gender = M")
run_query("SELECT * FROM GIETU WHERE designation='doctor';", "8. Designation = doctor")
run_query("SELECT * FROM GIETU WHERE salary=15000;", "9. Salary = 15000")
run_query("SELECT * FROM GIETU WHERE salary>20000;", "10. Salary > 20000")
run_query("SELECT * FROM GIETU WHERE salary<30000;", "11. Salary < 30000")
run_query("SELECT * FROM GIETU WHERE gender='M' AND salary>20000;", "12. Male AND salary > 20000")
run_query("SELECT * FROM GIETU WHERE gender='F' OR address='raipur';", "13. Female OR address = raipur")
run_query("SELECT * FROM GIETU WHERE name LIKE 'a%';", "14. Name starts with 'a'")
run_query("SELECT * FROM GIETU WHERE name LIKE '%h';", "15. Name ends with 'h'")
run_query("SELECT * FROM GIETU WHERE address LIKE '%pur%';", "16. Address contains 'pur'")
run_query("SELECT * FROM GIETU ORDER BY name ASC;", "17. Sorted by name ASC")
run_query("SELECT * FROM GIETU ORDER BY salary DESC;", "18. Sorted by salary DESC")
run_query("SELECT COUNT(*) FROM GIETU;", "19. Total employees")
run_query("SELECT COUNT(*) FROM GIETU WHERE gender='M';", "20. Count male employees")

cursor.close()
conn.close()