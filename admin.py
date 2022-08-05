import tkinter
from PIL import ImageTk,Image
import funcs as func
import get_data

adm=tkinter.Tk()

adm.title('Student LogIn')

adm.resizable(0,0)
adm.state('zoomed')

img = Image.open("login_4.jpg")
bg_img=ImageTk.PhotoImage(img,master=adm)


label_bg = tkinter.Label(adm,image=bg_img,bg='#040405')
label_bg.pack(fill='both',expand='yes')


log_frm=tkinter.Frame(adm,bg='#040405',width=850,height=600)
log_frm.place(x=250,y=100)


head_log=tkinter.Label(log_frm,text="WELCOME",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
head_log.place(x=60,y=30,width=200,height=30)

sign_in=tkinter.Label(log_frm,text="Sign In",font=('yu gothic vi',25,'bold'),bg='#040405',fg='snow')
sign_in.place(x=580,y=140)



vct = Image.open("vec_4.png")
vct = vct.resize((400, 350), Image.ANTIALIAS)
log_img=ImageTk.PhotoImage(vct,master=log_frm)


label_vc = tkinter.Label(log_frm,image=log_img,bg='#040405')
label_vc.place(x=5,y=100)





usr_name=tkinter.Label(log_frm,text="Username",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
usr_name.place(x=500,y=250)


usr_ent=tkinter.Entry(log_frm,font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
usr_ent.place(x=530,y=285,width=270)

usr_line=tkinter.Canvas(log_frm,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
usr_line.place(x=500,y=310)


l_warn=tkinter.Label(log_frm,text='',font=('yu gothic vi',13,'bold'),bg='#040405',fg='red')
l_warn.place(x=500,y=480)



password_label=tkinter.Label(log_frm,text="Password",font=('yu gothic vi',13,'bold'),bg='#040405',fg='snow')
password_label.place(x=500,y=330)


passwrd_ent=tkinter.Entry(log_frm,show='*',font=('yu gothic vi',12,'bold'),highlightthickness=0,relief=tkinter.FLAT,bg='#040405',fg='snow')
passwrd_ent.place(x=530,y=365,width=270)

passw_line=tkinter.Canvas(log_frm,width=300,highlightthickness=0,height=2.0,bg='#bdb9b1')
passw_line.place(x=500,y=390)

def daxil_ol():
    username=usr_ent.get()
    password=passwrd_ent.get()
    if func.select_user_admin(username,password):
        get_data.username=username
        adm.destroy()
        import admin_work
        
    else:
        l_warn.config(text="Could not LogIn")
        


but1=tkinter.Button(log_frm,text='LogIn',font=('yu gothic vi',12,'bold'),command=daxil_ol,bg='grey',fg='snow',width=30,height=2)
but1.place(x=500,y=420)
















adm.mainloop()
