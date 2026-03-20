from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Student Form")
try:
    root.iconbitmap("pixel2.ico")
except Exception:
    pass

root.geometry('500x500+0+0')
root.configure(background='#00704A')

bg_img = Image.open("dandadan.png") 
bg_img = bg_img.resize((1920, 1080))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# image
try:
    img = Image.open('star.png')
    resize_img = img.resize((100,70))
    img = ImageTk.PhotoImage(resize_img)
    img_label = Label(root,image = img)
    img_label.pack(pady=10,padx=20)
except Exception:
    pass

# text label
text_label = Label(root,text="all HD anime",font=('Arial', 18,'bold'),bg="#29282A",fg='white')
text_label.pack(pady=10,padx=20)

email_label = Label(root,text="Email ID",font=('Arial', 18,'bold'),bg="#159369",fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='white')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 18,'bold'),bg="#0CC285",fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 18,'bold'),fg='white',bg='lightblue', show="*") 
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 18,'bold'),bg="#111513",fg='white')
login_btn.pack(pady=(5,10))

root.mainloop()
