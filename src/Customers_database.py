import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "customers.db"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

con = sqlite3.connect(DB_PATH)

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT, email TEXT, phone TEXT, company TEXT, created_at DATATIME DEFAULT CURRENT_TIMESTAMP)")

con.commit()

def ADDcustomer(name, email, phone, company):
    data = [name,email,phone,company]
    cur.execute("""
    INSERT INTO Customers(name,email,phone,company)
    VALUES (?,?,?,?)
    """, data)
    con.commit()

def GETcustomers():
    cur.execute("SELECT * FROM Customers")
    return cur.fetchall()

def SEARCHcustomers(s):
    s = "%"+s+"%"
    cur.execute("SELECT * FROM Customers WHERE name LIKE ? OR email LIKE ? OR phone LIKE ? OR company LIKE ?",(s,s,s,s))
    return cur.fetchall()

def UPDATEcustomer(id, name, email, phone, company):
    cur.execute("""
    UPDATE Customers
    SET name = ?, 
    email = ?,
    phone = ?,
    company = ?
    WHERE id = ?
    """,(name,email,phone,company,id))
    con.commit()
    return cur.rowcount

def DELETEcustomer(id):
    cur.execute("DELETE FROM Customers WHERE id = ?",(id,))
    con.commit()
    return cur.rowcount

    


