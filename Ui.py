from tkinter import *
from tkinter import messagebox
import database
win=Tk()
win.geometry('400x400')
win.title('Login From')
win.resizable(0,0)
#=======function(s)============
database.craet_table()
def vorod():
    if ent_fname.get()=='' or ent_lname.get()=='':
        messagebox.showerror('Entry error','one of name entrys is empty!')
    elif ent_email.get()=='' or ent_password.get()=='' :
        messagebox.showerror('Entry error','one of mandatory entrys is empty!')
    elif len(ent_email.get())<18 or ent_email.get().count('@')<1:
        messagebox.showerror('Email error',"Your email is wrong!")
    elif len(ent_password.get())<8:
        messagebox.showerror('Passwor error','The minimum number of pssword character is 8 character!')
    else:
        database.signup(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_password.get())
        messagebox.showinfo('login','Login was euccessful')
def vorod_2():
    d=database.signin(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_password.get())
    if d:
        messagebox.showinfo('login  info','you have registered before')
    else:
        messagebox.showerror('login error','you have not registered before')
def show():
    if i.get()==1:
        ent_password.config(show='')
    else:
        ent_password.config(show='*')
#===========for design==============
lbl_fname=Label(win,text='Fname:',font='bold').place(x=30,y=20)
lbl_lname=Label(win,text='Lname:',font='bold').place(x=30,y=90)
lbl_email=Label(win,text='Email:',font='bold').place(x=25,y=160)
lbl_password=Label(win,text='Password:',font='bold').place(x=25,y=220)
ent_fname=Entry(win)
ent_fname.place(x=120,y=20)
ent_lname=Entry(win)
ent_lname.place(x=120,y=90)
ent_email=Entry(win)
ent_email.place(x=120,y=160)
ent_password=Entry(win,show='*')
ent_password.place(x=120,y=220)
i=IntVar()
c_box=Checkbutton(win,command=show,text='show password',variable=i)
c_box.place(x=120,y=250)
btn_signin=Button(win,text='sign up',font='bold',command=vorod)
btn_signin.place(x=90,y=350)  
btn_signup=Button(win,text='sign in',font='bold',command=vorod_2)
btn_signup.place(x=260,y=350)
messagebox.showinfo('All you need to do to sign up','The minimum number of pssword character is 8 character ,'
' You must complete all entrys to register ,You must enter your email correctly  ')
messagebox.showinfo('Description',"if you have already done a 'Sign up' you can sign in")
win.mainloop()