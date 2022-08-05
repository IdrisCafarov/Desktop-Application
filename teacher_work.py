import tkinter
import sqlite3
import get_data
from functools import partial
from tkinter import ttk
import tkcalendar
from PIL import ImageTk,Image


conn=sqlite3.connect('coders.db')

data=conn.execute("""
                  select grp.group_name,grp.group_id
                  from groups grp,teachers tchr
                  where grp.teacher_id=tchr.teacher_id and tchr.username=?
                  
                  """,[get_data.username])

info=data.fetchall()

conn.close()






tc=tkinter.Tk()

tc.resizable(0,0)
tc.state('zoomed')


img = Image.open("bg_tc_4.jpg")


bg_img=ImageTk.PhotoImage(img,master=tc)


label_bg = tkinter.Label(tc,image=bg_img,bg='#040405')
label_bg.pack(fill='both',expand='yes')


log_frm=tkinter.Frame(tc,bg='#040405',width=850,height=600)
log_frm.place(x=250,y=100)

head_log=tkinter.Label(log_frm,text="Welcome Teacher Evaluation System",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
head_log.place(x=120,y=30,height=30)

op_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Operations",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
op_frame.place(x=10,y=70,width=340,height=500)




res_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Operations",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
res_frame.place(x=370,y=70,width=450,height=500)







def home():
    tc.destroy()
    import desk_app_log






def get_students(group_id):
    
        
    conn=sqlite3.connect('coders.db')

    data=conn.execute("""
                  select students.name||' '||students.surname,students.student_id
                  from students,groups
                  where students.group_id=groups.group_id and groups.group_id=?
                  
                  """,group_id)

    students_info=data.fetchall()

    conn.close()
    
    def add_grades():
        import funcs as func
        grade_date=cal.get_date()
        student_grade=grade_ent.get()
        student_id=comMember.get().split()[-1]
        if grade_ent.get().strip()!="":
            
            if func.check_grades(grade_date,student_id):
                if int(student_grade) in [i for i in range(1,101)]:
                    if func.insert_grades(grade_date,student_grade,student_id):
                        warn_lab.config(text='Grade inserted',fg='green')
                else:
                    warn_lab.config(text='Please check the grade',fg='red')
            else:
                func.update_grade(student_id,student_grade,grade_date)
                warn_lab.config(text='Grade Correctly Updated',fg='green')
        else:
            warn_lab.config(text='Grade is Empty',fg='red')
    
    
    for widget in res_frame.winfo_children():
            widget.destroy()

    student_label=tkinter.Label(res_frame,text="Student",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
    student_label.place(x=10,y=10)

    comMember= ttk.Combobox(res_frame,font=('yu gothic vi',12,'bold'), width=18, state="readonly")
    comMember["values"]= students_info
    comMember.place(x=20,y=40)
    
    student_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
    student_line.place(x=10,y=70)
    
    
    
    
    grade_label=tkinter.Label(res_frame,text="Mark",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
    grade_label.place(x=10,y=80)
    
    grade_ent=tkinter.Entry(res_frame,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='white',fg='black')
    grade_ent.place(x=20,y=105)
    
    grade_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
    grade_line.place(x=10,y=135)
    
    
    
    cal=tkcalendar.Calendar(res_frame,selectmode='day')
    cal.place(x=20,y=145)
    
    cal_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
    cal_line.place(x=10,y=340)
    
    but1=tkinter.Button(res_frame,text='Submit',font=('yu gothic vi',12,'bold'),command=add_grades,bg='grey',fg='snow',width=30,height=2)
    but1.place(x=10,y=350)
    
    
    warn_lab=tkinter.Label(res_frame,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
    warn_lab.place(x=10,y=400)
   


for i in info:
    button=tkinter.Button(op_frame,font=('yu gothic vi',12,'bold'),text=i[0],command=partial(get_students,i[1]),bg='grey',fg='snow',width=30,height=2)
    button.pack()


home_button=tkinter.Button(op_frame,text='Main Page',font=('yu gothic vi',12,'bold'),command=home,bg='grey',fg='snow',width=30,height=2)
home_button.pack()











tc.mainloop()