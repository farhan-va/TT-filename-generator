import base64
from tkinter import *
from datetime import datetime

win = Tk()
win.title("TT Filename Generator")
win.geometry("600x700")
# win.iconbitmap("D:\\Chrome Downloads\\icons8-bank-64.ico")

iconimgdata = (
    b"iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAABmJLR0QA/wD/A"
    b"P+gvaeTAAAEIElEQVR4nO2a3U9jRRiHnzmlCLFFobjs0nLO8cYYyMYL71aNbo"
    b"wXfi3Il0aFuP/J/idmITHIhwQ37iYmGhJ345Um3hD1YjmnH8CyoFt2F6TldLw"
    b"oB9vSYiktQ+l57jrTeec3v7zzziRzwKOxEUpm/eibl5DOGFJ8klUhpxC+SeYH"
    b"/zxtKadnwMD888i9ayDGgLeLzy1+QcpJnsl8xczow9OQVVsDRqabSWvvIeU4i"
    b"PeBZgC/308kHOZFUwdg2YoSTyRIp9PuyBTI7xBiAn/mNjOjqVpJrI0BH872oY"
    b"kxkNeBC9mJBBe6XsA0dCLhME1NTXlDHMfhwYN1rGiURHyFjMy4Ev9Gyhl8mUn"
    b"mR+6BkNWUWj0DBuci7Mkh4DqCV9zmtrY2TEPHNA1aW1rKCpVKpYjFE1i2zcbG"
    b"Zm7XHwg5hU+bYG7ofjVkn8yAkelWdsUHIMYRvAv4AFpbWujpiWAaOu3t7SeaI"
    b"pncIpaIYy3bPN3edpszwM8IMcHuzhR3Pt+qNP7xDbhxQ+O33is42hiCT4EAgM"
    b"/no7v7Eqauc/FSF5rQKtVUFIlkc2MTy45i2zH2nD236x+EuIWUkyRDd1i8und"
    b"UnELKN6B/uhchRpHiC8DIDhaEOjswDQO9J4Lf7z/O3BXjOA4rK6tYdpTVtTWk"
    b"PCgLq8AMGXGTW0O/lhPraANGpjtI+4azVZzX3OZgMIiuRzB1g0Dg2QqXUR22d"
    b"3aIxxMsWxaPHiVzu5ZATpCWN7k9ulZq/GED3vqyheeC7yDEGFIOAH7IHl36/r"
    b"7uDHWqukIdSTK5hR2Ncn/ZYnd3123OAD+CnGRnZ47vx5/mjvlvGQPTryK1ceA"
    b"zIASgaRoXu7owDZ1wuBtNq+6+rhVSStbXH2LZNrF4Asdx3K4tYAHEBAuDP4CQ"
    b"WQOuzS0i5Jvuv0KhDkxDR+/pobm5+fRXUEVSqRTRWAzLjrK5+Vdu1yILw1ezB"
    b"vTPSoDe3pcxDYNgIKBAau15/OQJlm2ztPR7tmFhOP+sutzXd24XDxAMBLjc15"
    b"fXlncf/Xpm7lQFnQWyGSDFXcU6VPDT4ab+WenWg3NJkfXVx7lWQ5qKtp7nLCg"
    b"gPwMaoxbk7f3SF9r9LPh4ZKisqAcnyMLw4ZhnNRZeDShRA3Ko5t3gLMYqnQGV"
    b"1YMiZ+sZjlU2pe4Hldwbzlishq8BngGqBajGM0C1ANV4BqgWoBrPANUCVOMZo"
    b"FqAajwDVAtQjWeAagGq8QxQLUA1ngGqBajGM0C1ANUc9TJ0D7hyrGhS3OXboT"
    b"fqJhZHZ8DxJgEQ8vU6i/X/L0PHfoOrs1heDcj7Vcn+qjcK6kFhBpzvxcOhelC"
    b"8BpR4S697irwXejUAaIy9X8h+LXAzoLEWDwe1IK8GlHu21ju5d4OGrwHet8JA"
    b"o3wfWMgJvxvyOB/8CwVigOilN+7CAAAAAElFTkSuQmCC"
)

img = base64.b64decode(iconimgdata)
photo = PhotoImage(data=img)
win.iconphoto(False, photo)


