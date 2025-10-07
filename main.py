import base64
from tkinter import *
from datetime import datetime
import json
import os
import re

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


def on_copy() -> None:
    # json record initiation
    record = {
        "Company": "",
        "Division": "",
        "Bank": "",
        "Currency": "",
        "Amount": "",
        "Transactee": "",
        "Bank Ref": "",
        "Txn No": "",
        "Details": "",
        "Date": "",
    }

    blank_flag = False
    invalid_flag = False

    # beginning of title
    ttc = company.get() + tt_code.get()

    tt_str = tt + " " + ttc
    if company.get() == "":
        blank_flag = True
    if tt_code.get() == "":
        blank_flag = True

    record["Company"] = company.get()

    # checking for division for SQCC only
    if company.get() == "SQCC":
        if sqcc_div.get() == "":
            blank_flag = True
        tt_str += " " + sqcc_div.get()
        record["Division"] = sqcc_div.get()

    # more of title
    tt_str += " " + bank.get() + " " + currency.get() + " "
    if bank.get() == "":
        blank_flag = True
    if currency.get() == "":
        blank_flag = True

    record["Bank"] = bank.get()
    record["Currency"] = currency.get()

    # amount formatting
    amount_str = ""
    status_set = ""

    # outgoing transfers -ve, incoming +ve, status format
    if not blank_flag:
        amount_num = amount.get().strip()
        if any(c.isalpha() for c in amount_num):
            invalid_flag = True
            invalid_data_msg("Amount")
        else:
            amount_str += "{:,.2f}".format(float(amount.get().replace(",", "")))
            if (
                "-" in amount.get()
            ):  # instead of checking if 1st char is -, check if it contains a - at all
                status_set = "to"
            else:
                status_set = "Incoming from"

    # 123,456,789.01 format
    if transactee.get() == "":
        blank_flag = True
    if bankref.get() == "":
        blank_flag = True
    if txn.get() == "":
        blank_flag = True
    tt_str += (
        amount_str
        + " "
        + status_set
        + " "
        + transactee.get()
        + " - Bank ref "
        + bankref.get()
        + " Txn "
        + txn.get()
        + " "
    )

    record["Amount"] = amount_str
    record["Transactee"] = transactee.get()
    record["Bank Ref"] = bankref.get()
    record["Txn No"] = txn.get()

    if details.get() != "":
        tt_str += details.get() + " "
        record["Details"] = details.get()

    # date validation and correction
    date_str = date.get()
    if date_str == "":
        blank_flag = True
    else:
        try:
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")
            tt_str += date_str
            record["Date"] = date_str
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                date_formatted = date_obj.strftime("%d-%m-%Y")
                tt_str += date_formatted
                record["Date"] = date_formatted
            except ValueError:
                invalid_flag = True
                invalid_data_msg("Date")

    # if tt_str contains a tab character, remove it
    tt_str = tt_str.replace("\t", "")

    # static length check
    if len(tt_str) <= 255:
        if blank_flag:
            field_blank_msg()
            win.after(5000, clear_output_label)
        elif not invalid_flag:
            copy_to_clipboard(tt_str)
            save_record(ttc, record)
            win.after(5000, clear_output_label)
    else:
        length_overflow_msg()
        win.after(5000, clear_output_label)


def reset_fields() -> None:
    company.set(company_list[1])
    tt_code_entry.delete(0, END)
    sqcc_div.set(sqcc_div_list[0])
    bank.set(bank_list[1])
    currency.set(currency_list[1])
    amount_entry.delete(0, END)
    transactee_entry.delete(0, END)
    bankref_entry.delete(0, END)
    txn_entry.delete(0, END)
    details_entry.delete(0, END)
    date_entry.delete(0, END)
    output_display_text.delete("1.0", END)
    tt_code_entry.focus_set()


def on_reset() -> None:
    reset_fields()
    date_entry.insert(END, get_date())
    reset_label.configure(text="All fields cleared!")
    win.after(5000, clear_reset_label)


def output_clear(event: Event) -> None:
    event.widget.delete(0, "end")
    return None


def copy_to_clipboard(copy_str: str) -> None:
    win.clipboard_clear()
    win.clipboard_append(copy_str)
    win.update()
    output_label.configure(text="Generated and copied!", fg="green")
    output_display_text.insert(END, copy_str)


