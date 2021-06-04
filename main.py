#import modules
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import os
import mysql.connector
import time
from tkinter import messagebox as mb
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="delivero"
)
mycursor = mydb.cursor()
global mycart
mycart=[]

# COLOR PALETTE
# Pink ffdada
# Torquoise dbf6e9
# Blue 9ddfd3
#9ddfd3 #454693
# DArk 31326f


#Used to get dimension of the window and adjust components accirdingly
def getDim():
    global height1
    global width1
    # getting screen's height in pixels 
    height1 = main_screen.winfo_screenheight() 
    # getting screen's width in pixels 
    width1 = main_screen.winfo_screenwidth()

#Change color of button on and after mouse hover
def changeOnHover(button, bgOnHover, bgOnLeave,fgOnHover,fgOnLeave):
    button.bind("<Enter>", func=lambda e: button.config(background=bgOnHover,foreground=fgOnHover)) 
    button.bind("<Leave>", func=lambda e: button.config(background=bgOnLeave,foreground=fgOnLeave))

#Store image in img and assign it to respective variable
def pic(path):    
    global img
    img = ImageTk.PhotoImage(Image.open(path))

#Defines Navigation Bar and opens the Homepage 
class Navbar():
    #Calls Homepage function of Order Food
    def Homepage():
        Order_Food(main_screen,1)

    #Calls ViewCart function of Order Food
    def View_Cart():
        Order_Food(main_screen,2)

    #Logsout and opens Login Page
    def Logout():
        cust_num=""
        Login.login()
        
        
    #Defines the navigtion bar at the right corner of the homepage   
    def navbar():
        rightwidth=width1*0.2
        right_frame=Frame(main_screen,width=rightwidth,height=height1,background="#31326f")
        right_frame.place(relx=0.80,rely=0.0)
        right_frame.config()
        
        pic("eating.png")
        global user_icon
        user_icon=img
        Label(right_frame,width=124,height=124,image=user_icon).place(relx=0.3,rely=0.25)
        
        Order_Btn=Button(right_frame,text="Order Food",width=15,height=1,bg="#31326f",activeforeground="#31326f",activebackground="#ffdada",foreground="#ffdada",font=("Comic Sans MS",10,"bold"),borderwidth=0,command=Navbar.Homepage)
        Order_Btn.place(relx=0.3,rely=0.45)
        changeOnHover(Order_Btn,"#ffdada","#31326f","#31326f","#ffdada")
        
        Profile_Btn=Button(right_frame,text="My Cart",width=15,height=1,bg="#31326f",activeforeground="#31326f",activebackground="#ffdada",foreground="#ffdada",font=("Comic Sans MS",10,"bold"),borderwidth=0,command=Navbar.View_Cart)
        Profile_Btn.place(relx=0.3,rely=0.5)
        changeOnHover(Profile_Btn,"#ffdada","#31326f","#31326f","#ffdada")
        
        Orders_Btn=Button(right_frame,text="My Orders",width=15,height=1,bg="#31326f",activeforeground="#31326f",activebackground="#ffdada",foreground="#ffdada",font=("Comic Sans MS",10,"bold"),borderwidth=0,command=My_Orders.Homepage)
        Orders_Btn.place(relx=0.3,rely=0.55)
        changeOnHover(Orders_Btn,"#ffdada","#31326f","#31326f","#ffdada")
        
        Rest_Btn=Button(right_frame,text="Restaurants",width=15,height=1,bg="#31326f",activeforeground="#31326f",activebackground="#ffdada",foreground="#ffdada",font=("Comic Sans MS",10,"bold"),borderwidth=0,command=Restaurants.Homepage)
        Rest_Btn.place(relx=0.3,rely=0.60)
        changeOnHover(Rest_Btn,"#ffdada","#31326f","#31326f","#ffdada")
        
        #Label(text="",).grid(row=0,column=4)
        Logout_Btn=Button(right_frame,text="Logout",width=15,height=1,bg="#31326f",fg="#ffdada",activeforeground="#31326f",activebackground = "#ff6012",font=("Comic Sans MS",10,"bold"),borderwidth=0,command=Navbar.Logout)
        Logout_Btn.place(relx=0.3,rely=0.65)
        changeOnHover(Logout_Btn,"#ff6012","#31326f","#31326f","#ffdada")
        #print(cust_num)
        Navbar.Homepage()
        
