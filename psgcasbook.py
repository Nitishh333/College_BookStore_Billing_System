from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random
import time
import os
import tempfile
root=Tk()
root.geometry("2000x2000")
root.configure(bg="#333333")

frame=Frame(root)
frame.pack(pady=250)
frame.configure(bg="#333333")

uservar=StringVar()
passvar=StringVar()


login=Label(frame,text="LOGIN",font=("Arial",40,"bold","underline"),fg="#ff3399",bg="#333333")
login.grid(row=0,column=0,columnspan=2)

labeluser=Label(frame,text="USERNAME:",font=("Arial",25),bg="#333333",fg="#ffffff")
labeluser.grid(row=1,column=0,pady=20)

entry1=Entry(frame,font=2,textvariable=uservar)
entry1.grid(row=1,column=1,ipadx=30,padx=30)

passlabel=Label(frame,text="PASSWORD:",font=("Arial",25),bg="#333333",fg="#FFFFFF")
passlabel.grid(row=2,column=0,pady=20)

entry2=Entry(frame,show='*',font=2,textvariable=passvar)
entry2.grid(row=2,column=1,ipadx=30)

loginbutton=Button(frame,text="Login",font=("Arial",20),bg="#ff3399",fg="white",cursor="hand2",command=lambda:login())
loginbutton.grid(row=3,column=0,columnspan=2,ipadx=10,pady=20)

#=Button(frame,text="Clear",font=("Arial",20),bg="#ff3399",fg="white",command=lambda:clear())
#clearbutton.grid(row=3,column=0,sticky=E,padx=50)

def login():
    username="Admin"
    password="1234567"
    if(entry1.get()==username and entry2.get()==password):
        root.destroy()
        mainwindow()
    else:
        messagebox.showinfo("Invalid","INVALID!")
def clear():
    uservar.set("")
    passvar.set("")




