from tkinter import  *
root = Tk()
host_path='C:\Windows\System32\drivers\etc\hosts'
#host_path1='C:\\Users\\saive\\OneDrive\\Desktop\\Codes\\file1'
ip_address='127.0.0.1'
def display():  # function to display blocked website
    ptr=1
    with open(host_path,'r') as host_file1:
        file_content1=host_file1.readlines()
        for line in file_content1:
            if ptr >= 18:
                print(line)
            ptr+=1
display()

def submit():  # function to block website
    y1=entry1.get()
    website=y1
    with open(host_path,'r+') as host_file:
        file_content=host_file.readlines() 
       
        if website in file_content:
            Label(root,text="Already Blocked",font=('arial',10,'bold')).place(x=900,y=450)
            pass

        else:
            host_file.write(ip_address+" "+website+'\n')
            Label(root,text="Blocked",font=('arial',10,'bold')).place(x=800,y=450)
    host_file.close()
def submit1():  # function to unblock website
      
    y2=entry2.get()
    website1=y2  
    with open(host_path,'r+') as host_file1:
        file_content1=host_file1.readlines()
        web=ip_address+" "+website1
        print('yes')
        
        with open (host_path , 'r+') as f:
            for line in file_content1:
                if line.strip("\n") != web:       
                    f.write(line)

            f.truncate()     
    host_file1.close()


root.title("Shyam Sai")
# photo=PhotoImage(file='E:\webimg.jpg')   # to upload  image in folder
lable= Label(root,
                 text="website blocker",
                font=('Arial',20,'bold'),
                 fg='white',
                bg='black',
                 relief=RAISED,
                 bd=(10),
                 padx=(40),
                pady=(40),
                #  image=photo,
                 compound='bottom').place(x=600,y=10)
lable1=Label(root,text=("To Block The WebSite Paste The Link Here"),
                                                                     font=('Arial',10,'bold') ,
                                                                     compound='bottom'
                                                                     ).place(x=600,y=400)
lable2=Label(root,text=("To UnBlock The WebSite Paste The Link Here"),
                                                                     font=('Arial',10,'bold') ,
                                                                     compound='bottom'
                                                                     ).place(x=600,y=500)
entry1 = Entry(root,width=40)
entry1.place(x=600,y=450)


button =Button(root,
                    text="block",
                    font=('Arial',10,'bold'),
                    fg='white',
                 bg='black',
                 relief=RAISED,
                 #bd=(10),
                 #padx=(10),
                 #pady=(10),
                 command=submit
                 ).place(x=900,y=450)
button1=Button(root,
                    text="un block",
                    font=('Arial',10,'bold'),
                    fg='white',
                 bg='black',
                 relief=RAISED,
                 #bd=(10),
                 #padx=(10),
                 #pady=(10),
                 command=submit1
                 ).place(x=900,y=550)
entry2 = Entry(root,width=40)
entry2.place(x=600,y=550)

root.mainloop()