def onCopyClick():
    blankFlag = False
    invalidFlag = False
    # beginning of title
    ttStr = tt + " " + company.get() + ttCode.get()
    if company.get() == "":
        blankFlag = True
    if ttCode.get() == "":
        blankFlag = True
    # checking for division for SQCC only
    if company.get() == "SQCC":
        if div.get() == "":
            blankFlag = True
        ttStr += " " + div.get()
    # more of title
    ttStr += " " + bank.get() + " " + cur.get() + " "
    if bank.get() == "":
        blankFlag = True
    if cur.get() == "":
        blankFlag = True
    # amount formatting
    amountStr = ""
    statusSet = ""
    # outgoing transfers -ve, incoming +ve, status format
    if not blankFlag:
        if any(c.isalpha() for c in amount.get()):
            invalidFlag = True
            invalidData("Amount")
        else:
            amountStr += "{:,.2f}".format(float(amount.get().replace(",", "")))
            if amount.get()[0] == "-":
                statusSet = "Outgoing"
            else:
                statusSet = "Incoming"
    # 123,456,789.01 format
    if transactee.get() == "":
        blankFlag = True
    if bankref.get() == "":
        blankFlag = True
    if txn.get() == "":
        blankFlag = True
    ttStr += (
        amountStr
        + " "
        + statusSet
        + " "
        + transactee.get()
        + " - Bank ref "
        + bankref.get()
        + " Txn "
        + txn.get()
        + " "
    )
    if txnDesc.get() != "":
        ttStr += txnDesc.get() + " "
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
                invalidFlag = True
                invalidData("Date")
    # static length check
    if len(ttStr) <= 255:
        if blankFlag:
            fieldLeftBlank()
        elif not invalidFlag:
            clipCopy(ttStr)
    else:
        lengthOverflow()
    win.after(5000, clearLabel)


def onResetClick():
    company.set(companyList[1])
    ttCodeEntry.delete(0, END)
    div.set(divList[0])
    bank.set(bankList[1])
    cur.set(curList[1])
    amountEntry.delete(0, END)
    transacteeEntry.delete(0, END)
    bankrefEntry.delete(0, END)
    txnEntry.delete(0, END)
    txnDescEntry.delete(0, END)
    dateEntry.delete(0, END)
    outputDisplayText.delete("1.0", END)
    ttCodeEntry.focus_set()
    win.after(5000, clearLabel)
    resetLabel.configure(text="All fields cleared!")


def boxClear(event):
    event.widget.delete(0, "end")
    return None


def clipCopy(copyStr):
    win.clipboard_clear()
    win.clipboard_append(copyStr)
    win.update()
    outputLabel.configure(text="Generated and copied!", fg="green")
    outputDisplayText.insert(END, copyStr)


def lengthOverflow():
    outputLabel.configure(text="Max length of 255 characters exceeded!", fg="red")


def fieldLeftBlank():
    outputLabel.configure(text="Required field(s) left blank!", fg="red")


def invalidData(fieldName):
    outputLabel.configure(text="Invalid data in '" + fieldName + "' field!", fg="red")


def clearLabel():
    outputLabel.configure(text="")
    resetLabel.configure(text="")


