from tkinter import *
from datetime import datetime

win = Tk()
win.title("TT filename generator")
win.geometry('550x600')


def onButtonClick():
    blankFlag = False
    # beginning of title
    ttStr = tt + " " + companyclicked.get() + ttCode.get()
    if companyclicked.get() == "":
        blankFlag = True
    if ttCode.get() == "":
        blankFlag = True
    # checking for division for SQCC only
    if companyclicked.get() == "SQCC":
        if divclicked.get() == "":
            blankFlag = True
        ttStr += " " + divclicked.get()
    # more of title
    ttStr += " " + bankclicked.get() + " " + curclicked.get() + " "
    if bankclicked.get() == "":
        blankFlag = True
    if curclicked.get() == "":
        blankFlag = True
    # amount formatting
    amountStr = ""
    statusGot = statusclicked.get()
    if statusGot == "":
        blankFlag = True
    # outgoing transfers -ve, incoming +ve, status format
    if statusGot == "Outgoing":
        statusGot += " transfer to "
        if amount.get() == "":
            blankFlag = True
        elif amount.get()[0] != '-':
            # amount to title
            amountStr += '-'
            amountStr += '{:,.2f}'.format(float(amount.get().replace(",", "")))
    else:
        statusGot += " transfer from "
        if amount.get() == "":
            blankFlag = True
        else:
            amountStr += '{:,.2f}'.format(float(amount.get().replace(",", "")))
    # 123,456,789.01 format
    if transactee.get() == "":
        blankFlag = True
    if bankref.get() == "":
        blankFlag = True
    if txn.get() == "":
        blankFlag = True
    ttStr += amountStr + " " + statusGot + transactee.get() + " - Bank ref " + bankref.get() + " Txn " + txn.get() + " "
    if txndesc.get() != "":
        ttStr += txndesc.get() + " "
    # date validation and correction
    dateStr = date.get()
    if dateStr == "":
        blankFlag = True
    else:
        try:
            dateObj = datetime.strptime(dateStr, "%d-%m-%Y")
            ttStr += dateStr
        except ValueError:
            try:
                dateObj = datetime.strptime(dateStr, "%d/%m/%Y")
                dateFormatted = dateObj.strftime("%d-%m-%Y")
                ttStr += dateFormatted
            except ValueError:
                dateFormatError()
    # static length check
    if len(ttStr) <= 255:
        if not blankFlag:
            clipCopy(ttStr)
        else:
            fieldLeftBlank()
    else:
        lengthOverflow()


def boxClear(event):
    event.widget.delete(0, "end")
    return None


def clipCopy(copyStr):
    win.clipboard_clear()
    win.clipboard_append(copyStr)
    win.update()
    outputLabel.configure(text="Generated and copied!", fg="green")


def lengthOverflow():
    outputLabel.configure(
        text="Max length of 255 characters exceeded!", fg="red")


def dateFormatError():
    outputLabel.configure(text="Invalid date entered!", fg="red")


def fieldLeftBlank():
    outputLabel.configure(text="Required field left blank!", fg="red")


tt = "TT"
# Company
companyclicked = StringVar()
companyLabel = Label(win, text="Company", pady=7)
companyLabel.grid(row=0, column=0)
companyList = ["", "AR", "SQSS", "SQCC", "BA"]
companyclicked.set(companyList[1])
companyDrop = OptionMenu(win, companyclicked, *companyList)
companyDrop.grid(row=0, column=1)
# TT Code
ttCodeLabel = Label(win, text="TT Code")
ttCodeLabel.grid(row=1, column=0)
ttCode = Entry(win, width=50)
ttCode.grid(row=1, column=1)
# Division (for SQCC only)
divclicked = StringVar()
divLabel = Label(win, text="Division (for SQCC only)")
divLabel.grid(row=2, column=0)
divList = ["", "WH", "FS", "IT", "ST", "TY"]
divclicked.set(divList[0])
divDrop = OptionMenu(win, divclicked, *divList)
divDrop.grid(row=2, column=1)
# Bank
bankclicked = StringVar()
bankLabel = Label(win, text="Bank")
bankLabel.grid(row=3, column=0)
bankList = ["", "NCB", "RB", "ALJ"]
bankclicked.set(bankList[1])
bankDrop = OptionMenu(win, bankclicked, *bankList)
bankDrop.grid(row=3, column=1)
# Currency
curclicked = StringVar()
curLabel = Label(win, text="Currency")
curLabel.grid(row=4, column=0)
curList = ["", "SR", "USD"]
curclicked.set(curList[1])
curDrop = OptionMenu(win, curclicked, *curList)
curDrop.grid(row=4, column=1)
# Amount
amountLabel = Label(win, text="Amount")
amountLabel.grid(row=5, column=0)
amount = Entry(win, width=50)
amount.grid(row=5, column=1)
# Status
statusclicked = StringVar()
statusLabel = Label(win, text="Status")
statusLabel.grid(row=6, column=0)
statusList = ["", "Outgoing", "Incoming"]
statusclicked.set(statusList[1])
statusDrop = OptionMenu(win, statusclicked, *statusList)
statusDrop.grid(row=6, column=1)
# Transactee
transacteeLabel = Label(win, text="Vendor/Customer")
transacteeLabel.grid(row=7, column=0)
transactee = Entry(win, width=50)
transactee.grid(row=7, column=1)
# Bank reference number
bankrefLabel = Label(win, text="Bank ref.")
bankrefLabel.grid(row=8, column=0)
bankref = Entry(win, width=50)
bankref.grid(row=8, column=1)
# Txn reference number
txnLabel = Label(win, text="Transaction no.")
txnLabel.grid(row=9, column=0)
txn = Entry(win, width=50)
txn.grid(row=9, column=1)
# Txn description
txndescLabel = Label(win, text="Details")
txndescLabel.grid(row=10, column=0)
txndesc = Entry(win, width=50)
txndesc.grid(row=10, column=1)
# Date
dateLabel = Label(win, text="Date (DD-MM-YYYY)")
dateLabel.grid(row=11, column=0)
date = Entry(win, width=50)
date.grid(row=11, column=1)

# Execution button
copyButton = Button(
    win, text="Generate and copy to clipboard", command=onButtonClick)
copyButton.grid(row=12, column=0)

outputLabel = Label(win, text="", pady=10)
outputLabel.grid(row=12, column=1)

win.mainloop()
