import sqlite3
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkcalendar import DateEntry
from tkVideoPlayer import TkinterVideo
from password_strength import PasswordStats

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('DB\DB_Holiday.db')
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.resizable(False,False)
    root.config(bg='#ffffff')
    root.title("Holiday")
    root.option_add('*font',("Product Sans", 20))
    videoplayer = TkinterVideo(master=root, scaled=True)
    videoplayer.load(r"video\logo.mp4")
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    return root

def mainlayout():
    global mainframe
    mainframe = Frame(root, bg='#ffffff')
    mainframe.place(x=0, y=0, width=w, height=h)
    mainframe.rowconfigure(0, weight=10)  
    Label(mainframe, image=main_img1,bg="#ffffff").place(x=185,y=206)
    Button(mainframe, image=main_img2, foreground='#ffffff',bg='#ffffff',bd=0,command=loginlayout).place(x=689,y=321)
    Button(mainframe, image=main_img3, foreground='#ffffff',bg='#ffffff',bd=0,command=signuplayout).place(x=689,y=425)

def usertext(event):
    userentry.delete(0, END)
    userentry.config(fg='black')

def passtext(event):
    passentry.delete(0, END)
    passentry.config(show='•')
    passentry.config(fg='black')

def loginlayout():
    global userentry,passentry,loginframe
    mainframe.destroy
    root.title("Login")
    loginframe = Frame(root, bg='#ffffff')
    loginframe.place(x=0, y=0, width=w, height=h)
    loginframe.rowconfigure(0, weight=10)  
    Label(loginframe, image=login_img1,bg="#ffffff").place(x=185,y=206)

    Label(loginframe, image=login_img3,bg="#ffffff",).place(x=725,y=257)
    userentry = Entry(loginframe, bg='#ffffff',bd=0, fg='#398AB9',textvariable=userinfo,width=18)
    userentry.insert(0,' Email')
    userentry.bind("<Button>",usertext)
    userentry.place(x=800,y=260)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=300)

    Label(loginframe, image=login_img2,bg="#ffffff").place(x=725,y=346)
    passentry = Entry(loginframe, bg='#ffffff',bd=0, fg='#398AB9',textvariable=passinfo,width=18)
    passentry.insert(0,' Password')
    passentry.bind("<Button>",passtext)
    passentry.place(x=800,y=350)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=390)

    Button(loginframe, image=login_img5, foreground='#ffffff',bg='#ffffff',bd=0,command=backsignup).place(x=813,y=432)
    Button(loginframe, image=login_img4, foreground='#ffffff',bg='#ffffff',bd=0,command=loginclick).place(x=787,y=516)

def backsignup():
    loginframe.destroy
    userentry.delete(0,END)
    passentry.delete(0, END)
    signuplayout()

def loginclick():
    global resultuser
    if userentry.get() == "" or passentry.get() == "":
        messagebox.showwarning("Admin: ", "Enter email or password first")
        userentry.focus_force()
    else:
        sql = "select * from Login where email=? and password=?"
        cursor.execute(sql, [userinfo.get().upper(), passinfo.get()])
        resultuser = cursor.fetchall()
        print(resultuser)
        if resultuser:
            messagebox.showinfo("Admin : ", "Login Successfuly")
            flightlayout()
            userentry.delete(0, END)
            passentry.delete(0, END)
        else:
            sql = "select * from Admin where user=? and password=?"
            cursor.execute(sql, [userinfo.get(), passinfo.get()])
            result = cursor.fetchall()
            print(result)
            if result:
                messagebox.showinfo("Admin : ", "Login Successfuly")
                addmin()
                userentry.delete(0, END)
                passentry.delete(0, END)
            else:
                messagebox.showwarning("Admin","Incorrect Username or password")
                userentry.select_range(0, END)
                userentry.focus_force()

def newfirstnametext(event):
    newfirstname.delete(0,END)
    newfirstname.config(fg='black')

def newlastnametext(event):
    newlastname.delete(0,END)
    newlastname.config(fg='black')

def newemailtext(event):
    newemail.delete(0,END)
    newemail.config(fg='black')

def newpasstext(event):
    newpass.delete(0,END)
    newpass.config(show='•')
    newpass.config(fg='black')

def newconfirpasstext(event):
    newconfirpass.delete(0,END)
    newconfirpass.config(show='•')
    newconfirpass.config(fg='black')

def signuplayout():
    global newfirstname,newlastname,newemail,newpass,newconfirpass,signupframe,f2color,passtag
    mainframe.destroy
    root.title("Sign up")
    signupframe = Frame(root, bg='#ffffff')
    signupframe.place(x=0, y=0, width=w, height=h)
    signupframe.rowconfigure(0, weight=10)  
    Label(signupframe, image=singup_img1,bg="#ffffff").place(x=185,y=206)

    newemail = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newemailinfo)
    newemail.insert(0,' Email')
    newemail.bind("<Button>",newemailtext)
    newemail.place(x=800,y=123)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=163)

    newfirstname = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newfnameinfo)
    newfirstname.insert(0,' Firstname')
    newfirstname.bind("<Button>",newfirstnametext)
    newfirstname.place(x=800,y=213)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=253)
    
    newlastname = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newlnameinfo)
    newlastname.insert(0,' Lastname')
    newlastname.bind("<Button>",newlastnametext)
    newlastname.place(x=800,y=303)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=343)
    
    passtag = Label(signupframe, text=" ",bg="#ffffff",fg="#ffffff")
    passtag.place(x=1015,y=390)
    newpass = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=12,textvariable=newpwdinfo)
    newpass.insert(0,' Password')
    newpass.bind("<Button>",newpasstext)
    newpass.bind("<Key>",checkpass)
    newpass.place(x=800,y=393)
    f2color = Frame(width=300,height=3,bg="#D8D2CB")
    f2color.place(x=800,y=433)
    
    newconfirpass = Entry(signupframe, bg='#ffffff',bd=0, fg='#398AB9',width=18,textvariable=newconfirpwdinfo)
    newconfirpass.insert(0,' Confirm password')
    newconfirpass.bind("<Button>",newconfirpasstext)
    newconfirpass.place(x=800,y=487)
    Frame(width=300,height=3,bg="#D8D2CB").place(x=800,y=527)

    Button(signupframe, image=singup_img2, foreground='#ffffff',bg='#ffffff',bd=0,command=backlogin).place(x=789,y=582)
    Button(signupframe, image=singup_img3, foreground='#ffffff',bg='#ffffff',bd=0,command=registration).place(x=825,y=647)

