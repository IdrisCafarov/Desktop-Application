import sqlite3

conn=sqlite3.connect("coders.db")

conn.execute("""
             create table admin(
                 admin_id primary key,
                 username unique,
                 password text not null)
             """)
             
conn.commit()
conn.close()



conn=sqlite3.connect("coders.db")

conn.execute("insert into admin values(?,?,?)",("1","idris.jafarov","1234"))

conn.commit()
conn.close()



conn=sqlite3.connect("coders.db")

conn.execute("""
             Create table teachers(
                 teacher_id primary key,
                 username unique,
                 password text not null,
                 name text not null,
                 surname text not null
                 )
             
             
             """)
conn.commit()
conn.close()




conn=sqlite3.connect("coders.db")

conn.execute("""
             Create table students(
                 student_id primary key,
                 group_id number not null,
                 username unique,
                 password text not null,
                 name text not null,
                 surname text not null
                 )
             
             
             """)
conn.commit()
conn.close()


conn=sqlite3.connect("coders.db")

conn.execute("""
             Create table groups(
                 group_id primary key,
                 group_name text not null,
                 teacher_id number not null
                 )
             
             
             """)
conn.commit()
conn.close()




conn=sqlite3.connect("coders.db")

conn.execute("""
             Drop table grades;
             
             
             """)
conn.commit()
conn.close()




conn=sqlite3.connect("coders.db")

conn.execute("""
             Create table grades(
                 grade_date DATE not null,
                 student_grade number not null,
                 student_id number not null
                 
                 
                 )
             
             
             """)
conn.commit()
conn.close()




conn=sqlite3.connect("coders.db")
conn.execute("Delete from teachers where teacher_id=1000")
conn.commit()
conn.close()





