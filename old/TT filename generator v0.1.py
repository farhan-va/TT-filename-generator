from tkinter import *

win = Tk()
win.title("TT filename generator")

tt = "TT"

companyList = ["AR", "SQSS", "SQCC", "BA"]
companyclicked = StringVar()
companyclicked.set(companyList[0])
companyDrop = OptionMenu(win, companyclicked, *companyList)
companyDrop.pack()

ttcode = Entry(win, width = 50)
ttcode.pack()
ttcode.insert(0, "Enter TT code here")

divList = ["", "WH", "FS", "IT", "ST", "TY"]
divclicked = StringVar()
divclicked.set(divList[0])
divDrop = OptionMenu(win, divclicked, *divList)
divDrop.pack()

bankList = ["NCB", "RB", "ALJ"]
bankclicked = StringVar()
bankclicked.set(bankList[0])
bankDrop = OptionMenu(win, bankclicked, *bankList)
bankDrop.pack()

curList = ["SR", "USD"]
curclicked = StringVar()
curclicked.set(curList[0])
curDrop = OptionMenu(win, curclicked, *curList)
curDrop.pack()

amount = Entry(win, width = 50)
amount.pack()
amount.insert(0, "Enter amount here")

statusList = ["Outgoing to", "Incoming from"]
statusclicked = StringVar()
statusclicked.set(statusList[0])
statusDrop = OptionMenu(win, statusclicked, *statusList)
statusDrop.pack()

transactee = Entry(win, width = 50)
transactee.pack()
transactee.insert(0, "Enter vendor/customer name here")

bankref = Entry(win, width = 50)
bankref.pack()
bankref.insert(0, "Enter bank ref. no. here")

txn = Entry(win, width = 50)
txn.pack()
txn.insert(0, "Enter transaction no. here")

txndesc = Entry(win, width = 50)
txndesc.pack()
txndesc.insert(0, "Enter additional details here")

date = Entry(win, width = 50)
date.pack()
date.insert(0, "Enter date here (DD-MM-YYYY)")


def clipCopy():   
    ttstring = tt + " " + companyclicked.get() + " " + ttcode.get()
    if companyclicked.get() == "SQCC":
        ttstring += " " + divclicked.get()
    ttstring += " " + bankclicked.get() + " " + curclicked.get() + " " + amount.get() + " " + statusclicked.get() + " " + transactee.get() + " - Bank ref " + bankref.get() + " Txn " + txn.get() + " " + txndesc.get() + " " + date.get()
    win.clipboard_clear()
    win.clipboard_append(ttstring)
    win.update()
    copyLabel = Label(win, text = "Generated and copied!")
    copyLabel.pack()

clickButton = Button(win, text = "Generate and copy to clipboard", command = clipCopy)
clickButton.pack()

win.mainloop()