def checkpass(event):
    if len(newpass.get()) >= 2:
        result=PasswordStats(newpass.get())
        final=result.strength()
        print(final)
        if final >= 0.40:
            f2color.config(bg="#27cf54")
            passtag.config(text="Strong",fg="#27cf54")
        elif final > 0.10 and final < 0.20:
            f2color.config(bg="#F0A500")
            passtag.config(text="Good",fg="#F0A500")
        elif final <= 0.10:
            f2color.config(bg="#D0312D")
            passtag.config(text="Weak",fg="#D0312D")
 
def nicetomeetyoulayout():
    global ntmyframe
    ntmyframe = Frame(root, bg='#ffffff')
    ntmyframe.place(x=0, y=0, width=w, height=h)
    ntmyframe.rowconfigure((1,2,3), weight=1)
    ntmyframe.rowconfigure((0,4), weight=4)
    ntmyframe.columnconfigure(0,weight=1)

    Label(ntmyframe, image=ntmy_img1,bg="#ffffff").grid(row=1, column=0)
    Label(ntmyframe, text="Nice To Meet You !!!",fg='#398AB9',font=("Product Sans", 40),bg="#ffffff").grid(row=2, column=0)
    Label(ntmyframe, text=newfnameinfo.get(),fg='#398AB9',font=("Product Sans", 40, "bold"),bg="#ffffff").grid(row=3, column=0,sticky=N)

    newfirstname.delete(0,END)
    newlastname.delete(0,END)
    newemail.delete(0,END)
    newpass.delete(0,END)
    newconfirpass.delete(0,END)
    
    root.after(2000,loginlayout)

def backlogin():
    signupframe.destroy
    newfirstname.delete(0,END)
    newlastname.delete(0,END)
    newemail.delete(0,END)
    newpass.delete(0,END)
    newconfirpass.delete(0,END)
    loginlayout()

def registration() :
    print(newemailinfo.get())
    sql_chk = "SELECT * FROM Login WHERE email= ?"
    cursor.execute(sql_chk,[newemailinfo.get()])
    chk_result = cursor.fetchall()
    print(chk_result)
    if chk_result:
        messagebox.showwarning("Admin", 'This Email already use')
        newemail.focus_force()
        newemail.select_range(0,END)
    else:
        if newemailinfo.get() == " Email":
            messagebox.showwarning("Admin", 'Please enter your Email')
            newemail.focus_force()
        elif newfnameinfo.get() == " Firstname":
            messagebox.showwarning("Admin", 'Please enter your Firstname')
            newfirstname.focus_force()
        elif newlnameinfo.get() == " Lastname":
            messagebox.showwarning("Admin", 'Please enter your Lastname')
            newlastname.focus_force()
        elif newpwdinfo.get() == " Password":
            messagebox.showwarning("Admin", 'Please enter your password')
            newpass.focus_force()
        elif newconfirpwdinfo.get() == " Confirm password":
            messagebox.showwarning("Admin","Please enter your Confirm Password")
            newconfirpass.focus_force()
        else:
            if newpwdinfo.get() == newconfirpwdinfo.get():
                sql_ins = 'INSERT INTO Login VALUES (?,?,?,?)'
                cursor.execute(sql_ins, [newfnameinfo.get(),newlnameinfo.get(),newemailinfo.get().upper(),newpwdinfo.get()])
                conn.commit()
                retrivedata()
                nicetomeetyoulayout()
            else:
                 messagebox.showwarning("admin",'Confirm password is not matched')

