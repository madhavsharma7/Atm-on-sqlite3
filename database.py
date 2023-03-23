import sqlite3

def create_db():
    conn=sqlite3.connect("bank.db")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS bank(card_number_to text, pin text, amount text)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS customers(id text,name text,age text, address text, salary text)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS deposit(card_number text, pin text, amount text, contact text)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS login(first_name text, last_name text, username text, password text)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS stu(id text,name text,address text,salary text)')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS type(card_number text,amount text,type text)')
    conn.commit()
    conn.close()
    
create_db()
conn=sqlite3.connect(database=r'bank.db')
cur=conn.cursor()
cur.execute("select * from bank")
res=cur.fetchall()
if len(res)==0:
    create_db()
else:
    print("Already Exist")
    

