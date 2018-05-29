from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import datetime
import threading
import win32com.client

#UI 
root = Tk()
root.title("Mail Checker v1.0 by Rahul Pareek")
root.geometry("500x150")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Sbj = StringVar()
timeIntrvl = StringVar()

subject_entry = ttk.Entry(mainframe, width=50, textvariable=Sbj)
subject_entry.grid(column=2, row=1, sticky=(W, E))

time_entry = ttk.Entry(mainframe, width=7, textvariable=timeIntrvl)
time_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Subject :   ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Time Interval(minutes) :   ").grid(column=1, row=2, sticky=W)

first = True

def dummy():
    x = x+1

def Start():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    totalseconds = int(timeIntrvl.get())*60
    found = False

    for message in messages:
        if message.Subject == Sbj.get():
            found = True
            rcvdtime = message.ReceivedTime
            currtime = datetime.datetime.now(rcvdtime.tzinfo)
            if int(rcvdtime.timestamp() - currtime.timestamp()) > totalseconds:
                msg = Sbj.get() + " - Failure"
                tkinter.messagebox.showerror(title="Alert", message=msg)
                break
            else:
                remtime = totalseconds - int(rcvdtime.timestamp() - currtime.timestamp()) + 60
                t = threading.Timer(remtime, dummy)
                t.start()
                t.join()
                inbox2 = outlook.GetDefaultFolder(6)
                messages2 = inbox2.Items
                for message2 in messages2:
                    if message2.Subject == Sbj.get():
                        rcvdtime2 = message2.ReceivedTime
                        currtime2 = datetime.datetime.now(rcvdtime2.tzinfo)
                        if int(rcvdtime2.timestamp() - currtime2.timestamp()) > remtime:
                            msg = Sbj.get() + "  - Fail"
                            tkinter.messagebox.showerror(title="Alert", message=msg)
                        break
            break
    if found == False:
        tkinter.messagebox.showerror(title="Alert", message="No message found till now")
        exit()

    while True:
        t = threading.Timer(totalseconds, dummy)
        t.start()
        t.join()
        inbox3 = outlook.GetDefaultFolder(6)
        messages3 = inbox3.Items

        for message3 in messages3:
            if message3.Subject == Sbj.get():
                rcvdtime3 = message3.ReceivedTime
                currtime3 = datetime.datetime.now(rcvdtime3.tzinfo)
                if int(rcvdtime3.timestamp() - currtime3.timestamp()) > totalseconds:
                    msg = Sbj.get() + "  - Failed"
                    tkinter.messagebox.showerror(title="Alert", message=msg)
                break    
    
def Stop():
    exit()

start_btn = ttk.Button(mainframe, text="START", command=Start) 
start_btn.grid(column=1, row=3)

stop_btn = ttk.Button(mainframe, text="STOP", command=Stop) 
stop_btn.grid(column=2, row=3)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