def flightlayout():
    global flightframe, calenderpick
    flightframe = Frame(root, bg='#F5F2F2')
    flightframe.place(x=0, y=0, width=w, height=h)
    flightframe.rowconfigure((1,2,3), weight=1)
    flightframe.rowconfigure((0,4), weight=4)
    flightframe.columnconfigure(0,weight=1)

    Label(flightframe,text="Flight Details",bg="#F5F2F2",fg='#398AB9',font=("Product Sans", 25, "bold")).place(x=180,y=20)

    Label(flightframe,image=flight_img1,bg="#F5F2F2").place(x=-3,y=0)

    Button(flightframe,image=flight_img2,activebackground='#398AB9',bg="#398AB9",bd=0,command=logout).place(x=20,y=715)

    Button(flightframe,image=flight_img16,activebackground='#398AB9',bg="#398AB9",bd=0,command=profilelayout).place(x=20,y=140)

    Label(flightframe,image=flight_img3,bg="#F5F2F2").place(x=155,y=80)
    
    s = ttk.Style()
    s.configure("TMenubutton",font=("Product Sans", 15),background="#ffffff",foreground='#398AB9')

    fromoptions_list = ["Departure","Bangkok | BKK","Chiang Mai | CNX","Chiang Rai | CEI","Hat Yai | HDY","Hua Hin | HHQ","Khon Kaen | KKC","Koh Samui | USM","Krabi | KBV","Mae Hong Son | HGN","Nakhon Phanom | KOP","Nakhon Si Thammarat | NST","Pattaya | UTPA","Phuket | HKT","Surat Thani | URT","Trat | TDX","Ubon Ratchathani | UBP","Udon Thani | UTH"]
    fromoption = ttk.OptionMenu(flightframe,fromoptioninfo,*fromoptions_list)
    fromoption.place(x=230,y=105)

    Label(flightframe,image=flight_img4,bg="#F5F2F2").place(x=535,y=80)

    toptions_list = ["Destination","Bangkok | BKK","Chiang Mai | CNX","Chiang Rai | CEI","Hat Yai | HDY","Hua Hin | HHQ","Khon Kaen | KKC","Koh Samui | USM","Krabi | KBV","Mae Hong Son | HGN","Nakhon Phanom | KOP","Nakhon Si Thammarat | NST","Pattaya | UTPA","Phuket | HKT","Surat Thani | URT","Trat | TDX","Ubon Ratchathani | UBP","Udon Thani | UTH"]
    tooption = ttk.OptionMenu(flightframe,tooptioninfo,*toptions_list)
    tooption.place(x=610,y=105)

    Label(flightframe,image=flight_img5,activebackground='#F5F2F2',bg="#F5F2F2",bd=0).place(x=920,y=80)

    calenderpick = DateEntry(flightframe, width=5, background='#398AB9',foreground='#F5F2F2',font=("Product Sans", 15))
    calenderpick.place(x=1020,y=105)

    person = Spinbox(flightframe, from_=0, to=99,textvariable=personinfo,width=2, justify=CENTER, fg='#398AB9', bd=0, font=("Product Sans", 16, "bold"))
    person.place(x=1120,y=105)
    personinfo.set(1)

    Button(flightframe,image=flight_img7,activebackground='#F5F2F2',bg="#F5F2F2",bd=0,command=warning).place(x=1200,y=80)

def logout():
    flightframe.destroy
    mainlayout()

def warning():
    if fromoptioninfo.get() == "Departure":
        messagebox.showwarning("let's holiday", 'Please enter your Departure')
    elif tooptioninfo.get() == "Destination":
        messagebox.showwarning("let's holiday", 'Please enter your Destination')
    else:
        search()

