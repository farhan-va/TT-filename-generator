from tkinter import *

win = Tk()
win.title("TT filename generator")
win.geometry('500x600')


def onButtonClick():
    # beginning of title
    ttStr = tt + " " + companyclicked.get() + ttcode.get()
    # checking for division for SQCC only
    if companyclicked.get() == "SQCC":
        ttStr += " " + divclicked.get()
    # more of title
    ttStr += " " + bankclicked.get() + " " + curclicked.get() + " "
    # amount formatting
    amountStr = ""
    statusGot = statusclicked.get()
    # outgoing transfers -ve, incoming +ve
    if statusGot == "Outgoing":
        amountStr += '-'
    # 123,456,789.01 format
    amountStr += '{:,.2f}'.format(float(amount.get()))
    # amount to title
    ttStr += amountStr + " "
    # status format
    if statusGot == "Outgoing":
        statusGot += " transfer to "
    else:
        statusGot += " transfer from "
    # combining rest of the title
    ttStr += statusGot + transactee.get() + " - Bank ref " + bankref.get() + " Txn " + \
        txn.get() + " " + txndesc.get() + " " + date.get()
    # checking for length of string, static
    if len(ttStr) <= 175:
        clipCopy(ttStr)
    else:
        lengthOverflow()


def boxClear(event):
    event.widget.delete(0, "end")
    return None


def clipCopy(copyStr):
    win.clipboard_clear()
    win.clipboard_append(copyStr)
    win.update()
    outputLabel.configure(text="Generated and copied!", fg="black")


def lengthOverflow():
    outputLabel.configure(text="Max length of 175 characters exceeded!", fg="red")


tt = "TT"

companyList = ["AR", "SQSS", "SQCC", "BA"]
companyclicked = StringVar()
companyclicked.set(companyList[0])
companyDrop = OptionMenu(win, companyclicked, *companyList)
companyDrop.pack(pady=7)

ttcode = Entry(win, width=50)
ttcode.pack(pady=7)
ttcode.insert(0, "Enter TT code here")
ttcode.bind("<FocusIn>", boxClear)

divList = ["", "WH", "FS", "IT", "ST", "TY"]
divclicked = StringVar()
divclicked.set(divList[0])
divDrop = OptionMenu(win, divclicked, *divList)
divDrop.pack(pady=7)

bankList = ["NCB", "RB", "ALJ"]
bankclicked = StringVar()
bankclicked.set(bankList[0])
bankDrop = OptionMenu(win, bankclicked, *bankList)
bankDrop.pack(pady=7)

curList = ["SR", "USD"]
curclicked = StringVar()
curclicked.set(curList[0])
curDrop = OptionMenu(win, curclicked, *curList)
curDrop.pack(pady=7)

amount = Entry(win, width=50)
amount.pack(pady=7)
amount.insert(0, "Enter amount here")
amount.bind("<FocusIn>", boxClear)

statusList = ["Outgoing", "Incoming"]
statusclicked = StringVar()
statusclicked.set(statusList[0])
statusDrop = OptionMenu(win, statusclicked, *statusList)
statusDrop.pack(pady=7)

transactee = Entry(win, width=50)
transactee.pack(pady=7)
transactee.insert(0, "Enter vendor/customer name here")
transactee.bind("<FocusIn>", boxClear)

bankref = Entry(win, width=50)
bankref.pack(pady=7)
bankref.insert(0, "Enter bank ref. no. here")
bankref.bind("<FocusIn>", boxClear)

txn = Entry(win, width=50)
txn.pack(pady=7)
txn.insert(0, "Enter transaction no. here")
txn.bind("<FocusIn>", boxClear)

txndesc = Entry(win, width=50)
txndesc.pack(pady=7)
txndesc.insert(0, "Enter additional details here")
txndesc.bind("<FocusIn>", boxClear)

date = Entry(win, width=50)
date.pack(pady=7)
date.insert(0, "Enter date here (DD-MM-YYYY)")
date.bind("<FocusIn>", boxClear)

copyButton = Button(
    win, text="Generate and copy to clipboard", command=onButtonClick)
copyButton.pack(pady=12)

outputLabel = Label(win, text="")
outputLabel.pack(pady=10)

win.mainloop()