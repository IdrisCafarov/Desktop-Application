import sqlite3

def insert_teacher(teacher_id,username,password,name,surname):
    conn=sqlite3.connect('coders.db')
    
    try:
    
        conn.execute("insert into teachers values(?, ?, ?, ?, ?)",
                 (teacher_id,username,password,name,surname))
        
        conn.commit()
        
        return True
        
    except sqlite3.IntegrityError:
        return False
        
    

    finally:
        conn.close()
        
        
def insert_student(student_id,group_id,username,password,name,surname):
    conn=sqlite3.connect('coders.db')
    
    try:
    
        conn.execute("insert into students values(?, ?, ?, ?, ?, ?)",
                 (student_id,group_id,username,password,name,surname))
        
        conn.commit()
        
        return True
        
    except sqlite3.IntegrityError:
        return False
        
    

    finally:
        conn.close()
        
        
def insert_group(group_id,group_name,teacher_id):
    conn=sqlite3.connect('coders.db')
    
    try:
    
        conn.execute("insert into groups values(?, ?, ?)",
                 (group_id,group_name,teacher_id))
        
        conn.commit()
        
        return True
        
    except sqlite3.IntegrityError:
        return False
        
    

    finally:
        conn.close()        


def insert_admin(admin_id,username,password):
    conn=sqlite3.connect('coders.db')
    
    try:
    
        conn.execute("insert into admin values(?, ?, ?)",
                 (admin_id,username,password))
        
        conn.commit()
        
        return True
        
    except sqlite3.IntegrityError:
        return False
        
    

    finally:
        conn.close()        



    
def select_user_admin(username, password):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from admin
                 where username=?
                 and password=?""",
                 (username, password))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True


def select_user_teacher(username, password):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from teachers
                 where username=?
                 and password=?""",
                 (username, password))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True

def select_user_student(username, password):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from students
                 where username=?
                 and password=?""",
                 (username, password))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True

def check_grades(grade_date, student_id):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from grades
                 where grade_date=?
                 and student_id=?""",
                 (grade_date, student_id))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return True
    return False




def insert_grades(grade_date,student_grade,student_id):
    conn=sqlite3.connect('coders.db')
    
    try:
    
        conn.execute("insert into grades values(?, ?, ?)",
                 (grade_date,student_grade,student_id))
        
        conn.commit()
        
        return True
        
    except sqlite3.IntegrityError:
        return False
        
    

    finally:
        conn.close() 
        
        
        
def update_teacher(teacher_id,key,new_data):
    conn=sqlite3.connect('coders.db')
    if key=="username":
        conn.execute("""
                 Update teachers
                 Set username=?
                 where teacher_id=?
                 
                 """,(new_data,teacher_id))
    elif key=="password":
        conn.execute("""
                 Update teachers
                 Set password=?
                 where teacher_id=?
                 
                 """,(new_data,teacher_id))
    elif key=="name":
        conn.execute("""
                 Update teachers
                 Set name=?
                 where teacher_id=?
                 
                 """,(new_data,teacher_id))
                 
    elif key=="surname":
        conn.execute("""
                 Update teachers
                 Set surname=?
                 where teacher_id=?
                 
                 """,(new_data,teacher_id))
        
                 
                 
    conn.commit()
    conn.close()
        
        
        
def update_student(student_id,key,new_data):
    conn=sqlite3.connect('coders.db')
    if key=="username":
        conn.execute("""
                 Update students
                 Set username=?
                 where student_id=?
                 
                 """,(new_data,student_id))
    elif key=="password":
        conn.execute("""
                 Update students
                 Set password=?
                 where student_id=?
                 
                 """,(new_data,student_id))
    elif key=="name":
        conn.execute("""
                 Update students
                 Set name=?
                 where student_id=?
                 
                 """,(new_data,student_id))
                 
    elif key=="surname":
        conn.execute("""
                 Update students
                 Set surname=?
                 where student_id=?
                 
                 """,(new_data,student_id))
        
                 
                 
    conn.commit()
    conn.close()
        
        
def update_admin(admin_id,key,new_data):
    conn=sqlite3.connect('coders.db')
    if key=="username":
        conn.execute("""
                 Update admin
                 Set username=?
                 where admin_id=?
                 
                 """,(new_data,admin_id))
    elif key=="password":
        conn.execute("""
                 Update admin
                 Set password=?
                 where admin_id=?
                 
                 """,(new_data,admin_id))
        
                 
                 
    conn.commit()
    conn.close()
                

    

def check_teacher(teacher_id):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from teachers
                 where teacher_id=?""",
                 (teacher_id))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True



def delete_teacher(teacher_id):
    conn=sqlite3.connect("coders.db")
    conn.execute("Delete from teachers where teacher_id=?",teacher_id)
    conn.commit()
    conn.close()



def check_student(student_id):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from students
                 where student_id=?""",
                 (student_id))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True



def delete_student(student_id):
    conn=sqlite3.connect("coders.db")
    conn.execute("Delete from students where student_id=?",student_id)
    conn.commit()
    conn.close()
   
        

    
def check_admin(admin_id):
    conn=sqlite3.connect('coders.db')
    
    data=conn.execute("""select * from admin
                 where admin_id=?""",
                 (admin_id))
    
    info=data.fetchall()
    
    conn.close()


    if info==[]:
        return False
    return True



def delete_admin(admin_id):
    conn=sqlite3.connect("coders.db")
    conn.execute("Delete from admin where admin_id=?",admin_id)
    conn.commit()
    conn.close()
   
            
        
def update_grade(student_id,student_grade,grade_date):
    conn=sqlite3.connect('coders.db')
    conn.execute("""
                 Update grades
                 Set student_grade=?
                 where student_id=? and grade_date=?
                 
                 """,(student_grade,student_id,grade_date))
    conn.commit()
    conn.close()

conn=sqlite3.connect('coders.db')
conn.execute("""
                 Update grades
                 Set student_grade=?
                 where student_id=? and grade_date=?
                 
                 """,(["88","3","7/15/22"]))
conn.commit()
conn.close()