def mainwindow():
    global cmb,costvar,quantityvar,ratevar,treeview,totalcostvar,totalcost
    
  



    root=Tk()
    root.geometry("1530x785+0+0")
    root.resizable(0,0)
    frame1=Frame(root,highlightthickness=2,bg="black",bd=6,relief=RIDGE)
    frame1.pack(ipadx=700)
    label1=Label(frame1,text="PSG CAS BOOK STORE",fg="white",bg="black",font=("georgia",30,"bold","underline"))
    label1.grid(row=0,column=1,padx=530,ipady=10)

    frame2=Frame(root,width=50,height=50,highlightthickness=2,highlightbackground="black",bd=8,relief=RIDGE)
    frame2.pack(ipadx=650,ipady=345)

    frame2.config(width=300)
    frame2.grid_propagate(False)



    additem=Button(frame2,text="ADD NEW ITEM",bd=3,relief=RAISED,fg="#0080ff",font=("bold"),cursor="hand2",command=lambda:insert())
    additem.grid(row=3,column=1,pady=30,ipady=10)


    logoutbtn=Button(frame2,text="LOGOUT",bd=3,relief=RAISED,fg="#0080ff",cursor="hand2",font="bold",command=root.destroy)
    logoutbtn.grid(row=0,column=7,padx=85,sticky=NE,ipadx=10,ipady=10)

    resetbutton=Button(frame2,text="RESET",bd=3,relief=RAISED,fg="#0080ff",cursor="hand2",font="bold",command=lambda:delete())
    resetbutton.grid(row=3,column=6,ipadx=30,ipady=10,sticky=W,padx=20)

    buttonaddlist=Button(frame2,text="ADD TO LIST",fg="#0080ff",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:treevieww())
    buttonaddlist.grid(row=3,column=5,pady=30,ipadx=10,ipady=10,sticky=W,padx=30)

    buttoncalculate=Button(frame2,text="CALCULATE",fg="#0080ff",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:sql())
    buttoncalculate.grid(row=3,column=2,ipadx=10,ipady=10,sticky=W,padx=20)

    buttonbill=Button(frame2,text="GENERATE BILL",fg="#0080ff",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:bill())
    buttonbill.grid(row=4,column=7,pady=150,sticky=SW,ipadx=10,ipady=10)

    conn=sqlite3.connect("miniproject.db")
    cursor=conn.cursor()
    cursor.execute("select product_name from product")
    results=cursor.fetchall()
    resultss=[result[0]for result in results]

    cmb=ttk.Combobox(frame2,value=resultss,width=25)
    cmb.grid(row=1,column=2,ipadx=30)
    cmb.set("Select the product")

    itemlists=list()

    totalcost=0.0
    totalcostvar=StringVar()
    totalcostvar.set("TOTAL COST={}".format(totalcost))

    quantityvar=StringVar()
    ratevar=StringVar()
    costvar=StringVar()
    ratevar.set("0.00")
    costvar.set("0.00")


    labelselectitem=Label(frame2,text="SELECT PRODUCT :",font=1)
    labelselectitem.grid(row=1,column=1,pady=30,padx=100)





    labelquantity=Label(frame2,text="QUANTITY : ",font=1)
    labelquantity.grid(row=2,column=1,padx=30)

    entryquantity=Entry(frame2,width=38,bd=3,relief=RIDGE,textvariable=quantityvar)
    entryquantity.grid(row=2,column=2)

    labelrate=Label(frame2,text="RATE :",font=1)
    labelrate.grid(row=1,column=5,padx=140)

    entryrate=Label(frame2,textvariable=ratevar)
    entryrate.grid(row=1,column=6,sticky=W)

    labelcost=Label(frame2,text="COST :",font=1)
    labelcost.grid(row=2,column=5)

    entrycost=Label(frame2,width=27,bd=3,relief=RIDGE,textvariable=costvar)
    entrycost.grid(row=2,column=6,sticky=W)



    total=Label(frame2,textvariable=totalcostvar)
    total.grid(row=4,column=6,sticky=NW,padx=70)

    treeview=ttk.Treeview(frame2,height=10,columns=("PRODUCT NAME","QUANTITY","RATE","COST"))
    treeview.heading('#1',text="PRODUCT NAME")
    treeview.heading('#2',text="QUANTITY")
    treeview.heading('#3',text="RATE")
    treeview.heading('#4',text="COST")
    treeview['show']='headings'

    treeview.grid(row=4,column=0,columnspan=7,padx=100,ipady=50,ipadx=150)
def loggout():
    root()

def insert():
    global entrynew
    global entrynewrate
    global newproduct
    global newrate
    global Treeview
    rooot=Tk()
    rooot.geometry("1530x785+0+0")
    rooot.resizable(0,0)

    newproduct=StringVar()
    newrate=StringVar()
    
    Labeladdnew=Label(rooot,text="ENTER THE NEW ITEM  :",font=1)
    Labeladdnew.grid(row=0,column=0,padx=100,pady=50)
    entrynew=Entry(rooot,relief=RIDGE,bd=3,textvariable=newproduct)
    entrynew.grid(row=0,column=1,ipadx=30)

    Labeladdrate=Label(rooot,text="RATE  :",font=1)
    Labeladdrate.grid(row=0,column=2,padx=150,sticky=E)
    entrynewrate=Entry(rooot,relief=RIDGE,bd=3,textvariable=newrate)
    entrynewrate.grid(row=0,column=3,sticky=W,ipadx=30)

    buttonaddnew=Button(rooot,text="ADD",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:addinto())
    buttonaddnew.grid(row=2,column=0,ipadx=30,ipady=10)

    viewbutton=Button(rooot,text="VIEW",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:view())
    viewbutton.grid(row=2,column=3,ipadx=30,ipady=10)

    updatebutton=Button(rooot,text="UPDATE",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:update())
    updatebutton.grid(row=2,column=2,ipadx=30,ipady=10)

    selectbutton=Button(rooot,text="SELECT ITEM",bd=3,relief=RAISED,font="bold",cursor="hand2",command=lambda:select_data(Treeview))
    selectbutton.grid(row=2,column=1,ipadx=30,ipady=10)

    
    
    Treeview=ttk.Treeview(rooot,height=10,columns=("ID","NAME","RATEE"))
    Treeview.heading('#1',text="PRODUCT ID")
    Treeview.heading('#2',text="PRODUCT NAME")
    Treeview.heading('#3',text="RATE")
    Treeview['show']='headings'

    Treeview.grid(row=5,column=0,columnspan=6,padx=200,pady=50,ipadx=250,ipady=100)
    
