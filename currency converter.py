#dictionaries used
from tkinter import ttk

#import all the requird elements
from tkinter import *

#to get the responce
import requests

#tkinter window formating
window = Tk()
window.title("Currency Converter")
window.geometry("350x500")
window.config(bg="#542C6F")
window.resizable(height=False,width=False)

#heading of GUI
heading = Label(text="Currency Converter", font=("Times New Roman", 24,"underline"), bg="#542C6F")
heading.place(x=40,y=10)

#currencies use in the program
currencies = ['Australian Dollar (AUD)', 'Chinese Yuan (CNY)', 'Euro (EUR)', 'Japanese Yen (JPY)', 'Pakistani Rupee (PKR)','Pound sterling (GBP)', 'Russian Ruble (RUB)', 'Saudi Riyal (SAR)', 'United Arab Emirates Dirham (''AED)', 'United States Dollar (USD)','Canadian Dollar (CAD)','Afghani(AFN)']

#label 1 from
currency_from = Label(text="Select Currency :", font=("Arial",12, "underline"), bg="#542C6F",fg="#FDF3F3")
currency_from.place(x=50,y=70)

#to store 1st currency
cur1 = StringVar()

#currencies list
curr1 = ttk.Combobox(window, values=currencies, textvariable=cur1)
curr1.place(x=180,y=70)

#label Entry box to enter amount user to convert
amount = Label(text="Enter amount :", font=("Arial", 12, "underline"), bg="#542C6F",fg="#FDF3F3")
amount.place(x=50,y=140)

#Entry box
amount_get = Entry(width=23)
amount_get.place(x=180,y=140)

# dropdown for currency to convert into
convert_to = Label(text=f"Convert curr to :", font=("Arial", 12, "underline"), bg="#542C6F", fg="#FDF3F3")
convert_to.place(x=50,y=110)

#to store 2nd currency
m = StringVar()
convert_into = ttk.Combobox(window, values=currencies, textvariable=m)
convert_into.place(x=180,y=110)
exchange = Label()

#convert button function
def convert():
    global exchange
    # converted currency label
    exchange = Label(font=("Arial", 12, "bold"), bg="#542C6F",fg="#FDF3F3", pady=10)

    try:
        # save amount
        amount = int(amount_get.get())

        # saving the user input of currency to convert from [-4:-1] get last 3 alphabet of currency code
        curr_1 = curr1.get()[-4:-1]

        # saving the currency to convert to
        curr_2 = convert_into.get()[-4:-1]

        #get data fromURL
        URL = "https://openexchangerates.org/api/latest.json?app_id=efcd841a7aad48e195fb39d583a14b45"

        #save responce
        response = requests.get(URL).json()

        # fetch required values from API rates
        c1= response["rates"][curr_1]
        c2= response["rates"][curr_2]

        # display converted currency
        exchange.config(text=f"1 {curr_1} = {round(c2 / c1, 4)} {curr_2}\n\n{amount:,.2f} {curr_1}"
                              f" = {round(c2 / c1 * amount, 2):,.2f} {curr_2}")
        exchange.place(x=80,y=170)
    except:
        pass


# convert currency button
convert_btn = Button(text="Convert", width=12, font=("Arial",12, "bold"), command=convert)
convert_btn.place(x=110,y=260)


# reset button function
def reset():
    # reset all the states
    curr1.delete(0, "end")
    convert_into.delete(0, "end")
    amount_get.delete(0, "end")
    exchange.destroy()


# reset button
reset_button = Button(text="Reset", width=10, font=("Arial", 15, "bold"), command=reset, bg="#FF0000", border=0)
reset_button.place(x=112,y=300)

# tkinter window loop
window.mainloop()