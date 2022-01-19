from tkinter import *

def createwindow():
    root = Tk()
    root.title("Registration Form by Soravith")
    root.geometry('600x600')
    root.configure(bg='#f2f2f2')
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    return root

def contentwindow(root):
    # Content
    title_Reg = Label(root, text="Registration Form", fg='#19a9fc')
    title_Reg.configure(font=("Product Sans", 25, "bold"))

    title_name = Label(root, text="Name :", fg='#242424')
    title_name.configure(font=("Product Sans", 15))
    box_name = Entry(width=40, bg='#ffffff')

    title_email = Label(root, text="Email :", fg='#242424')
    title_email.configure(font=("Product Sans", 15))
    box_email = Entry(width=40, bg='#ffffff')

    title_gender = Label(root, text='Gender :', fg='#242424')
    title_gender.configure(font=("Product Sans", 15))
    rad_male = Radiobutton(root, text="Male", bg='#f2f2f2', value="1")
    rad_male.configure(font=("Product Sans", 13))
    rad_female = Radiobutton(root, text="Female", bg='#f2f2f2', value="2")
    rad_female.configure(font=("Product Sans", 13))
    rad_other = Radiobutton(root, text="Other", bg='#f2f2f2', value="3")
    rad_other.configure(font=("Product Sans", 13))

    title_phone = Label(root, text="Phone Number:", fg='#242424')
    title_phone.configure(font=("Product Sans", 15))
    box_phone = Entry(width=40, bg='#ffffff')

    title_user = Label(root, text="Username:", fg='#242424')
    title_user.configure(font=("Product Sans", 15))
    box_user = Entry(width=40, bg='#ffffff')

    title_password = Label(root, text="Password:", fg='#242424')
    title_password.configure(font=("Product Sans", 15))
    box_password = Entry(width=40, bg='#ffffff')

    title_security = Label(root, text="Security Question:", fg='#242424')
    title_security.configure(font=("Product Sans", 15))
    box_security = Entry(width=40, bg='#ffffff')

    title_answer = Label(root, text="Answer:", fg='#242424')
    title_answer.configure(font=("Product Sans", 15))
    box_answer = Entry(width=40, bg='#ffffff')

    butt_cancel = Button(root, text="Cancel", bg="#e01f39", width=15, height=2, font="Product 13 bold ")
    butt_cancel.configure(font=("Product Sans", 13))

    butt_reg = Button(root, text="Register", bg="#19a9fc", width=15, height=2, font="Product 13 bold")
    butt_reg.configure(font=("Product Sans", 13))

    # Show on Screen
    title_Reg.grid(column=0, row=0, columnspan=2, ipady=20,)

    title_name.grid(row=1, column=0, ipadx=50, ipady=5, sticky="w")
    box_name.grid(row=1, column=1, ipady=3, sticky="w")

    title_email.grid(row=2, column=0, ipadx=50, ipady=5, sticky="w")
    box_email.grid(row=2, column=1, ipady=3, sticky="w")

    title_gender.grid(row=3, column=0, ipadx=50, ipady=5, sticky="w")
    rad_male.grid(row=3, column=1, ipady=2, sticky="w")
    rad_female.grid(row=4, column=1, ipady=2, sticky="w")
    rad_other.grid(row=5, column=1, ipady=2, sticky="w")

    title_phone.grid(row=6, column=0, ipadx=50, ipady=5, sticky="w")
    box_phone.grid(row=6, column=1, ipady=3, sticky="w")

    title_user.grid(row=7, column=0, ipadx=50, ipady=5, sticky="w")
    box_user.grid(row=7, column=1, ipady=3, sticky="w")

    title_password.grid(row=8, column=0, ipadx=50, ipady=5, sticky="w")
    box_password.grid(row=8, column=1, ipady=3, sticky="w")

    title_security.grid(row=9, column=0, ipadx=50, ipady=5, sticky="w")
    box_security.grid(row=9, column=1, ipady=3, sticky="w")

    title_answer.grid(row=10, column=0, ipadx=50, ipady=5, sticky="w")
    box_answer.grid(row=10, column=1, ipady=3, sticky="w")

    butt_cancel.grid(row=11, column=0, pady=30, padx=20, sticky="e")

    butt_reg.grid(row=11, column=1, pady=30, padx=20, sticky="w")
    
root = createwindow()
contentwindow(root)
root.mainloop()