import tkinter
import sqlite3
import get_data
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image


conn=sqlite3.connect('coders.db')

data=conn.execute("""
                  select grades.grade_date,grades.student_grade
                  from students,grades
                  where students.student_id=grades.student_id and students.username=?
                  
                  """,[get_data.username])

grade_info=data.fetchall()


conn.close()

conn=sqlite3.connect('coders.db')
data=conn.execute("""
                  select students.student_id,students.name||' '||students.surname,groups.group_name
                  from students,grades,groups
                  where students.student_id=grades.student_id and students.group_id=groups.group_id and students.username=?
                  
                  """,[get_data.username])

student_info=data.fetchall()

conn.close()




st=tkinter.Tk()

st.resizable(0,0)
st.state('zoomed')


img = Image.open("student_work_bg.jpg")


bg_img=ImageTk.PhotoImage(img,master=st)


label_bg = tkinter.Label(st,image=bg_img,bg='#040405')
label_bg.pack(fill='both',expand='yes')


log_frm=tkinter.Frame(st,bg='#040405',width=850,height=600)
log_frm.place(x=250,y=100)

head_log=tkinter.Label(log_frm,text="Welcome Student Page",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
head_log.place(x=120,y=30,height=30)

op_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Personal Data",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
op_frame.place(x=10,y=70,width=340,height=500)




res_frame=tkinter.LabelFrame(log_frm,font=('yu gothic vi',15,'bold'),text = "Grades",bd=30,highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
res_frame.place(x=370,y=70,width=450,height=500)


student_id=tkinter.Label(op_frame,text="Student ID",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
student_id.place(x=10,y=10)

    
idd=tkinter.Label(op_frame,text=student_info[0][0],font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
idd.place(x=20,y=40)

    
id_line=tkinter.Canvas(op_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
id_line.place(x=10,y=70)


student_name=tkinter.Label(op_frame,text="Student Name",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
student_name.place(x=10,y=80)
    
name=tkinter.Label(op_frame,text=student_info[0][1],font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
name.place(x=20,y=105)
    
name_line=tkinter.Canvas(op_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
name_line.place(x=10,y=135)
    


group_name=tkinter.Label(op_frame,text="Group Name",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
group_name.place(x=10,y=145)
    
namee=tkinter.Label(op_frame,text=student_info[0][2],font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
namee.place(x=20,y=170)
    
group_line=tkinter.Canvas(op_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
group_line.place(x=10,y=200)





columns = ('date', 'mark')
tree = ttk.Treeview(res_frame, columns=columns, show='headings')


tree.heading('date', text='Lesson Date')
tree.heading('mark', text='Lesson Mark')



for contact in grade_info:
    tree.insert('', tkinter.END, values=contact)


tree.grid(row=0, column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(res_frame, orient=tkinter.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

def home():
    st.destroy()
    import desk_app_log

def overall():
    sum1=0
    count=0
    for x in grade_info:
        sum1+=x[1]
        count+=1
    return round(sum1/count,2)

x=overall()
overall_lab=tkinter.Label(res_frame,text='Overall',font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
overall_lab.place(x=10,y=250)


overall=tkinter.Label(res_frame,text=x,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
overall.place(x=20,y=275)

overall_line=tkinter.Canvas(res_frame,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
overall_line.place(x=10,y=305)



home_button=tkinter.Button(res_frame,text='Main Page',font=('yu gothic vi',12,'bold'),command=home,bg='grey',fg='snow',width=30,height=2)
home_button.place(x=10,y=350)






st.mainloop()  
    
    