def get_date() -> str:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y")
    return formatted_date


def length_overflow_msg() -> None:
    output_label.configure(text="Max length of 255 characters exceeded!", fg="red")


def field_blank_msg() -> None:
    output_label.configure(text="Required field(s) left blank!", fg="red")


def invalid_data_msg(field_name: str) -> None:
    output_label.configure(text="Invalid data in '" + field_name + "' field!", fg="red")


def clear_output_label() -> None:
    output_label.configure(text="")


def clear_reset_label() -> None:
    reset_label.configure(text="")


def save_record(ttc: str, record: json) -> None:
    with open(records_file, "r") as file:
        records = json.load(file)

    if records == "":
        records = {}

    # Add the new record to the existing records
    records[ttc] = record

    # Write all records to the file
    with open(records_file, "w") as file:
        json.dump(records, file, indent=4)


def search_record(ttc: str, tt_num: str) -> None:
    try:
        with open(records_file, "r") as file:
            records = json.load(file)

            try:
                saved_record = records.get(ttc)
                load_record(tt_num, saved_record)
            except:
                date_entry.insert(END, get_date())
                output_label.configure(text="Record doesn't exist!", fg="red")
                win.after(5000, clear_output_label)

    except:
        output_label.configure(text="No records exist!", fg="red")
        win.after(5000, clear_output_label)


def load_record(tt_num: str, record: json) -> None:
    reset_fields()

    tt_code.set(tt_num)
    company.set(company_list[company_list.index(record["Company"])])
    sqcc_div.set(sqcc_div_list[sqcc_div_list.index(record["Division"])])
    bank.set(bank_list[bank_list.index(record["Bank"])])
    currency.set(currency_list[currency_list.index(record["Currency"])])
    amount_entry.insert(END, record["Amount"])
    transactee_entry.insert(END, record["Transactee"])
    bankref_entry.insert(END, record["Bank Ref"])
    txn_entry.insert(END, record["Txn No"])
    details_entry.insert(END, record["Details"])
    date_entry.insert(END, record["Date"])
    output_display_text.delete("1.0", END)
    tt_code_entry.focus_set()

    output_label.configure(text="Existing record loaded!", fg="green")
    win.after(5000, clear_output_label)


def on_search() -> None:
    ttc = company.get() + tt_code.get()
    if ttc == "":
        field_blank_msg()
        win.after(5000, clear_output_label)
    else:
        search_record(ttc, tt_code.get())