def search():
    global result
    status = "yes"
    sql = "SELECT * FROM Flights WHERE from_dep= ? AND to_arr=? " 
    cursor.execute(sql,[fromoptioninfo.get(), tooptioninfo.get()])

    sql = "SELECT * FROM Flights WHERE day=? " 
    cursor.execute(sql,[calenderpick.get_date()])
    result = cursor.fetchall()
    
    searchframe = Frame(root, bg='#F5F2F2')
    searchframe.place(x=165, y=180, width=1050, height=620)
    searchframe.columnconfigure((0,1,2,3,4),weight=1)
    
    s = ttk.Style()
    s.configure('TButton',background="#F5F2F2")

    canvas = Canvas(searchframe, width=1100, height=620)
    
    scrollbar = ttk.Scrollbar(searchframe, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right",fill=Y)
    scrollable_frame = ttk.Frame(canvas,style='TButton')
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for i,data in enumerate(result):
        if data[1] == "Thai Airasia":
            frame1 = Frame(scrollable_frame, bg='#ffffff',height=151,width=904)
            frame1.grid(row=i+0,columnspan=3)
            Label(frame1,image=flight_img11,bg="#ffffff").grid(row=0,columnspan=4)
            Label(frame1,text=data[0],bg="#ffffff",font=("Product Sans", 15, "bold")).place(x=149, y=47)
            Label(frame1,text=data[1],bg="#ffffff",font=("Product Sans", 15,)).place(x=149, y=78)
            Label(frame1,text="%s\n%s"%(data[2],data[5]),bg="#ffffff",font=("Product Sans", 12,)).place(x=280, y=55)
            Label(frame1,text="%s\n%s"%(data[3],data[6]),bg="#ffffff",font=("Product Sans", 12,)).place(x=545, y=55)
            Label(frame1,text="%s฿"%(data[8]*personinfo.get()),bg="#ffffff",font=("Product Sans", 20,)).place(x=790, y=65)
            Button(frame1,image=flight_img17,bd=0,bg="#ffffff",command=lambda i=i :flightdetaillayout(i,data)).grid(row=0,column=4,sticky="E")

        elif data[1] == "Thai Smile":
            frame2 = Frame(scrollable_frame, bg='#ffffff',height=151,width=904)
            frame2.grid(row=i+0,columnspan=3)
            Label(frame2,image=flight_img14,bg="#ffffff").grid(row=0,columnspan=4)
            Label(frame2,text=data[0],bg="#ffffff",font=("Product Sans", 15, "bold")).place(x=149, y=47)
            Label(frame2,text=data[1],bg="#ffffff",font=("Product Sans", 15,)).place(x=149, y=78)
            Label(frame2,text="%s\n%s"%(data[2],data[5]),bg="#ffffff",font=("Product Sans", 12,)).place(x=280, y=55)
            Label(frame2,text="%s\n%s"%(data[3],data[6]),bg="#ffffff",font=("Product Sans", 12,)).place(x=545, y=55)
            Label(frame2,text="%s฿"%(data[8]*personinfo.get()),bg="#ffffff",font=("Product Sans", 20,)).place(x=790, y=65)
            Button(frame2,image=flight_img17,bd=0,bg="#ffffff",command=lambda i=i :flightdetaillayout(i,data)).grid(row=0,column=4,sticky="E")
        
        elif data[1] == "Thai Lion Air":
            frame3 = Frame(scrollable_frame, bg='#ffffff',height=151,width=904)
            frame3.grid(row=i+0,columnspan=3)
            Label(frame3,image=flight_img12,bg="#ffffff").grid(row=0,columnspan=4)
            Label(frame3,text=data[0],bg="#ffffff",font=("Product Sans", 15, "bold")).place(x=149, y=47)
            Label(frame3,text=data[1],bg="#ffffff",font=("Product Sans", 15,)).place(x=149, y=78)
            Label(frame3,text="%s\n%s"%(data[2],data[5]),bg="#ffffff",font=("Product Sans", 12,)).place(x=280, y=55)
            Label(frame3,text="%s\n%s"%(data[3],data[6]),bg="#ffffff",font=("Product Sans", 12,)).place(x=545, y=55)
            Label(frame3,text="%s฿"%(data[8]*personinfo.get()),bg="#ffffff",font=("Product Sans", 20,)).place(x=790, y=65)
            Button(frame3,image=flight_img17,bd=0,bg="#ffffff",command=lambda i=i :flightdetaillayout(i,data)).grid(row=0,column=4,sticky="E")

        elif data[1] == "Nokair":
            frame4 = Frame(scrollable_frame, bg='#ffffff',height=151,width=904)
            frame4.grid(row=i+0,columnspan=3)
            Label(frame4,image=flight_img13,bg="#ffffff").grid(row=0,columnspan=4)
            Label(frame4,text=data[0],bg="#ffffff",font=("Product Sans", 15,"bold")).place(x=149, y=47)
            Label(frame4,text=data[1],bg="#ffffff",font=("Product Sans", 15,)).place(x=149, y=78)
            Label(frame4,text="%s\n%s"%(data[2],data[5]),bg="#ffffff",font=("Product Sans", 12,)).place(x=280, y=55)
            Label(frame4,text="%s\n%s"%(data[3],data[6]),bg="#ffffff",font=("Product Sans", 12,)).place(x=545, y=55)
            Label(frame4,text="%s฿"%(data[8]*personinfo.get()),bg="#ffffff",font=("Product Sans", 20,)).place(x=790, y=65)
            Button(frame4,image=flight_img17,bd=0,bg="#ffffff",command=lambda i=i :flightdetaillayout(i,data)).grid(row=0,column=4,sticky="E")

    canvas.place(x=0,y=0)
    scrollbar.pack(side="right", fill="y")

    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

def flightdetaillayout(i,data):
    global flightdetaillframe
    flightdetaillframe = Frame(root, bg='#ffffff')
    flightdetaillframe.place(x=0, y=0, width=w, height=h)
    flightdetaillframe.rowconfigure((0,1), weight=4)
    flightdetaillframe.columnconfigure((0,1,),weight=1)

    Label(flightdetaillframe,image=flight_img1,bg="#ffffff").place(x=-3,y=0)    
    
    Label(flightdetaillframe,text="Flight Details",fg="#398AB9",bg="#ffffff",font=("Product Sans", 30,)).place(x=180,y=40)


    Label(flightdetaillframe,image=flight_img18,bg="#ffffff").place(x=180,y=130)
    
    Label(flightdetaillframe,text=result[i][1],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=287,y=155)
    Label(flightdetaillframe,text=result[i][0],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=287,y=190)

    Label(flightdetaillframe,text=result[i][9],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=640,y=170)

    Label(flightdetaillframe,text=result[i][2],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=270,y=260)
    Label(flightdetaillframe,text=result[i][5],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=270,y=295)

    Label(flightdetaillframe,text=result[i][4],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=270,y=390)

    Label(flightdetaillframe,text=result[i][3],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=270,y=475)
    Label(flightdetaillframe,text=result[i][6],fg="#262626",bg="#EFEFEF",font=("Product Sans", 18,)).place(x=270,y=510)

    Label(flightdetaillframe,text="Plane type",fg="#262626",bg="#EFEFEF",font=("Product Sans", 15,)).place(x=590,y=230)
    Label(flightdetaillframe,text=result[i][10],fg="#262626",bg="#EFEFEF",font=("Product Sans", 20,)).place(x=590,y=260)

    Label(flightdetaillframe,image=flight_img19,bg="#ffffff").place(x=848,y=130)

    Label(flightdetaillframe,text="Price breakdown",fg="#ffffff",bg="#398AB9",font=("Product Sans", 20,)).place(x=880,y=155)

    Label(flightdetaillframe,text="Person",fg="#262626",bg="#EFEFEF",font=("Product Sans", 20,)).place(x=880,y=230)

    Label(flightdetaillframe,text=personinfo.get(),fg='#398AB9',bg="#EFEFEF",font=("Product Sans", 20, "bold")).place(x=880,y=273)

    Label(flightdetaillframe,text="%s฿"%(result[i][8]*personinfo.get()),fg="#262626",bg="#EFEFEF",font=("Product Sans", 20,)).place(x=1150,y=273)

    Label(flightdetaillframe,text="Total",fg="#262626",bg="#EFEFEF",font=("Product Sans", 20,)).place(x=880,y=460)

    Label(flightdetaillframe,text="%0.2f฿"%(result[i][8]*personinfo.get()+200),fg='#398AB9',bg="#EFEFEF",font=("Product Sans", 20, "bold")).place(x=1100,y=460)
    
    Button(flightdetaillframe,image=flight_img25,bg="#ffffff",command=flightdetaillframe.destroy,font=("Product Sans", 20, "bold"),bd=0).place(x=850,y=670)

    Button(flightdetaillframe,image=flight_img26,bg="#ffffff",command=lambda:paylayout(i,data),font=("Product Sans", 20, "bold"),bd=0).place(x=1020,y=670)

def retrivedata() :
    sql = "select * from Login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

def addmin():
    global addminframe,mytree,search_box
    global fn,al,dp,ar,ft,dt,at,st,pr,date,pt
    addminframe = Frame(root, bg='#ffffff')
    addminframe.place(x=0, y=0, width=w, height=h)
    addminframe.rowconfigure(0, weight=30)
    addminframe.rowconfigure((1,2,3,4,5,6), weight=1)
    addminframe.rowconfigure(7, weight=2)
    addminframe.columnconfigure((1,2,3,4),weight=1)
    addminframe.columnconfigure(5,weight=5)
    addminframe.columnconfigure(0,weight=2)
    Label(addminframe,image=flight_img1,bg="#ffffff").place(x=-3,y=0)
    
    Label(addminframe,image=flight_img3,bg="#ffffff").place(x=183,y=50)    

    search_box = Entry(addminframe, width=10, font=("Product Sans", 20),bd=0)
    search_box.place(x=210 ,y=75)

    Button(addminframe,image=flight_img2,activebackground='#398AB9',bg="#398AB9",bd=0,command=logoutaddmin).place(x=20,y=715)

    Button(addminframe,image=flight_img7,activebackground='#ffffff',bg="#ffffff",bd=0,command=fetchSearch).place(x=570,y=50)

    mytree = ttk.Treeview(addminframe, columns=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11'))
    mytree.place(x=183, y=174)

    mytree.heading('col1',text='Flight Number', anchor=CENTER)
    mytree.heading('col2',text='Airlines', anchor=CENTER)
    mytree.heading('col3',text='Departure', anchor=CENTER)
    mytree.heading('col4',text='Arrival', anchor=CENTER)
    mytree.heading('col5',text='Flight Time', anchor=CENTER)
    mytree.heading('col6',text='Departure Time', anchor=CENTER)
    mytree.heading('col7',text='Arrival Time', anchor=CENTER)
    mytree.heading('col8',text='Seats', anchor=CENTER)
    mytree.heading('col9',text='Price', anchor=CENTER)
    mytree.heading('col10',text='Date', anchor=CENTER)
    mytree.heading('col11',text='Plane Type', anchor=CENTER)

    mytree.column('col1', anchor=CENTER, width=90)
    mytree.column('col2', anchor=CENTER, width=100)
    mytree.column('col3', anchor=CENTER, width=130)
    mytree.column('col4', anchor=CENTER, width=130)
    mytree.column('col5', anchor=CENTER, width=100)
    mytree.column('col6', anchor=CENTER, width=100)
    mytree.column('col7', anchor=CENTER, width=100)
    mytree.column('col8', anchor=CENTER, width=50)
    mytree.column('col9', anchor=CENTER, width=50)
    mytree.column('col10', anchor=CENTER, width=100)
    mytree.column('col11', anchor=CENTER, width=100)
    mytree.column('#0',width=0,minwidth=0)
    mytree.bind('<Double-1>', treeviewclick) # Double click event
    fetch_tree()
    
    Label(addminframe, text='Flight Number',bg="#ffffff").grid(row=1, column=1,sticky="e")
    fn = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    fn.grid(row=1,column=2)

    Label(addminframe, text='Airlines',bg="#ffffff").grid(row=1, column=3,sticky="e")
    al = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    al.grid(row=1,column=4)

    Label(addminframe, text='Departure',bg="#ffffff").grid(row=2, column=1,sticky="e")
    dp = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    dp.grid(row=2,column=2)

    Label(addminframe, text='Arrival',bg="#ffffff").grid(row=2, column=3,sticky="e")
    ar = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    ar.grid(row=2,column=4)

    Label(addminframe, text='Flight Time',bg="#ffffff").grid(row=3, column=1,sticky="e")
    ft = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    ft.grid(row=3,column=2)

    Label(addminframe, text='Departure Time',bg="#ffffff").grid(row=3, column=3,sticky="e")
    dt = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    dt.grid(row=3,column=4)

    Label(addminframe, text='Arrival Time',bg="#ffffff").grid(row=4, column=1,sticky="e")
    at = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    at.grid(row=4,column=2)

    Label(addminframe, text='Seats',bg="#ffffff").grid(row=4, column=3,sticky="e")
    st = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    st.grid(row=4,column=4)

    Label(addminframe, text='Price',bg="#ffffff").grid(row=5, column=1,sticky="e")
    pr = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    pr.grid(row=5,column=2)

    Label(addminframe, text='Date',bg="#ffffff").grid(row=5, column=3,sticky="e")
    date = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    date.grid(row=5,column=4)

    Label(addminframe, text='Plane Type',bg="#ffffff").grid(row=6, column=1,sticky="e")
    pt = Entry(addminframe,bg="#D8D2CB", width=15, font=("Product Sans", 15))
    pt.grid(row=6,column=2)

    ttk.Button(addminframe, text='Add record', command=add_record).grid(row=1, column=5)
    ttk.Button(addminframe, text='Update record', command=update_record).grid(row=2, column=5)
    ttk.Button(addminframe, text='Remove record', command=delete_record).grid(row=3, column=5)
    ttk.Button(addminframe, text='Clear', command=clear_data).grid(row=4, column=5)

def logoutaddmin():
    addminframe.destroy
    mainlayout()
    
def fetchSearch():
    mytree.delete(*mytree.get_children())
    if search_box.get() == '':
        sql = "SELECT * FROM Flights"
        cursor.execute(sql)
        result = cursor.fetchall()
    else:
        sql = "SELECT * FROM Flights WHERE flight_number = ?"
        cursor.execute(sql , [search_box.get().upper()])
        result = cursor.fetchall()
    if result:
        for i, data in enumerate(result):
            #mytree.insert("","end",values=(data))
            mytree.insert("","end",values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10]))
            print(data)

