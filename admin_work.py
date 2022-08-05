import tkinter
import sqlite3
from tkinter import ttk
from PIL import ImageTk,Image



wrk=tkinter.Tk()

wrk.resizable(0,0)
wrk.state('zoomed')


img = Image.open("bg_tc_4.jpg")


bg_img=ImageTk.PhotoImage(img,master=wrk)


label_bg = tkinter.Label(wrk,image=bg_img,bg='#040405')
label_bg.pack(fill='both',expand='yes')


log_frm=tkinter.Frame(wrk,bg='#040405',width=850,height=600)
log_frm.place(x=250,y=100)

head_log=tkinter.Label(log_frm,text="Welcome to Admin System",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
head_log.place(x=120,y=30,height=30)

op_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Operations",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
op_frame.place(x=10,y=70,width=340,height=500)




res_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Fillings",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
res_frame.place(x=370,y=70,width=450,height=500)




def home():
    wrk.destroy()
    import desk_app_log

def go_back():
    for widget in op_frame.winfo_children():
       widget.destroy()
       
    b1=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Add Staff',bg='grey',fg='snow',width=30,height=2,command=add_staff)
    b1.pack()

    b2=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Update Staff',bg='grey',fg='snow',width=30,height=2,command=update_staff)
    b2.pack()

    b3=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Delete Staff',bg='grey',fg='snow',width=30,height=2,command=delete_staff)
    b3.pack()
    
    home_button=tkinter.Button(op_frame,text='Main Page',font=('yu gothic vi',12,'bold'),command=home,bg='grey',fg='snow',width=30,height=2)
    home_button.pack()

def add_staff():
    
    
    
    def add_teacher():
        for widget in res_frame.winfo_children():
            widget.destroy()
            
        def add_teachers():
            import funcs as func
            usr_idd=id_ent.get()
            usr_nm=usr_ent.get()
            paswrd=pasw_ent.get()
            namee=name_ent.get()
            srnm=surname_ent.get()
            
            if id_ent.get().strip()!="" and usr_ent.get().strip()!="" and pasw_ent.get().strip!="" and name_ent.get().strip()!=0 and surname_ent.get().strip()!=0:
                
            
                if func.insert_teacher(usr_idd,usr_nm,paswrd,namee,srnm):
                    warn_lab.config(text='Correctly Inserted',fg='green')
                else:
                    warn_lab.config(text='Could not inserted',fg='red')
                    
            else:
                warn_lab.config(text='There is empty data',fg='red')
                
                
        id_label=tkinter.Label(res_frame,text="Teacher ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        id_label.place(x=10,y=0)
    
        id_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        id_ent.place(x=20,y=25)
    
        id_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        id_line.place(x=10,y=50)
    
        
        
        usr_label=tkinter.Label(res_frame,text="Username",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        usr_label.place(x=10,y=60)
    
        usr_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        usr_ent.place(x=20,y=95)
    
        usr_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        usr_line.place(x=10,y=120)
    
        
        
        pasw_label=tkinter.Label(res_frame,text="Password",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        pasw_label.place(x=10,y=130)
    
        pasw_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        pasw_ent.place(x=20,y=155)
    
        pasw_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        pasw_line.place(x=10,y=190)
    
        
        
        name_label=tkinter.Label(res_frame,text="Name",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        name_label.place(x=10,y=200)
    
        name_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        name_ent.place(x=20,y=225)
    
        name_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        name_line.place(x=10,y=250)
    
        
        
        surname_label=tkinter.Label(res_frame,text="Surname",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        surname_label.place(x=10,y=260)
    
        surname_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        surname_ent.place(x=20,y=295)
    
        surname_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        surname_line.place(x=10,y=320)
    
        
        
        but1=tkinter.Button(res_frame,text='Submit',font=('yu gothic vi',12,'bold'),command=add_teachers,bg='grey',fg='snow',width=30,height=2)
        but1.place(x=10,y=330)
    
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=420)
            
        
    
    def add_student():
        for widget in res_frame.winfo_children():
            widget.destroy()
            
        def add_students():
            import funcs as func
            usr_idd=id_ent.get()
            usr_group=group_ent.get()
            usr_nm=usr_ent.get()
            paswrd=pasw_ent.get()
            namee=name_ent.get()
            srnm=surname_ent.get()
            
            if id_ent.get().strip()!="" and group_ent.get().strip()!="" and usr_ent.get().strip()!="" and pasw_ent.get().strip!="" and name_ent.get().strip()!=0 and surname_ent.get().strip()!=0:
                
            
                if func.insert_student(usr_idd,usr_group,usr_nm,paswrd,namee,srnm):
                    warn_lab.config(text='Correctly Inserted',fg='green')
                else:
                    warn_lab.config(text='Could not inserted',fg='red')
                    
            else:
                warn_lab.config(text='There is empty data',fg='red')
                
                
        id_label=tkinter.Label(res_frame,text="Student ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        id_label.place(x=10,y=0)
    
        id_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        id_ent.place(x=20,y=25)
    
        id_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        id_line.place(x=10,y=50)
    
        
        
        group_label=tkinter.Label(res_frame,text="Group ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        group_label.place(x=10,y=60)
    
        group_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        group_ent.place(x=20,y=85)
    
        group_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        group_line.place(x=10,y=110)
    
        
        
        usr_label=tkinter.Label(res_frame,text="Username",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        usr_label.place(x=10,y=120)
    
        usr_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        usr_ent.place(x=20,y=145)
    
        usr_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        usr_line.place(x=10,y=170)
    
        
        
        pasw_label=tkinter.Label(res_frame,text="Password",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        pasw_label.place(x=10,y=180)
    
        pasw_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        pasw_ent.place(x=20,y=205)
    
        pasw_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        pasw_line.place(x=10,y=230)
    
        
        
        name_label=tkinter.Label(res_frame,text="Name",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        name_label.place(x=10,y=240)
    
        name_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        name_ent.place(x=20,y=265)
    
        name_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        name_line.place(x=10,y=290)
    
        
        
        surname_label=tkinter.Label(res_frame,text="Surname",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        surname_label.place(x=10,y=300)
    
        surname_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        surname_ent.place(x=20,y=325)
    
        surname_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        surname_line.place(x=10,y=350)
    
        
        
        but1=tkinter.Button(res_frame,text='Submit',font=('yu gothic vi',12,'bold'),command=add_students,bg='grey',fg='snow',width=30,height=2)
        but1.place(x=10,y=360)
    
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=420)
            
        
    
    
    def add_groups():
        for widget in res_frame.winfo_children():
            widget.destroy()
        
        def add_group():
            import funcs as func
            group_idd_idd=id_ent.get()
            name_group=group_ent.get()
            teacher_id=teacher_ent.get()
            
            if id_ent.get().strip()!="" and group_ent.get().strip()!="" and teacher_ent.get().strip()!="":
            
                if func.insert_group(group_idd_idd,name_group,teacher_id):
                    warn_lab.config(text='Correctly Inserted',fg='green')
                else:
                    warn_lab.config(text='Could not inserted',fg='red')
            else:
                warn_lab.config(text='There is empty data',fg='red')
                
                
        id_label=tkinter.Label(res_frame,text="Group ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        id_label.place(x=10,y=0)
    
        id_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        id_ent.place(x=20,y=25)
    
        id_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        id_line.place(x=10,y=50)
    
        
        
        group_label=tkinter.Label(res_frame,text="Group Name",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        group_label.place(x=10,y=60)
    
        group_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        group_ent.place(x=20,y=85)
    
        group_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        group_line.place(x=10,y=110)
    
        
        
        teacher_label=tkinter.Label(res_frame,text="Teacher ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        teacher_label.place(x=10,y=120)
    
        teacher_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        teacher_ent.place(x=20,y=145)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=170)
    
        
        
        
        but1=tkinter.Button(res_frame,text='Submit',font=('yu gothic vi',12,'bold'),command=add_group,bg='grey',fg='snow',width=30,height=2)
        but1.place(x=10,y=180)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=240)
        
    def add_admins():
        for widget in res_frame.winfo_children():
            widget.destroy()
        
        def add_admin():
            import funcs as func
            admin_id=id_ent.get()
            username=user_ent.get()
            password=pasw_ent.get()
            if id_ent.get().strip()!="" and user_ent.get().strip()!="" and pasw_ent.get().strip()!="":
                
                if func.insert_admin(admin_id,username,password):
                    warn_lab.config(text='Correctly Inserted',fg='green')
                else:
                    warn_lab.config(text='Could not inserted',fg='red')
            else:
                warn_lab.config(text='There is empty data',fg='red')
                
                
        id_label=tkinter.Label(res_frame,text="Admin ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        id_label.place(x=10,y=0)
    
        id_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        id_ent.place(x=20,y=25)
    
        id_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        id_line.place(x=10,y=50)
    
        
        
        user_label=tkinter.Label(res_frame,text="Username",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        user_label.place(x=10,y=60)
    
        user_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        user_ent.place(x=20,y=85)
    
        user_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        user_line.place(x=10,y=110)
    
        
        
        pasw_label=tkinter.Label(res_frame,text="Password",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        pasw_label.place(x=10,y=120)
    
        pasw_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
        pasw_ent.place(x=20,y=145)
    
        pasw_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        pasw_line.place(x=10,y=170)
    
        
        
        but1=tkinter.Button(res_frame,text='Submit',font=('yu gothic vi',12,'bold'),command=add_admin,bg='grey',fg='snow',width=30,height=2)
        but1.place(x=10,y=180)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=240)
        
    
    
    for widget in op_frame.winfo_children():
       widget.destroy()
       
    b1=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Teacher',bg='grey',fg='snow',width=30,height=2,command=add_teacher)
    b1.pack()
    
    b2=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Student',bg='grey',fg='snow',width=30,height=2,command=add_student)
    b2.pack()
    
    b3=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Admin',bg='grey',fg='snow',width=30,height=2,command=add_admins)
    b3.pack()
    
    b4=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Lesson Group',bg='grey',fg='snow',width=30,height=2,command=add_groups)
    b4.pack()
    
    
    b5=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Go Back',bg='grey',fg='snow',width=30,height=2,command=go_back)
    b5.pack()
    
    
def update_staff():
    
    
    
    
    def update_teacher():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select name||' '||surname,teacher_id
                  from teachers
                  
                  
                  """)

        teachers_info=data.fetchall()
        conn.commit()
        conn.close()
        def change():
            import funcs as func
            teacher_id=comMember1.get().split()[-1]
            key=comMember2.get()
            new_data=entry_ent.get()
            
            if new_data.strip()!="":
                func.update_teacher(teacher_id,key,new_data)
                warn_lab.config(text="data updated",fg="green")
            else:
                warn_lab.config(text="cant update empty data",fg='red')
            
        
        
        for widget in res_frame.winfo_children():
            widget.destroy()
        
        teacher_label=tkinter.Label(res_frame,text="Teacher",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        teacher_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= teachers_info
        comMember1.place(x=20,y=40)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=70)
    
    
    
    
        data_label=tkinter.Label(res_frame,text="Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        data_label.place(x=10,y=80)
    
        comMember2= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember2["values"]= ["username","password","name","surname"]
        comMember2.place(x=20,y=105)
    
        data_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        data_line.place(x=10,y=135)
    
    
    
    
        entry_label=tkinter.Label(res_frame,text="New Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        entry_label.place(x=10,y=145)
        
        entry_ent=tkinter.Entry(res_frame,font=('yu gothic vi',13,'bold'))
        entry_ent.place(x=20,y=170)
        
        entry_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        entry_line.place(x=10,y=200)
        
        
        btn=tkinter.Button(res_frame,command=change,text='Submit',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=240)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=300)
        
        
    def update_student():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select name||' '||surname,student_id
                  from students
                  
                  
                  """)

        students_info=data.fetchall()
        conn.commit()
        conn.close()
        def change():
            import funcs as func
            student_id=comMember1.get().split()[-1]
            key=comMember2.get()
            new_data=entry_ent.get()
            
            if new_data.strip()!="":
                func.update_student(student_id,key,new_data)
                warn_lab.config(text="data updated",fg="green")
            else:
                warn_lab.config(text="cant update empty data",fg='red')
            
        
        
        for widget in res_frame.winfo_children():
            widget.destroy()
        
        student_label=tkinter.Label(res_frame,text="Student",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        student_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= students_info
        comMember1.place(x=20,y=40)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=70)
    
    
    
    
        data_label=tkinter.Label(res_frame,text="Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        data_label.place(x=10,y=80)
    
        comMember2= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember2["values"]= ["username","password","name","surname"]
        comMember2.place(x=20,y=105)
    
        data_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        data_line.place(x=10,y=135)
    
    
    
    
        entry_label=tkinter.Label(res_frame,text="New Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        entry_label.place(x=10,y=145)
        
        entry_ent=tkinter.Entry(res_frame,font=('yu gothic vi',13,'bold'))
        entry_ent.place(x=20,y=170)
        
        entry_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        entry_line.place(x=10,y=200)
        
        
        btn=tkinter.Button(res_frame,command=change,text='Submit',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=240)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=300)   
    
    
    def update_admin():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select username,admin_id
                  from admin
                  
                  
                  """)

        admins_info=data.fetchall()
        conn.commit()
        conn.close()
        def change():
            import funcs as func
            admin_id=comMember1.get().split()[-1]
            key=comMember2.get()
            new_data=entry_ent.get()
            
            if new_data.strip()!="":
                func.update_admin(admin_id,key,new_data)
                warn_lab.config(text="data updated",fg="green")
            else:
                warn_lab.config(text="cant update empty data",fg='red')
            
        
        
        for widget in res_frame.winfo_children():
            widget.destroy()
        
        student_label=tkinter.Label(res_frame,text="Admin",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        student_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= admins_info
        comMember1.place(x=20,y=40)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=70)
    
    
    
    
        data_label=tkinter.Label(res_frame,text="Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        data_label.place(x=10,y=80)
    
        comMember2= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember2["values"]= ["username","password"]
        comMember2.place(x=20,y=105)
    
        data_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        data_line.place(x=10,y=135)
    
    
    
    
        entry_label=tkinter.Label(res_frame,text="New Data",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        entry_label.place(x=10,y=145)
        
        entry_ent=tkinter.Entry(res_frame,font=('yu gothic vi',13,'bold'))
        entry_ent.place(x=20,y=170)
        
        entry_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        entry_line.place(x=10,y=200)
        
        
        btn=tkinter.Button(res_frame,command=change,text='Submit',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=240)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=300)   
    
    
    
    
    for widget in op_frame.winfo_children():
       widget.destroy()
       
    b1=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Teacher',bg='grey',fg='snow',width=30,height=2,command=update_teacher)
    b1.pack()
    
    b2=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Student',bg='grey',fg='snow',width=30,height=2,command=update_student)
    b2.pack()
    
    b3=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Admin',bg='grey',fg='snow',width=30,height=2,command=update_admin)
    b3.pack()
    
    
    
    
    b4=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Go Back',bg='grey',fg='snow',width=30,height=2,command=go_back)
    b4.pack()
    
    
def delete_staff():
    def delete_teacher():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select name||' '||surname,teacher_id
                  from teachers
                  
                  
                  """)
            
        teachers_info=data.fetchall()

        conn.close()
        def delete():
            import funcs as func
            teacher_id=comMember1.get().split()[-1]
            if func.check_teacher(teacher_id):
                func.delete_teacher(teacher_id)
                warn_lab.config(text="Succesfully Deleted",fg='green')
            else:
                warn_lab.config(text="User not Found",fg='red')
           
            
    
        for widget in res_frame.winfo_children():
            widget.destroy()
            
        teacher_label=tkinter.Label(res_frame,text="Teacher",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        teacher_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= teachers_info
        comMember1.place(x=20,y=40)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=70)
    
    
    
        
        
        btn=tkinter.Button(res_frame,command=delete,text='Delete',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=90)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=150)
    



    def delete_student():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select name||' '||surname,student_id
                  from students
                  """)
            
        students_info=data.fetchall()
        conn.commit()
        conn.close()
        
        
        def delete():
            import funcs as func
            student_id=comMember1.get().split()[-1]
            
            if func.check_student([student_id]):
                func.delete_student([student_id])
                warn_lab.config(text="Succesfully Deleted",fg='green')
            else:
                warn_lab.config(text="User not Found",fg='red')
           
            
    
        for widget in res_frame.winfo_children():
            widget.destroy()
            
        student_label=tkinter.Label(res_frame,text="Student",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        student_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= students_info
        comMember1.place(x=20,y=40)
    
        teacher_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        teacher_line.place(x=10,y=70)
    
    
    
        
        
        btn=tkinter.Button(res_frame,command=delete,text='Delete',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=90)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=150)
            
    
        
    def delete_admin():
        conn=sqlite3.connect('coders.db')

        data=conn.execute("""
                  select username,admin_id
                  from admin
                  """)
            
        admin_info=data.fetchall()
        conn.commit()
        conn.close()
        
        
        def delete():
            import funcs as func
            admin_id=comMember1.get().split()[-1]
            
            if func.check_admin([admin_id]):
                func.delete_admin([admin_id])
                warn_lab.config(text="Succesfully Deleted",fg='green')
            else:
                warn_lab.config(text="User not Found",fg='red')
           
            
    
        for widget in res_frame.winfo_children():
            widget.destroy()
            
        admin_label=tkinter.Label(res_frame,text="Admin",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
        admin_label.place(x=10,y=10)

        comMember1= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
        comMember1["values"]= admin_info
        comMember1.place(x=20,y=40)
    
        admin_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
        admin_line.place(x=10,y=70)
    
    
        
        btn=tkinter.Button(res_frame,command=delete,text='Delete',font=('yu gothic vi',12,'bold'),bg='grey',fg='snow',width=30,height=2)
        btn.place(x=10,y=90)
        
        warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
        warn_lab.place(x=10,y=150)
            
    
    
    
    for widget in op_frame.winfo_children():
       widget.destroy()
       
    b1=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Teacher',bg='grey',fg='snow',width=30,height=2,command=delete_teacher)
    b1.pack()
    
    b2=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Student',bg='grey',fg='snow',width=30,height=2,command=delete_student)
    b2.pack()
    
    b3=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Admin',bg='grey',fg='snow',width=30,height=2,command=delete_admin)
    b3.pack()
    
    
    
    
    b4=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Go Back',bg='grey',fg='snow',width=30,height=2,command=go_back)
    b4.pack()
    



b1=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Add Staff',bg='grey',fg='snow',width=30,height=2,command=add_staff)
b1.pack()

b2=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Update Staff',bg='grey',fg='snow',width=30,height=2,command=update_staff)
b2.pack()

b3=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text='Delete Staff',bg='grey',fg='snow',width=30,height=2,command=delete_staff)
b3.pack()
   
home_button=tkinter.Button(op_frame,text='Main Page',font=('yu gothic vi',12,'bold'),command=home,bg='grey',fg='snow',width=30,height=2)
home_button.pack()



    



wrk.mainloop()