def delete_data(Treeview):
    selected_item=Treeview.selection()[0]
    print(Treeview.item(selected_item)['values'])
    pid=Treeview.item(selected_item)['values'][0]
    query="delete from product where Product_id=%s"
    sel_data=(pid,)
    cursor.execute(query,sel_data)
    conn.commit()
    Treeview.delete(selected_item)
    messagebox.showinfo("","deleted succesfulluy")
def update():
    global entrynew
    global entrynewrate
    global curitem
    global values
    uname=entrynew.get()
    urate=entrynewrate.get()
    if(uname!="" and urate!=""):
        
        Treeview.item(curitem,values=(values[0],uname,urate))
        conn=sqlite3.connect("miniproject.db")
        cursor=conn.cursor()
        
        query="update product set Product_name=?,Product_rate=? where Product_id=?"
        nn=(uname,urate,values[0],)
        cursor.execute(query,nn)
        conn.commit()
        messagebox.showinfo("","updated succesfully")
        entrynew.delete(0,END)
        entrynewrate.delete(0,END)
    else:
        messagebox.showinfo("MESSAGE","please check the credentials")
        
    
    
def select_data(Treeview):
    global curitem
    global values
    curitem=Treeview.focus()
    values=Treeview.item(curitem,"values")
    entrynew.insert(0,values[1])
    entrynewrate.insert(0,values[2])
    
def view():
    records=Treeview.get_children()
    for element in records:
        Treeview.delete(element)
    conn=sqlite3.connect("miniproject.db")
    cursor=conn.cursor()

    query="select * from product"
    cursor.execute(query)
    data=cursor.fetchall()
    
    for rows in data:
        Treeview.insert('','end',values=(rows[0],rows[1],rows[2]))
    
    conn.commit()


    
def addinto():
    global entrynew
    global entrynewrate
    global newproduct
    global newrate
    global queryyy
    global cursor
    global rooot

    addproduct=entrynew.get()
    addrate=entrynewrate.get()
    if(addproduct!="" and addrate!=""):
        conn=sqlite3.connect("miniproject.db")
        cursor=conn.cursor()
        queryyy="insert into product (Product_name,Product_rate) values('{}','{}')".format(addproduct,addrate)
        cursor.execute(queryyy)
        conn.commit()
        if(queryyy):
             messagebox.showinfo("message","succesfully added")
             
        
            
        
    else:
        messagebox.showinfo("message","please check the credentials")
            
        

   

    

    
    
    
def sql():
    a=cmb.get()
    quantityyy=quantityvar.get()
    if(quantityyy!="" and a!="Select the product"):
        conn=sqlite3.connect("miniproject.db")
        cursor=conn.cursor()
        query="select Product_rate from product where Product_name=?"
        name=(a,)
        cursor.execute(query,name)
        row=cursor.fetchone()
        conn.commit()
    
        quantityy=quantityvar.get()
        quantityy=int(quantityy)
        integer=float(row[0])
        ratevar.set(integer)
        cost=quantityy*integer
        costvar.set(cost)
    else:
        messagebox.showinfo("message","please check the credentials")

    



    



 





    



