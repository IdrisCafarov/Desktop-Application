import sqlite3
def create_table():
    conn=sqlite3.connect("coders.db")
    conn.execute("""
    create table telebeler_login(
        username primary key,
        password text not null,
        name text not null,
        surname text not null,
        );           
                 """)
                 
    conn.commit()
    conn.close()
    
    
    
def insert_table():
    