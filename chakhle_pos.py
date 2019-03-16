from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="CHAKH LE RESTAURANT ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Submit():
    if (Dinein.get()==""):
        CoDinein=0
    else:
        CoDinein=float(Dinein.get())
    
    if (Card.get()==""):
        CoCard=0
    else:
        CoCard=float(Card.get())

    if (Paytm.get()==""):
        CoPaytm=0
    else:
        CoPaytm=float(Paytm.get())

    if (Swiggy.get()==""):
        CoSwiggy=0
    else:
        CoSwiggy=float(Swiggy.get())
        
    if (Zomato.get()==""):
        CoZomato=0
    else:
        CoZomato=float(Zomato.get())

    if (Foodpanda.get()==""):
        CoFoodpanda=0
    else:
        CoFoodpanda=float(Foodpanda.get())

    if (Expenses.get()==""):
        CoExpenses=0
    else:
        CoExpenses=float(Expenses.get())

    if (Bw.get()==""):
        CoBw=0
    else:
        CoBw=float(Bw.get())

    if (Prev_cash.get()==""):
        CoPrev_cash=0
    else:
        CoPrev_cash=float(Prev_cash.get())

    if (Cash_Hand.get()==""):
        CoCash_Hand=0
    else:
        CoCash_Hand=float(Cash_Hand.get())

    CostofMeal= "Rs", str('%.2f' % (CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostBurger+CostSandwich))
    
    
def qExit():
    root.destroy()

def Reset():
    Dinein.set("")
    Card.set("")
    Paytm.set("")
    Swiggy.set("")
    Zomato.set("")
    Foodpanda.set("")
    Expenses.set("")
    Bw.set("")
    Prev_cash.set("")
    Cash_Hand.set("")

def Display():
    txtReference.setvar(Dinein)
    txtFries.setvar(Card)
    txtNoodles.setvar(Paytm)
    txtSoup.setvar(Swiggy)
    txtBurger.setvar(Zomato)
    txtSandwich.setvar(Foodpanda)
    

    
#====================================Restaraunt Info 1===========================================================
Dinein = StringVar()
Card = StringVar()
Paytm = StringVar()
Swiggy = StringVar()
Zomato = StringVar()
Foodpanda = StringVar()
Expenses = StringVar()
Bw = StringVar() #Bank Withdrawl
Prev_cash = StringVar()
Cash_Hand = StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Cash (Dine-in\Take-away)",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=Dinein,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries= Label(f1, font=('arial', 16, 'bold'),text="Card (Dine-in\Take-away)",bd=16,anchor="w")
lblFries.grid(row=1, column=0)
txtFries=Entry(f1, font=('arial',16,'bold'),textvariable=Card,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)


lblNoodles= Label(f1, font=('arial', 16, 'bold'),text="Paytm\PhonePe",bd=16,anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Paytm,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNoodles.grid(row=2,column=1)


lblSoup= Label(f1, font=('arial', 16, 'bold'),text="Swiggy",bd=16,anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Swiggy,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSoup.grid(row=3,column=1)

lblBurger= Label(f1, font=('arial', 16, 'bold'),text="Zomato",bd=16,anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Zomato,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBurger.grid(row=4,column=1)

lblSandwich= Label(f1, font=('arial', 16, 'bold'),text="FoodPanda",bd=16,anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Foodpanda,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSandwich.grid(row=5,column=1)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Expenses",bd=16,anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Expenses,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Bank Withdrawl",bd=16,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Bw,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Prev Cash",bd=16,anchor="w")
lblService.grid(row=2, column=2)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Prev_cash,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=3)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="Cash in Hand",bd=16,anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Cash_Hand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=3)

#==========================================Buttons==========================================================================================
btnSubmit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Add",bg="powder blue",command=Submit).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

btnDisplay=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Display",bg="powder blue",command=Display).grid(row=8,column=1)


root.mainloop()