class Order_Food(Frame):
    def __init__(self,root,index):
        self.root=root
        if index==1:
            Order_Food.Homepage()
        if index==2:
            Order_Food.View_Cart()

    #Homepage
    def Homepage():
        global dict1
        global dict2
        global dict3
        dict1={}
        dict2={}
        dict3={}
        leftwidth=width1*0.8
        global left_frame
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()

        global food_name
        food_name=StringVar()
        global food_entry
        food_lable = Label(left_frame,text="Search Food",bg="#ffdada",font=("helvetica",16,"bold"))
        food_lable.place(rely=0.21,relx=0.15)
        food_entry = Entry(left_frame,textvariable=food_name,font =("helvetica",16,"bold"),borderwidth=0)
        food_entry.place(rely=0.21,relx=0.35)
        #food_entry.insert("Search Food")
	#food_entry.bind("<Enter>",func=lambda e: delete("0","END"))
	
        global tree
        #tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4"),show='headings')
        style=ttk.Style()
        #style.theme_use("winnative")

        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        ttk.Style().configure("Treeview.Heading", font=("helvetica", 16,"bold"))
        ttk.Style().configure(
                "Treeview",
                font=('Comic Sans MS',16),
                background="#dbf6e9",
                fieldbakground="dbf6e9",
                foreground="#31326f",
                rowheight=28
                )
        style.map('Treeview', background=[('selected', '#31326f')],foreground=[('selected','#ffdada')])
        #tree.tag_configure('odd',background='#E8E8E8')
        #tree.tag_configure('even',background='red')
        tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4"),show='headings')
        ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree.yview)
        tree.configure(yscroll=ybar.set)
        tree.column("#1",anchor=CENTER,width=150)
        tree.heading("#1", text="Food_ID")
        tree.column("#2",anchor=CENTER,width=275)
        tree.heading("#2", text="Dish")
        tree.column("#3",anchor=CENTER,width=275)
        tree.heading("#3", text="Restaurant")
        tree.column("#4",anchor=CENTER,width=150)
        tree.heading("#4", text="Price")
        tree.place(rely=0.32,relx=0.15)


        #tree.insert("",END,values=("12","13","14"),tags = ('oddrow',))
        #tree.insert("",END,values=("15","16","17"),tags = ('evenrow',))
        tree.tag_configure("evenrow",background='#9ddfd3',foreground='black')
        tree.tag_configure("oddrow",background='#dbf6e9',foreground='black')

        #Initially Displaying All Food in The List
        try:                
            sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID AND Dish LIKE '%'"
            #res_id=2
            #sql1 = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID="+str(res_id)+" AND Dish LIKE '%'"
            #val = (search_info)
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            i=1
            for row in myresult:
                if(i%2==0):
                    id=tree.insert("",END,values=row,tags=('evenrow',))
                else:
                    id=tree.insert("",END,values=row,tags=('oddrow',))
                dict1[id] = row[0]
                i=i+1
        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)

        Search_btn=Button(left_frame,text="Search",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.Search,borderwidth=0)
        Search_btn.place(rely=0.20,relx=0.65)
        changeOnHover(Search_btn,"#454693","#ffdada","#ffdada","#454693")

        Book_btn=Button(left_frame,text="Add To Cart",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.Add_To_Cart,borderwidth=0)
        Book_btn.place(relx=0.35,rely=0.75)
        changeOnHover(Book_btn,"#454693","#ffdada","#ffdada","#454693")
        
        View_btn=Button(left_frame,text="View Cart",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.View_Cart,borderwidth=0)
        View_btn.place(relx=0.50,rely=0.75)
        changeOnHover(View_btn,"#454693","#ffdada","#ffdada","#454693")


    #Overloaded Homepage when we search using restaurants
    def Homepage1(sql):
        global dict1
        global dict2
        global dict3
        dict1={}
        dict2={}
        dict3={}
        leftwidth=width1*0.8
        global left_frame
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()

        #pic("maple.png")
        #global maple
        #maple=img
        #Label(left_frame,width=120,height=120,image=maple).place(relx=0.85,rely=0.80)

        global food_name
        food_name=StringVar()
        global food_entry
        food_lable = Label(left_frame,text="Search Food",bg="#ffdada",font=("helvetica",16,"bold"))
        food_lable.place(rely=0.21,relx=0.15)
        food_entry = Entry(left_frame,textvariable=food_name,font =("helvetica",16,"bold"),borderwidth=0)
        food_entry.place(rely=0.21,relx=0.35)
        #food_entry.insert("Search Food")
	#food_entry.bind("<Enter>",func=lambda e: delete("0","END"))
	
        global tree
        #tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4"),show='headings')
        style=ttk.Style()
        #style.theme_use("winnative")

        style.layout("Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        ttk.Style().configure("Treeview.Heading", font=("helvetica", 16,"bold"))
        ttk.Style().configure(
                "Treeview",
                font=('Comic Sans MS',16),
                background="#dbf6e9",
                fieldbakground="dbf6e9",
                foreground="#31326f",
                rowheight=28
                )
        style.map('Treeview', background=[('selected', '#31326f')],foreground=[('selected','#ffdada')])
        #tree.tag_configure('odd',background='#E8E8E8')
        #tree.tag_configure('even',background='red')
        tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4"),show='headings')
        ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree.yview)
        tree.configure(yscroll=ybar.set)
        tree.column("#1",anchor=CENTER,width=150)
        tree.heading("#1", text="Food_ID")
        tree.column("#2",anchor=CENTER,width=275)
        tree.heading("#2", text="Dish")
        tree.column("#3",anchor=CENTER,width=275)
        tree.heading("#3", text="Restaurant")
        tree.column("#4",anchor=CENTER,width=150)
        tree.heading("#4", text="Price")
        tree.place(rely=0.32,relx=0.15)


        #tree.insert("",END,values=("12","13","14"),tags = ('oddrow',))
        #tree.insert("",END,values=("15","16","17"),tags = ('evenrow',))
        tree.tag_configure("evenrow",background='#9ddfd3',foreground='black')
        tree.tag_configure("oddrow",background='#dbf6e9',foreground='black')

        #Initially Displaying All Food in The List
        try:                
            #sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID AND Dish LIKE '%'"
            #res_id=2
            #sql1 = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID="+str(res_id)+" AND Dish LIKE '%'"
            #val = (search_info)
            print(sql)
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            i=1
            for row in myresult:
                if(i%2==0):
                    id=tree.insert("",END,values=row,tags=('evenrow',))
                else:
                    id=tree.insert("",END,values=row,tags=('oddrow',))
                dict1[id] = row[0]
                i=i+1
        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)

        Search_btn=Button(left_frame,text="Search",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.Search,borderwidth=0)
        Search_btn.place(rely=0.20,relx=0.65)
        changeOnHover(Search_btn,"#454693","#ffdada","#ffdada","#454693")

        Book_btn=Button(left_frame,text="Add To Cart",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.Add_To_Cart,borderwidth=0)
        Book_btn.place(relx=0.35,rely=0.75)
        changeOnHover(Book_btn,"#454693","#ffdada","#ffdada","#454693")
        
        View_btn=Button(left_frame,text="View Cart",width=10,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",font=("Comic Sans MS",14,"bold"),command=Order_Food.View_Cart,borderwidth=0)
        View_btn.place(relx=0.50,rely=0.75)
        changeOnHover(View_btn,"#454693","#ffdada","#ffdada","#454693")



    #Function to Search Food Works when user click  Search Button
    def Search():
        search_info=food_name.get()
        tree.delete(*tree.get_children())
        
        print(search_info)
        try:                
            sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID AND Dish LIKE '%"+search_info+"%'" 
            #val = (search_info)
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            i=1
            
            for row in myresult:
                if(i%2==0):
                    id=tree.insert("",END,values=row,tags=('evenrow',))
                else:
                    id=tree.insert("",END,values=row,tags=('oddrow',))
                dict1[id] = row[0]
                i=i+1
        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            #print(err.msg)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)
        
    #Adds Selected Item into user cart
    def Add_To_Cart():
        a=tree.focus()
        f_id=dict1[a]
        mycart.append(f_id)


    #Places Order For Particular User placing all orders in cart....
        #Need to define Order Placed Dialog.....
    def Place_Order():
        cost=0
        order_id=0
        try:                
            sql = "Select MAX(Order_ID) FROM Orders"
            mycursor.execute(sql)
            myresult=mycursor.fetchone()
            last_order_id=myresult[0]
            order_id=last_order_id+1
            for x in dict2.values():
              cost=(x[1]*x[2])+cost
        except mysql.connector.Error as err:
            Label(left_frame, text="Some Error Occured 1", fg="red",font=("playful", 14)).place(relx=0.2,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.2,rely=0.75)

        try:
            for x in dict2.values():
                sql = "INSERT INTO Order_Detail (Order_ID,Food_ID,QTY) VALUES (%s,%s,%s)" 
                val = (order_id,x[0],x[2])
                #print(sql,val)
                mycursor.execute(sql,val)
                mydb.commit()
            #ORDER PLACED SUCCESSFULLY
            print("Inserted in Orders")
            mb.showinfo("Order Placed", "Order Placed Successfully !!")
        except mysql.connector.Error as err:
            Label(left_frame, text="Some Error Occured 2", fg="red",font=("playful",14)).place(relx=0.2,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.2,rely=0.75)
        try:
            sql = "INSERT INTO Orders (Order_ID,CUST_NUM,COST) VALUES (%s,%s,%s)"
            val=(order_id,cust_num,cost)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Inserted in Orders")
            #ORDER PLACED SUCCESSFULLY
            mb.showinfo("Order Placed", "Order Placed Successfully !!")
        except mysql.connector.Error as err:
            Label(left_frame, text="Some Error Occured 3", fg="red",font=("playful", 14)).place(relx=0.2,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.2,rely=0.75)

        
        
    #Increase Quantity of Selected Item by 1
    def Increase():
        selected_item = tree.selection()[0]
        f_id=dict2[selected_item][0]
        mycart.append(f_id)
        Order_Food.View_Cart()

    #Delete Selected Item from Cart
    def Delete_Item():
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
        f_id=dict2[selected_item][0]
        for i in mycart:
            if(i == f_id): 
                mycart.remove(i)
    
    #Defining Left Main Screen folder listing users cart
    def View_Cart():
        leftwidth=width1*0.8
        global left_frame
        global tree
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()

        #CART EMPTY
        if len(mycart)==0:
            #Cart empty widget
            pic("empty_cart.jpg")
            global empty_cart
            empty_cart=img
            Label(left_frame,width=450,height=450,image=empty_cart,borderwidth=0).place(relx=0.31,rely=0.15)
            #print("Cart Empty")
            Search1_btn=Button(left_frame,text="Search Food Here",width=15,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",18,"bold"),command=Navbar.Homepage)
            Search1_btn.place(relx=0.42,rely=0.80)
            changeOnHover(Search1_btn,"#454693","#ffdada","#ffdada","#454693")

            #Search food Buttons at bottom
            
        else:
            try:
                tree.delete(*tree.get_children())
                if len(mycart)==1:
                    sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID AND Food_ID ="+str(mycart[0])
                    print(sql)
                    tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4","c5"),show='headings')
                    ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree.yview)
                    tree.configure(yscroll=ybar.set)
                    tree.column("#1",anchor=CENTER,width=100)
                    tree.heading("#1",text="Food_ID")
                    tree.column("#2",anchor=CENTER,width=275)
                    tree.heading("#2",text="Dish")
                    tree.column("#3",anchor=CENTER,width=275)
                    tree.heading("#3",text="Restaurant")
                    tree.column("#4",anchor=CENTER,width=100)
                    tree.heading("#4",text="Price")
                    tree.column("#5",anchor=CENTER,width=100)
                    tree.heading("#5",text="QTY")
                    tree.place(rely=0.30,relx=0.15)
                else:
                    food_id=tuple(mycart)
                    sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID AND Food_ID IN {}".format(food_id)
                    print(sql)
                    tree = ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4","c5"),show='headings')
                    ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree.yview)
                    tree.configure(yscroll=ybar.set)
                    tree.column("#1",anchor=CENTER,width=100)
                    tree.heading("#1",text="Food_ID")
                    tree.column("#2",anchor=CENTER,width=275)
                    tree.heading("#2",text="Dish")
                    tree.column("#3",anchor=CENTER,width=275)
                    tree.heading("#3",text="Restaurant")
                    tree.column("#4",anchor=CENTER,width=100)
                    tree.heading("#4",text="Price")
                    tree.column("#5",anchor=CENTER,width=100)
                    tree.heading("#5",text="QTY")
                    tree.place(rely=0.3,relx=0.15)
                tree.tag_configure("evenrow",background='#9ddfd3',foreground='black')
                tree.tag_configure("oddrow",background='#dbf6e9',foreground='black')
                mycursor.execute(sql)
                myresult=mycursor.fetchall()
                i=1;
                for row in myresult:
                    qty=mycart.count(row[0])
                    if(i%2!=0):
                        id=tree.insert("",END,values=(row[0],row[1],row[2],row[3],qty),tags=('oddrow',))
                    else:
                        id=tree.insert("",END,values=(row[0],row[1],row[2],row[3],qty),tags=('evenrow',))
                    i=i+1
                    dict2[id] = [row[0],row[3],qty]
                #print(dict2)
                Book_btn=Button(left_frame,text="Order Now",width=12,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",14,"bold"),command=Order_Food.Place_Order)
                Book_btn.place(relx=0.27,rely=0.75)
                changeOnHover(Book_btn,"#454693","#ffdada","#ffdada","#454693")

                Delete_btn=Button(left_frame,text="Delete Item",width=12,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",14,"bold"),command=Order_Food.Delete_Item)
                Delete_btn.place(relx=0.42,rely=0.75)
                changeOnHover(Delete_btn,"#454693","#ffdada","#ffdada","#454693")

                Increase_btn=Button(left_frame,text="Increase QTY",width=12,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",14,"bold"),command=Order_Food.Increase)
                Increase_btn.place(relx=0.57,rely=0.75)
                changeOnHover(Increase_btn,"#454693","#ffdada","#ffdada","#454693")

            except mysql.connector.Error as err:
                Label(left_frame, text="Unable To Fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
                Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)

            


class Restaurants():
    def Homepage():
        leftwidth=width1*0.8
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()
        #msg_lable=Label(left_frame,text="Restaurants",font =("helvetica",16,"bold"))
        #msg_lable.place(rely=0.20,relx=0.35)
        global dict4
        dict4={}
        try:
            sql="SELECT * From restaurants"
            global tree3
            tree3=ttk.Treeview(left_frame,column=("c1","c2"),show='headings')
            tree3.delete(*tree3.get_children())
            ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree3.yview)
            tree3.configure(yscroll=ybar.set)
            tree3.column("#1",anchor=CENTER)
            tree3.heading("#1",text="Res_ID")
            tree3.column("#2",anchor=CENTER,width=350)
            tree3.heading("#2",text="Restaurant_ID")
            tree3.place(rely=0.25,relx=0.28)

            tree3.tag_configure("evenrow",background='#9ddfd3',foreground='black')
            tree3.tag_configure("oddrow",background='#dbf6e9',foreground='black')

            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            i=1
            for row in myresult:
                #print(row)
                if(i%2!=0):
                    id=tree3.insert("",END,values=row,tags=('oddrow',))
                else:
                    id=tree3.insert("",END,values=row,tags=('evenrow',))
                i=i+1
                dict4[id]=row[0]
        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To Fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)

        Details_btn=Button(left_frame,text="View Food Available",width=19,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",14,"bold"),command=Restaurants.ResOrder)
        Details_btn.place(relx=0.38,rely=0.75)
        changeOnHover(Details_btn,"#454693","#ffdada","#ffdada","#454693")
        
    def ResOrder():
        selected_item = tree3.selection()[0]
        #res_id=dict4[selected_item][0]
        #print(selected_item)
        res_id=selected_item[3]
        #print(res_id)
        sql = "Select Food_ID,Dish,Res_Name,Price from Food, restaurants where restaurants.Res_ID=food.Res_ID and food.Res_ID ="+str(res_id)
        #print(sql)
        Order_Food.Homepage1(sql)


        
class My_Orders():
    def Order_Details():
        selected_item = tree1.selection()[0]
        o_id=dict3[selected_item][0]
        leftwidth=width1*0.8
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()
        msg_lable = Label(left_frame, text="Order Details",font=("Comic Sans MS",16,"bold"),fg="#454693",bg="#ffdada",borderwidth=0)
        msg_lable.place(rely=0.20,relx=0.40)
        try:
            sql = "SELECT order_detail.Food_ID,Dish,Res_Name,QTY,QTY*PRICE FROM order_detail,food,restaurants WHERE order_ID="+str(o_id)+" AND food.Food_ID=order_detail.Food_ID AND food.Res_ID=restaurants.RES_ID"
            #print(sql)
            global tree2
            tree2= ttk.Treeview(left_frame,column=("c1", "c2", "c3","c4","c5"),show='headings')
            tree2.delete(*tree2.get_children())
            ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree2.yview)
            tree2.configure(yscroll=ybar.set)
            tree2.column("#1",anchor=CENTER,width=100)
            tree2.heading("#1", text="Food_ID")
            tree2.column("#2",anchor=CENTER,width=275)
            tree2.heading("#2", text="Dish")
            tree2.column("#3",anchor=CENTER,width=275)
            tree2.heading("#3", text="Restaurant")
            tree2.column("#4",anchor=CENTER,width=100)
            tree2.heading("#4", text="Quantity")
            tree2.column("#5",anchor=CENTER,width=100)
            tree2.heading("#5", text="Cost")
            tree2.place(rely=0.30,relx=0.15)

            tree2.tag_configure("evenrow",background='#9ddfd3',foreground='black')
            tree2.tag_configure("oddrow",background='#dbf6e9',foreground='black')

            mycursor.execute(sql)
            myresult=mycursor.fetchall()

            i=1
            for row in myresult:
                #print(row)
                if(i%2!=0):
                    id=tree2.insert("",END,values=row,tags=('oddrow',))
                else:
                    id=tree2.insert("",END,values=row,tags=('evenrow',))
                i=i+1
        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To Fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)
        Orders_btn=Button(left_frame,text="Back To My Orders",width=19,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",18,"bold"),command=My_Orders.Homepage)
        Orders_btn.place(relx=0.4,rely=0.75)
        changeOnHover(Orders_btn,"#454693","#ffdada","#ffdada","#454693")

    def Homepage():
        leftwidth=width1*0.8
        left_frame=Frame(main_screen,width=leftwidth,height=height1,background="#ffdada")
        left_frame.place(relx=0.0,rely=0.0)
        left_frame.config()
        #msg_lable = Label(left_frame, text="Your Orders",font =("helvetica",16,"bold"))
        #msg_lable.place(rely=0.20,relx=0.35)
        try:
            sql = "Select Order_ID,DATE,COST from Orders where CUST_NUM ="+cust_num
            print(sql)
            mycursor.execute(sql)
            myresult=mycursor.fetchall()
            if(len(myresult)!=0):                    
                global tree1
                tree1=ttk.Treeview(left_frame,column=("c1", "c2", "c3"),show='headings')
                ybar=Scrollbar(left_frame,orient=VERTICAL,command=tree1.yview)
                tree1.configure(yscroll=ybar.set)
                tree1.column("#1",anchor=CENTER)
                tree1.heading("#1", text="Order_ID")
                tree1.column("#2",anchor=CENTER,width=350)
                tree1.heading("#2", text="Date-Time")
                tree1.column("#3",anchor=CENTER)
                tree1.heading("#3", text="Cost")
                tree1.place(rely=0.30,relx=0.20)

                tree1.tag_configure("evenrow",background='#9ddfd3',foreground='black')
                tree1.tag_configure("oddrow",background='#dbf6e9',foreground='black')

                i=1
                for row in myresult:
                    #print(row)
                    if(i%2!=0):
                        id=tree1.insert("",END,values=row,tags=('oddrow',))
                    else:
                        id=tree1.insert("",END,values=row,tags=('evenrow',))
                    i=i+1
                    dict3[id] = [row[0]]
                Details_btn=Button(left_frame,text="View Order Details",width=15,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",18,"bold"),command=My_Orders.Order_Details)
                Details_btn.place(relx=0.41,rely=0.75)
                changeOnHover(Details_btn,"#454693","#ffdada","#ffdada","#454693")

            else:
                pic("plate.png")
                global plate
                plate=img
                Label(left_frame,width=400,height=400,image=plate,borderwidth=0).place(relx=0.31,rely=0.15)
                Search1_btn=Button(left_frame,text="Search Food Here",width=15,height=1,bg="#ffdada",activebackground="#454693",activeforeground="#ffdada",foreground="#454693",borderwidth=0,font=("Comic Sans MS",18,"bold"),command=Navbar.Homepage)
                Search1_btn.place(relx=0.42,rely=0.80)
                changeOnHover(Search1_btn,"#454693","#ffdada","#ffdada","#454693")
  

        except mysql.connector.Error as err:
            Label(left_frame, text="Unable To Fetch Details", fg="red",font=("playful", 14)).place(relx=0.7,rely=0.70)
            Label(left_frame,text=err.msg,fg="red",font=("playful",12)).place(relx=0.7,rely=0.75)

        
        
        
class Register:
    def register():
        leftwidth=width1*0.5
        left_signup_screen=Frame(main_screen,width=leftwidth,height=height1,bg="#ffdada")
        left_signup_screen.place(relx=0.0,rely=0.0)
        left_signup_screen.config()
        pic("24-hours.png")
        global image1
        image1=img
        Label(left_signup_screen,image=image1,width=512,height=512,borderwidth=0).place(relx=0.1,rely=0.1)

        rightwidth=width1*0.55
        #print(leftwidth,rightwidth,width1)
        global right_signup_screen
        right_signup_screen=Frame(main_screen,width=leftwidth,height=height1,bg="#ffdada")
        right_signup_screen.place(relx=0.5,rely=0.0)
        right_signup_screen.config()        
        Label(right_signup_screen, text="Please enter details below to Register",borderwidth=0,bg="#ffdada",fg="#31326f",font=("helvetica",24,"bold")).place(relx=0.05,rely=0.1)
        
     
        global email
        global password
        global name
        global phone
        global name_entry
        global phone_entry
        global email_entry
        global password_entry
        email = StringVar()
        password = StringVar()
        name = StringVar()
        phone = StringVar()
        name_lable = Label(right_signup_screen,text="Name *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold"))
        name_lable.place(rely=0.26,relx=0.1)
        name_entry = Entry(right_signup_screen, textvariable=name,borderwidth=0,font =("helvetica",16,"bold"))
        name_entry.place(rely=0.26,relx=0.3)
        phone_lable = Label(right_signup_screen, text="Phone *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold"))
        phone_lable.place(rely=0.32,relx=0.1)
        phone_entry = Entry(right_signup_screen, textvariable=phone,borderwidth=0,font =("helvetica",16,"bold"))
        phone_entry.place(rely=0.32,relx=0.30)
        email_lable = Label(right_signup_screen, text="Email *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold"))
        email_lable.place(rely=0.38,relx=0.1)
        email_entry = Entry(right_signup_screen, textvariable=email,borderwidth=0,font =("helvetica",16,"bold"))
        email_entry.place(rely=0.38,relx=0.3)
        password_lable = Label(right_signup_screen, text="Password *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold"))
        password_lable.place(rely=0.44,relx=0.1)
        password_entry = Entry(right_signup_screen, textvariable=password,borderwidth=0,show='*',font =("helvetica",16,"bold"))
        password_entry.place(rely=0.44,relx=0.3)
        #Button(right_signup_screen,text="Register",width=10,height=1,bg="light green",command=).place(rely=0.55,relx=0.25)

        pic("register.png")
        global img_reg
        img_reg=img
        Button(right_signup_screen,width=148,height=42,image=img_reg,command=Register.register_user,borderwidth=0).place(rely=0.55,relx=0.24)

        pic("login1.png")
        global image3
        image3=img
        Button(right_signup_screen,width=125,height=125,image=image3,command=Login.login,borderwidth=0).place(rely=0.70,relx=0.25)
        #Button(right_signup_screen,text="Already A User... Login Here!!", width =20,height=1,bg="Yellow",command=Login.login).place(rely=0.75,relx=0.25)


    # Implementing event on register button         
    def register_user():
        email_info = email.get()
        password_info = password.get()
        phone_info=phone.get()
        name_info=name.get()
        try:                
            sql = "INSERT INTO user (name,phone,email,password) VALUES (%s,%s,%s,%s)" 
            val = (name_info,phone_info,email_info,password_info)
            mycursor.execute(sql,val)
            mydb.commit()
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            name_entry.delete(0, END)
            phone_entry.delete(0, END)
            Label(right_signup_screen, text="Registration Success", fg="green",font=("playful", 14)).place(relx=0.20,rely=0.65)
            time.sleep(3) # Sleep for 3 seconds
            Login.login()
        except mysql.connector.Error as err:
            Label(right_signup_screen, text="Registration Failed",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold","italic")).place(relx=0.2,rely=0.63)
            Label(right_signup_screen,text=err.msg,borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold","italic")).place(relx=0.2,rely=0.68)
            
class Login:
    # Designing window for login 
    def login():
        leftwidth=width1*0.5
        global left_login_screen
        left_login_screen=Frame(main_screen,width=leftwidth,height=height1,bg="#ffdada")
        left_login_screen.place(relx=0.0,rely=0.0)
        left_login_screen.config()

        pic("24-hours.png")
        global hours24
        hours24=img
        Label(left_login_screen,image=hours24,width=512,height=512,borderwidth=0).place(relx=0.1,rely=0.1)

        rightwidth=width1*0.55
        #print(leftwidth,rightwidth,width1)
        global right_login_screen
        right_login_screen=Frame(main_screen,width=leftwidth,height=height1,bg="#ffdada")
        right_login_screen.place(relx=0.5,rely=0.0)
        right_login_screen.config()        
        Label(right_login_screen,text="Please enter details below to Login",borderwidth=0,bg="#ffdada",fg="#31326f",font=("helvetica",24,"bold")).place(relx=0.05,rely=0.1)

        global phone_verify
        global password_verify
   
        phone_verify = StringVar()
        password_verify = StringVar()
 
        global phone_login_entry
        global password_login_entry

        Label(right_login_screen, text="Phone *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold")).place(rely=0.3,relx=0.10)
        phone_login_entry = Entry(right_login_screen, textvariable=phone_verify,font =("helvetica",16,"bold"),borderwidth=0,background="white")
        phone_login_entry.place(rely=0.31,relx=0.3)
        
        Label(right_login_screen, text="Password *",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold")).place(rely=0.4,relx=0.1)
        password_login_entry = Entry(right_login_screen, textvariable=password_verify,show='*',font =("helvetica",16,"bold"),borderwidth=0,background="white")
        password_login_entry.place(rely=0.39,relx=0.3)

        pic("signup.png")
        global image2
        image2=img
        pic("login.png")
        global img_login
        img_login=img
        
        Button(right_login_screen,width=148,height=44,image=img_login,command=Login.login_verify,borderwidth=0).place(rely=0.55,relx=0.24)
        Button(right_login_screen,width=125,height=125,image=image2,command=Register.register,borderwidth=0).place(rely=0.7,relx=0.26)

    # Implementing event on login button 
    def login_verify():
        phone1 = phone_verify.get()
        password1 = password_verify.get()
        mycursor.execute("Select phone,password from user")
        myresult=mycursor.fetchall()
        mycursor.execute("SELECT COUNT(*) FROM user")
        resultcount=mycursor.fetchone()
        #print(resultcount)
        count=0
        for x in myresult:
            count=count+1
            flag=0
            if x[0]==phone1:
                if x[1]==password1:
                    #print("Login Success")
                    global cust_num
                    cust_num=phone1
                    Navbar.navbar()
                    #Login Success
                else:
                    Login.password_not_recognised()
                    flag=1
                    break
            else:
                continue
        #print(resultcount[0],count)
        if resultcount[0]== count and flag==0:
            #print("user not found")
            Login.user_not_found()
        
    # Designing popup for login invalid password
    def password_not_recognised():
        Label(right_login_screen,text="Invalid Password !!",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold","italic")).place(rely=0.65,relx=0.22)
        password_login_entry.delete(0,END)
        
    # Designing popup for user not found
    def user_not_found():
        Label(right_login_screen,text="User Not Found !!",borderwidth=0,bg="#ffdada",fg="#31326f",font =("helvetica",16,"bold","italic")).place(rely=0.65,relx=0.22)     
        phone_login_entry.delete(0,END)
        password_login_entry.delete(0,END)
        

def main_screen():
    global main_screen
    main_screen = Tk()
    main_screen.state("zoomed")
    main_screen.resizable(width=FALSE, height=FALSE)
    main_screen.title("FUTURE FOOD")
    getDim()
    #Navbar.navbar()
    Login.login()
    #mb.showinfo("Order Placed", "Order Placed Successfully !!")
main_screen()