def treeviewclick(event):
    prod = mytree.item(mytree.focus(), 'values')
    clear_data()
    fn.insert(0, prod[0])
    al.insert(0, prod[1]) 
    dp.insert(0, prod[2]) 
    ar.insert(0, prod[3]) 
    ft.insert(0, prod[4])
    dt.insert(0, prod[5])
    at.insert(0, prod[6])
    st.insert(0, prod[7])
    pr.insert(0, prod[8])
    date.insert(0, prod[9])
    pt.insert(0, prod[10])

def add_record() :
    # print('add record')
    sql_chk = "SELECT * FROM flights WHERE flight_number= ?"
    cursor.execute(sql_chk,[fn.get().upper()])
    chk_result = cursor.fetchall()
    print(chk_result)
    if chk_result:
        messagebox.showwarning("Admin", 'This flight number already use')
        fn.focus_force()
        fn.select_range(0,END)
    else:
        if fn.get() == '' :
            messagebox.showwarning('Admin', 'Enter ID first')
            fn.focus_force()
            #check other
        else :
            sql = ''' INSERT INTO flights (flight_number, airlines, from_dep, to_arr, flight_time, time_departure, time_arrival, seats, price, day, plane_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''
            cursor.execute(sql, [fn.get().upper(), al.get(), dp.get(), ar.get(), ft.get(), dt.get(), at.get(), st.get(), pr.get(), date.get(), pt.get()])
            conn.commit()
            messagebox.showinfo('Admin', 'Add successfully')
            clear_data()
            fetch_tree()

def update_record() :
    # print('update record')
    prod = mytree.item(mytree.focus(), 'values')
    selected_prod_id = prod[1] #product id from Treeview
    fn.focus_force()

    if fn.get() == '' :
        messagebox.showwarning('Admin', 'Enter ID first')
        fn.focus_force()
    #check other
    else :
        sql = ''' UPDATE flights
                  SET flight_number=?, airlines=?, from_dep=?, to_arr=?, flight_time=?, time_departure=?, time_arrival=?, seats=?, price=?, day=?, plane_type=?
                  WHERE flight_number=?
              '''
        cursor.execute(sql, [fn.get().upper(), al.get(), dp.get(), ar.get(), ft.get(), dt.get(), at.get(), st.get(), pr.get(), date.get(), pt.get(),fn.get().upper()])
        conn.commit()
        messagebox.showinfo('Admin', 'Update successfully')
        clear_data()
        fetch_tree()

def delete_record() :
    # print('remove record')
    msg = messagebox.askquestion('Delete', 'Are you sure you want to delete?', icon='warning')
    if msg == 'no' :
        clear_data()
    else :
        prod = mytree.item(mytree.focus(), 'values')
        selected_prod_id = prod[0] #product id from Treeview

        sql = 'DELETE FROM flights WHERE flight_number=?'
        cursor.execute(sql, [selected_prod_id])
        conn.commit()
        messagebox.showinfo('Admin', 'Delete successfully')
        clear_data()
        fetch_tree()
    
def clear_data():    
    fn.delete(0, END)
    al.delete(0, END) 
    dp.delete(0, END) 
    ar.delete(0, END) 
    ft.delete(0, END)
    dt.delete(0, END)
    at.delete(0, END)
    st.delete(0, END)
    pr.delete(0, END)
    date.delete(0, END)
    pt.delete(0, END)
    fn.focus_force()

def fetch_tree():
  mytree.delete(*mytree.get_children())
  sql = "SELECT * FROM Flights"
  cursor.execute(sql)
  result = cursor.fetchall()
  if result:
    for i, data in enumerate(result):
      #mytree.insert("","end",values=(data))
      mytree.insert("","end",values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10]))
      print(data)

def profilelayout():
    global password_update,checkbox,addminframe
    addminframe = Frame(root, bg='#F5F2F2')
    addminframe.place(x=0, y=0, width=w, height=h)
    Label(addminframe,image=flight_img1,bg="#F5F2F2").place(x=-3,y=0)

    Button(addminframe,image=flight_img16,activebackground='#398AB9',bg="#398AB9",bd=0,command=addminframe.destroy).place(x=20,y=140)

    Label(addminframe,image=flight_img16,bg="#F5F2F2").place(x=200,y=200)

    Button(addminframe,text="Back",width=10,command=addminframe.destroy,font=("Product Sans", 20, "bold"),bd=0).place(x=180,y=700)

    Button(addminframe,text="Edit",width=10,command=addminframe.destroy,font=("Product Sans", 20, "bold"),bd=0).place(x=380,y=700)

    Label(addminframe,image=flight_img21,bg="#F5F2F2").place(x=150,y=50)

    Label(addminframe,text="%s %s"%(resultuser[0][0],resultuser[0][1]),bg="#ffffff",font=("Product Sans", 30, "bold")).place(x=320,y=110)

    Label(addminframe,text=resultuser[0][0],bg="#ffffff",fg="#398AB9",font=("Product Sans", 20, "bold")).place(x=215,y=355)

    Label(addminframe,text=resultuser[0][1],bg="#ffffff",fg="#398AB9",font=("Product Sans", 20, "bold")).place(x=485,y=355)

    Label(addminframe,text=resultuser[0][2],bg="#ffffff",fg="#398AB9",font=("Product Sans", 20, "bold")).place(x=785,y=355)

    def show_password():
        if password_update.cget("show") == "•":
            password_update.config(show="")
        else :
            password_update.config(show="•")

    checkbox = Checkbutton(addminframe, text="Show password", command=show_password,bg="#ffffff")
    checkbox.place(x=215,y=530)

    Label(addminframe,text="<-- You can change your password right here\nthen click update password button\nfor update your information",bg="#ffffff",fg="#398AB9",font=("Product Sans", 15)).place(x=550,y=485)

    password_update = Entry(addminframe,bg="#F5F2F2",width="15",fg="#398AB9",font=("Product Sans", 20, "bold"),textvariable=password_updateinfo,bd=0,show="•")
    password_update.place(x=215,y=485)
    password_updateinfo.set(resultuser[0][3])

    Button(addminframe,text="Back",width=10,command=addminframe.destroy,font=("Product Sans", 20, "bold"),bd=0).place(x=200,y=650)

    Button(addminframe,text="Update Password",width=15,command=Update_Password,font=("Product Sans", 20, "bold"),bd=0).place(x=400,y=650)

def Update_Password():
    if messagebox.askyesno("let's holiday", 'Do you want to change your password?'):
        user = resultuser[0][2]
        sql = ''' UPDATE login
                SET password=?
                WHERE email=?
            '''
        cursor.execute(sql, [password_updateinfo.get(),user])
        conn.commit()
        messagebox.showinfo("let's holiday", 'Logout')
        addminframe.destroy
        mainlayout()

def card_numtext(event):
    card_num.delete(0,END)

def card_nametext(event):
    card_name.delete(0,END)

def card_datetext(event):
    card_date.delete(0,END)

def card_vcctext(event):
    card_vcc.delete(0,END)

def paylayout(i,data):
    global card_num,card_name,card_date,card_vcc
    payframe = Frame(root, bg='#EFEFEF')
    payframe.place(x=0, y=0, width=w, height=h)
    Label(payframe,image=flight_img1,bg="#EFEFEF").place(x=-3,y=0)  

    Button(payframe,image=flight_img20,fg="#398AB9",bg="#EFEFEF",bd=0,command=payframe.destroy).place(x=340,y=70)

    Label(payframe,image=flight_img23,bg="#EFEFEF").place(x=400,y=50) 
    card_num = Entry(payframe,bg="#F6F6F6",width="21",fg="#398AB9",font=("Product Sans", 20),bd=0,textvariable=card_numinfo)
    card_num.place(x=485,y=303)
    card_num.insert(0,' Card Number')
    card_num.bind("<Button>",card_numtext)
    

    card_name = Entry(payframe,bg="#F6F6F6",width="21",fg="#398AB9",font=("Product Sans", 20),bd=0,textvariable=card_nameinfo)
    card_name.place(x=485,y=395)
    card_name.bind("<Button>",card_nametext)
    card_nameinfo.set("Name Card")

    card_date = Entry(payframe,bg="#F6F6F6",width="6",fg="#398AB9",font=("Product Sans", 20),bd=0,textvariable=card_dateinfo)
    card_date.place(x=485,y=487)
    card_date.bind("<Button>",card_datetext)
    card_dateinfo.set("Date")

    card_vcc = Entry(payframe,bg="#F6F6F6",width="6",fg="#398AB9",font=("Product Sans", 20),bd=0,textvariable=card_vccinfo)
    card_vcc.place(x=655,y=487)
    card_vcc.bind("<Button>",card_vcctext)
    card_vccinfo.set("VCC")

    Button(payframe,image=flight_img24,bg="#ffffff",command=lambda:paylayoutwarning(i,data),font=("Product Sans", 20, "bold"),bd=0).place(x=500,y=644)

def paylayoutwarning(i,data) :
    if card_num.get() == "Card Number":
        messagebox.showwarning("let's holiday", 'Please enter your Card Number')
    elif card_name.get() == "Name Card":
        messagebox.showwarning("let's holiday", 'Please enter your Card Name')
    elif card_date.get() == "Date":
        messagebox.showwarning("let's holiday", 'Please enter your Card Date')
    elif card_vcc.get() == "VCC":
        messagebox.showwarning("let's holiday", 'Please enter your Card VCC')
    else:
        messagebox.showinfo("let's holiday", 'You are Good To GO!!!')
        emailsend(i,data)

def emailsend(i,data):
    global emailframe
    emailframe = Frame(root, bg='#EFEFEF')
    emailframe.place(x=0, y=0, width=w, height=h)

    Label(emailframe,image=flight_img1,bg="#EFEFEF").place(x=-3,y=0) 
    Label(emailframe,image=flight_img22,bg="#EFEFEF").place(x=280,y=220)

    Button(emailframe,image=flight_img6,bg="#EFEFEF",command=backflightlayout,font=("Product Sans", 20, "bold"),bd=0).place(x=570,y=650)
    
    curr = time.time()
    local_time = time.ctime(curr)

    sender_email="Your Email"
    receiver_email="%s"%(resultuser[0][2].lower())
    password = "Your password"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Booking is confirmed!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text of your message
    text = text = """\
    Thank you for choosing let's holiday
    
    ELECTRONIC TICKET RECEIPT
    Date : %s

    Date Flight %s
    Flight %s
    Airlines %s
    Plane Type %s
    Passenger %s
    From %s
    To %s
    Flight %s
    Departure %s
    Arrival %s
    
    Price %s

    """%(local_time,result[i][9],result[i][0],result[i][1],result[i][10],personinfo.get(),result[i][2],result[i][3],result[i][4],result[i][5],result[i][6],result[i][8]*personinfo.get()+200)

    # Turn these into plain Text objects
    part1 = MIMEText(text, "plain")

    # plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    seats = result[i][7]-1
    flight = result[i][0]
    
    if seats == 0 :
        sql = 'DELETE FROM flights WHERE flight_number=?'
        cursor.execute(sql, [flight])
        conn.commit()
    else:    
        sql = ''' UPDATE flights
                SET seats=?
                WHERE flight_number=?
            '''
        cursor.execute(sql, [seats,flight])
        conn.commit()
    
def backflightlayout():
    emailframe.destroy
    flightlayout()

w = 1300
h = 800

createconnection()
root = mainwindow()

#loginlayout info
userinfo = StringVar()
passinfo = StringVar()

#signuplayout info
newemailinfo = StringVar()
newfnameinfo = StringVar()
newlnameinfo = StringVar()
newpwdinfo = StringVar()
newconfirpwdinfo = StringVar()

#flightlayout info
fromoptioninfo = StringVar()
tooptioninfo = StringVar()
seatoptioninfo = StringVar()
calinfo = StringVar()
personinfo = IntVar()

#profilelayout info
password_updateinfo = StringVar()

#paylayout info
card_numinfo = StringVar()
card_nameinfo = StringVar()
card_dateinfo = StringVar()
card_vccinfo = StringVar()

#icon
img_icon = PhotoImage(file="images\paper-plane.png")
root.iconphoto(FALSE,img_icon)

#mainlayout_img
main_img1 = PhotoImage(file=r'images\main_img.png')
main_img2 = PhotoImage(file=r'images\login_button.png')
main_img3 = PhotoImage(file=r'images\signup_button.png')

#loginlayout_img
login_img1 = PhotoImage(file=r'images\login_img.png')
login_img2 = PhotoImage(file=r'images\Vpn key.png')
login_img3 = PhotoImage(file=r'images\Account circle.png')
login_img4 = PhotoImage(file=r'images\login_small_button.png')
login_img5 = PhotoImage(file=r'images\back to sign up.png')

#signuplayout_img
singup_img1 = PhotoImage(file=r'images\singup_img.png')
singup_img2 = PhotoImage(file=r'images\Already have an account.png')
singup_img3 = PhotoImage(file=r'images\signup_small_button.png')

#nicetomeetyoulayout_img
ntmy_img1 = PhotoImage(file=r'images\waving-hand.png')

#flightlayout_img
flight_img1 = PhotoImage(file=r'images\bar.png')
flight_img2 = PhotoImage(file=r'images\logout_button.png')
flight_img3 = PhotoImage(file=r'images\From.png')
flight_img4 = PhotoImage(file=r'images\To.png')
flight_img5 = PhotoImage(file=r'images\date_button.png')
flight_img6 = PhotoImage(file=r'images\done_button.png')
flight_img7 = PhotoImage(file=r'images\Search_button.png')
flight_img8 = PhotoImage(file=r'images\class.png')
flight_img9 = PhotoImage(file=r'images\Passengers.png')
flight_img11 = PhotoImage(file=r'images\air asia bar.png')
flight_img12 = PhotoImage(file=r'images\lion air bar.png')
flight_img13 = PhotoImage(file=r'images\nokair bar.png')
flight_img14 = PhotoImage(file=r'images\thai smile bar.png')
flight_img15 = PhotoImage(file=r'images\thai smile bar.png')
flight_img16 = PhotoImage(file=r'images\profile.png')
flight_img17 = PhotoImage(file=r'images\booking_button.png')

#profilelayout_img
flight_img21 = PhotoImage(file=r'images\detail profile.png')

#flightdetailllayout_img
flight_img18 = PhotoImage(file=r'images\detail flight.png')
flight_img19 = PhotoImage(file=r'images\detail price.png')
flight_img20 = PhotoImage(file=r'images\back.png')
flight_img25 = PhotoImage(file=r'images\backred.png')
flight_img26 = PhotoImage(file=r'images\confirm.png')

#paylayout_img
flight_img23 = PhotoImage(file=r'images\detail pay.png')
flight_img24 = PhotoImage(file=r'images\paynow.png')

#email_img
flight_img22 = PhotoImage(file=r'images\Bookingdone.png')

root.after(3700,mainlayout)

root.mainloop()