def treevieww():
    global totalcost
    global totalcostvar
    quantityy=quantityvar.get()
    a=cmb.get()
    integer=ratevar.get()
    cost=costvar.get()
    if(a!="" and quantityy!="" and integer !="0.00" and cost!="0.00" ):
        conn=sqlite3.connect("miniproject.db")
        cursor=conn.cursor()
        quantityy=quantityvar.get()
        a=cmb.get()
        integer=float(ratevar.get())
        cost=costvar.get()
        queryy="insert into bill (Name,Quantity,Rate,Cost) values('{}','{}','{}','{}')".format(a,quantityy,integer,cost)
        cursor.execute(queryy)
        conn.commit()
        records=treeview.get_children()
        for element in records:
            treeview.delete(element)
        conn=sqlite3.connect("miniproject.db")
        cursor=conn.cursor()


        query="select * from bill"
        cursor.execute(query)
        data=cursor.fetchall()
        
        for row in data:
            treeview.insert('','end',values=(row[1],row[2],row[3],row[4]))
        
        conn.commit()
        cmb.set("Select the product")
        quantityvar.set("")
        ratevar.set("0.00")
        costvar.set("0.00")
        

        conn.close()
    else:
        messagebox.showinfo("message","please check the credentials")
    totalcost+=float(cost)
    totalcostvar.set("TOTAL COST={}".format(totalcost))
    
 
def delete():
    global totalcost
    global totalcosvar
    conn=sqlite3.connect("miniproject.db")
    cursor=conn.cursor()
    query="DELETE FROM bill"
    cursor.execute(query)
    conn.commit()
    
    
    totalcost=0.0
    cost=0
    totalcostvar.set("TOTAL COST={}".format(totalcost))
    records=treeview.get_children()
    for element in records:
        treeview.delete(element)
    
    
    conn.commit()
    
def bill():
    root=Tk()
    root.geometry("1000x700+0+0")
    root.resizable(0,0)
    global totalcostvar
    frame1=Frame(root,relief=GROOVE,bd=10)
    frame1.place(x=40,y=10,width=700,height=400)
    scroll_y=Scrollbar(frame1,orient=VERTICAL)
    
    textarea=Text(frame1,yscrollcommand=scroll_y,width=150)
    textarea.pack()
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=textarea.yview)



    x=random.randint(1000,9999)
    billno='BILL'+str(x)

    date=time.strftime('%d/%m/%Y')

    
    #conn=pymysql.connect(host="localhost",user="root",password="Admin@123",db="bookstore")
    #cursor=conn.cursor(pymysql.cursors.DictCursor)
    conn=sqlite3.connect("miniproject.db")
    cursor=conn.cursor()
    costt=totalcostvar.get()
    textarea.delete(1.0,END)
    textarea.insert(END,"\n\t\t\t WELCOME TO PSG CAS BOOK STORE")
    textarea.insert(END,'\n\n\nBILL Number :\t\t'+billno+'\t\t\t\t\t\t\t'+date)
    textarea.insert(END,'\n\n================================================================================\n================================================================================')
    textarea.insert(END,'\nPRODUCT NAME\t\t\t\t QUANTITY\tRATE\t COST')
    
    for child in treeview.get_children():
        item=(treeview.item(child,'values')[0])
        quan=float(treeview.item(child,'values')[1])
        rate=float(treeview.item(child,'values')[2])
        cost=float(treeview.item(child,'values')[3])
        textarea.insert(END,f'\n\n\n{item}')
        textarea.insert(END,f'\t\t\t\t{quan}')
        textarea.insert(END,f'\t{rate}')
        textarea.insert(END,f'\t{cost}')
    textarea.insert(END,'\n\n\n================================================================================')
    textarea.insert(END,f'\n\t\t\t\t\t\t\t{costt}')
    textarea.insert(END,"\n\n\n\t\t\t\tTHANK YOU VISIT AGAIN")


    printbtn=Button(root,text="PRINT",bd=2,relief=RIDGE,font=2,cursor="hand2",command=lambda:print(textarea.get('1.0',END)))
    printbtn.pack(side=BOTTOM,anchor=NW,pady=150,padx=400)

    delete()


def print(txt):
    printbill=tempfile.mktemp('.txt')
    open(printbill,'w').write(txt)
    os.startfile(printbill,'print')
        

    
    
input()    
    


#/////////////////////treeview


#scrollbar=Scrollbar(frame2,orient="vertical",command=treeview.yview)
#scrollbar.grid(row=4,column=5,sticky="NSE")

#treeview.configure(yscroll=scrollbar.set)

 