tt = "TT"
# Main frame
mainFrame = Frame(win, padx=7, pady=7)
mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
# Inputs frame
inputsFrame = Frame(mainFrame, padx=7, pady=7)
inputsFrame.grid(row=0, column=0)
# Header
headerLabel = Label(
    win,
    text="TT Filename Generator",
    font=("Consolas", 18),
    fg="dark blue",
    padx=10,
    pady=15,
)
headerLabel.place(relx=0.5, anchor=N)
# Footer
footerLabel = Label(
    win, text="Made by Farhan Arshad\nVersion 0.7.2", fg="grey", padx=7, pady=7
)
footerLabel.place(relx=1, rely=1, anchor=SE)
# Company
company = StringVar()
companyLabel = Label(inputsFrame, text="Company: ", pady=7)
companyLabel.grid(row=0, column=0, sticky=E)
companyList = ["", "AR", "SQSS", "SQCC", "BA"]
company.set(companyList[1])
companyDrop = OptionMenu(inputsFrame, company, *companyList)
companyDrop.grid(row=0, column=1, sticky=W, pady=3)
# TT Code
ttCode = StringVar()
ttCodeLabel = Label(inputsFrame, text="TT Code: ")
ttCodeLabel.grid(row=1, column=0, sticky=E)
ttCodeEntry = Entry(inputsFrame, textvariable=ttCode, width=50)
ttCodeEntry.grid(row=1, column=1, pady=3)
# Division (for SQCC only)
div = StringVar()
divLabel = Label(inputsFrame, text="Division (for SQCC only): ")
divLabel.grid(row=2, column=0, sticky=E)
divList = ["", "WH", "FS", "IT", "ST", "TY"]
div.set(divList[0])
divDrop = OptionMenu(inputsFrame, div, *divList)
divDrop.grid(row=2, column=1, sticky=W, pady=3)
# Bank
bank = StringVar()
bankLabel = Label(inputsFrame, text="Bank: ")
bankLabel.grid(row=3, column=0, sticky=E)
bankList = ["", "NCB", "RB", "ALJ"]
bank.set(bankList[1])
bankDrop = OptionMenu(inputsFrame, bank, *bankList)
bankDrop.grid(row=3, column=1, sticky=W, pady=3)
# Currency
cur = StringVar()
curLabel = Label(inputsFrame, text="Currency: ")
curLabel.grid(row=4, column=0, sticky=E)
curList = ["", "SR", "USD"]
cur.set(curList[1])
curDrop = OptionMenu(inputsFrame, cur, *curList)
curDrop.grid(row=4, column=1, sticky=W, pady=3)
# Amount
amount = StringVar()
amountLabel = Label(inputsFrame, text="Amount: ")
amountLabel.grid(row=5, column=0, sticky=E)
amountEntry = Entry(inputsFrame, textvariable=amount, width=50)
amountEntry.grid(row=5, column=1, pady=3)
# Transactee
transactee = StringVar()
transacteeLabel = Label(inputsFrame, text="Vendor/Customer: ")
transacteeLabel.grid(row=6, column=0, sticky=E)
transacteeEntry = Entry(inputsFrame, textvariable=transactee, width=50)
transacteeEntry.grid(row=6, column=1, pady=3)
# Bank reference number
bankref = StringVar()
bankrefLabel = Label(inputsFrame, text="Bank ref.: ")
bankrefLabel.grid(row=7, column=0, sticky=E)
bankrefEntry = Entry(inputsFrame, textvariable=bankref, width=50)
bankrefEntry.grid(row=7, column=1, pady=3)
# Txn reference number
txn = StringVar()
txnLabel = Label(inputsFrame, text="Transaction no.: ")
txnLabel.grid(row=8, column=0, sticky=E)
txnEntry = Entry(inputsFrame, textvariable=txn, width=50)
txnEntry.grid(row=8, column=1, pady=3)
# Txn description
txnDesc = StringVar()
txnDescLabel = Label(inputsFrame, text="Details: ")
txnDescLabel.grid(row=9, column=0, sticky=E)
txnDescEntry = Entry(inputsFrame, textvariable=txnDesc, width=50)
txnDescEntry.grid(row=9, column=1, pady=3)
# Date
date = StringVar()
dateLabel = Label(inputsFrame, text="Date (DD-MM-YYYY): ")
dateLabel.grid(row=10, column=0, sticky=E)
dateEntry = Entry(inputsFrame, textvariable=date, width=50)
dateEntry.grid(row=10, column=1, pady=3)

# Execution button
copyButton = Button(
    inputsFrame, text="Generate and copy to clipboard", command=onCopyClick
)
copyButton.grid(row=11, column=0, pady=10)
# Result indicator
outputLabel = Label(inputsFrame, text="", pady=10)
outputLabel.grid(row=11, column=1)
# Reset button
resetButton = Button(inputsFrame, text="Reset fields", command=onResetClick)
resetButton.grid(row=12, column=1, pady=5)
# Reset indicator
resetLabel = Label(inputsFrame, text="", pady=5)
resetLabel.grid(row=12, column=0)
# Output display
outputDisplayLabel = Label(mainFrame, text="File name: ")
outputDisplayLabel.grid(row=1, column=0, sticky=W, padx=42)
outputDisplayText = Text(mainFrame, height=3, width=50)
outputDisplayText.grid(row=2, column=0)
# Cursor focus
ttCodeEntry.focus_set()

win.mainloop()
