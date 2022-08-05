import tkinter
from PIL import ImageTk,Image
import tkcalendar



log=tkinter.Tk()
log.title('Main Page') 

log.resizable(0,0)
log.state('zoomed')

img = Image.open("bg.jpg")
bg_img=ImageTk.PhotoImage(img,master=log)



label_bg = tkinter.Label(log,image=bg_img,bg='grey')
label_bg.place(x=0, y=0, relwidth=1, relheight=1)


log_frm=tkinter.Frame(log,bg='#040405',width=650,height=400)
log_frm.place(x=30,y=150)


head_log=tkinter.Label(log_frm,text="Welcome to Coders Azerbaijan",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
head_log.place(x=30,y=30)





def admin_tk():
    log.destroy()
    import admin
    
def teacher_tk():
    log.destroy()
    import teacher
    
    
def student_tk():
    log.destroy()
    import student_log


b1=tkinter.Button(log_frm,font=('yu gothic vi',12,'bold'),text='Login as Admin',bg='grey',fg='snow',width=30,height=2,command=admin_tk)
b1.place(x=150,y=90)

b2=tkinter.Button(log_frm,font=('yu gothic vi',12,'bold'),text='Login as Teacher',bg='grey',fg='snow',width=30,height=2,command=teacher_tk)
b2.place(x=150,y=150)


b3=tkinter.Button(log_frm,font=('yu gothic vi',12,'bold'),text='Login as Student',bg='grey',fg='snow',width=30,height=2,command=student_tk)
b3.place(x=150,y=210)



log.mainloop()