if __name__ == "__main__":

    records_file = os.path.join(os.path.expanduser("~"), "Documents", "TT records.json")

    if not os.path.exists(records_file):
        with open(records_file, "w") as file:
            file.write("{}")

    tt = "TT"

    # Main frame
    main_frame = Frame(win, padx=7, pady=7)
    main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Inputs frame
    inputs_frame = Frame(main_frame, padx=7, pady=7)
    inputs_frame.grid(row=0, column=0)

    # Header
    header_label = Label(
        win,
        text="TT Filename Generator",
        font=("Consolas", 18),
        fg="dark blue",
        padx=10,
        pady=15,
    )
    header_label.place(relx=0.5, anchor=N)

    # Footer
    footer_label = Label(
        win, text="Made by Farhan Arshad\nVersion 1.2.2", fg="grey", padx=7, pady=7
    )
    footer_label.place(relx=1, rely=1, anchor=SE)

    # Company
    company = StringVar()
    company_label = Label(inputs_frame, text="Company: ", pady=7)
    company_label.grid(row=0, column=0, sticky=E)
    company_list = ["", "AR", "SQSS", "SQCC", "BA"]
    company.set(company_list[1])
    company_dropdown = OptionMenu(inputs_frame, company, *company_list)
    company_dropdown.grid(row=0, column=1, sticky=W, pady=3)

    # TT Code
    tt_code = StringVar()
    tt_code_label = Label(inputs_frame, text="TT Code: ")
    tt_code_label.grid(row=1, column=0, sticky=E)
    tt_code_entry = Entry(inputs_frame, textvariable=tt_code, width=50)
    tt_code_entry.grid(row=1, column=1, pady=3)

    # TT record search button
    search_button = Button(inputs_frame, text="Search", command=on_search)
    search_button.grid(row=1, column=2, padx=(3, 7))

    # Division (for SQCC only)
    sqcc_div = StringVar()
    sqcc_div_label = Label(inputs_frame, text="Division (for SQCC only): ")
    sqcc_div_label.grid(row=2, column=0, sticky=E)
    sqcc_div_list = ["", "WH", "FS", "IT", "ST", "TY"]
    sqcc_div.set(sqcc_div_list[0])
    sqcc_div_dropdown = OptionMenu(inputs_frame, sqcc_div, *sqcc_div_list)
    sqcc_div_dropdown.grid(row=2, column=1, sticky=W, pady=3)

    # Bank
    bank = StringVar()
    bank_label = Label(inputs_frame, text="Bank: ")
    bank_label.grid(row=3, column=0, sticky=E)
    bank_list = ["", "NCB", "RB", "ALJ"]
    bank.set(bank_list[1])
    bank_dropdown = OptionMenu(inputs_frame, bank, *bank_list)
    bank_dropdown.grid(row=3, column=1, sticky=W, pady=3)

    # Currency
    currency = StringVar()
    currency_label = Label(inputs_frame, text="Currency: ")
    currency_label.grid(row=4, column=0, sticky=E)
    currency_list = ["", "SR", "USD"]
    currency.set(currency_list[1])
    currency_dropdown = OptionMenu(inputs_frame, currency, *currency_list)
    currency_dropdown.grid(row=4, column=1, sticky=W, pady=3)

    # Amount
    amount = StringVar()
    amount_label = Label(inputs_frame, text="Amount: ")
    amount_label.grid(row=5, column=0, sticky=E)
    amount_entry = Entry(inputs_frame, textvariable=amount, width=50)
    amount_entry.grid(row=5, column=1, pady=3)

    # Transactee
    transactee = StringVar()
    transactee_label = Label(inputs_frame, text="Vendor/Customer: ")
    transactee_label.grid(row=6, column=0, sticky=E)
    transactee_entry = Entry(inputs_frame, textvariable=transactee, width=50)
    transactee_entry.grid(row=6, column=1, pady=3)

    # Bank reference number
    bankref = StringVar()
    bankref_label = Label(inputs_frame, text="Bank ref.: ")
    bankref_label.grid(row=7, column=0, sticky=E)
    bankref_entry = Entry(inputs_frame, textvariable=bankref, width=50)
    bankref_entry.grid(row=7, column=1, pady=3)

    # Txn reference number
    txn = StringVar()
    txn_label = Label(inputs_frame, text="Transaction no.: ")
    txn_label.grid(row=8, column=0, sticky=E)
    txn_entry = Entry(inputs_frame, textvariable=txn, width=50)
    txn_entry.grid(row=8, column=1, pady=3)

    # Txn description
    details = StringVar()
    details_label = Label(inputs_frame, text="Details: ")
    details_label.grid(row=9, column=0, sticky=E)
    details_entry = Entry(inputs_frame, textvariable=details, width=50)
    details_entry.grid(row=9, column=1, pady=3)

    # Date
    date = StringVar()
    date_label = Label(inputs_frame, text="Date (DD-MM-YYYY): ")
    date_label.grid(row=10, column=0, sticky=E)
    date_entry = Entry(inputs_frame, textvariable=date, width=50)
    date_entry.grid(row=10, column=1, pady=3)

    # Execution button
    copy_button = Button(
        inputs_frame, text="Generate and copy to clipboard", command=on_copy
    )
    copy_button.grid(row=11, column=0, pady=10)

    # Result indicator
    output_label = Label(inputs_frame, text="", pady=10)
    output_label.grid(row=11, column=1)

    # Reset button
    reset_button = Button(inputs_frame, text="Reset fields", command=on_reset)
    reset_button.grid(row=12, column=1, pady=5)

    # Reset indicator
    reset_label = Label(inputs_frame, text="", pady=5)
    reset_label.grid(row=12, column=0)

    # Output display
    output_display_label = Label(main_frame, text="File name: ")
    output_display_label.grid(row=1, column=0, sticky=W, padx=42)
    output_display_text = Text(main_frame, height=3, width=50)
    output_display_text.grid(row=2, column=0)

    # Cursor focus
    tt_code_entry.focus_set()
    date_entry.insert(END, get_date())

    win.mainloop()
