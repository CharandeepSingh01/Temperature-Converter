#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from PIL import ImageTk, Image
from functools import partial
import sqlite3

#SETTING CELSIUS AS DEFAULT VALUE
tempVal = "Celsius"


#DROPDOWN LIST VALUE
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp


#CONVERSION OF THE TEMPERATURE WITH ADDING DATA TO DATABASE MAIN PART
def call_convert(relabel1, relabe12, inputn):
    conn=sqlite3.connect('database4.db')
    cd=conn.cursor()
    tem = inputn.get()
    if tempVal == 'Celsius':
        f = float((float(tem) * 9 / 5) + 32)
        k = float((float(tem) + 273.15))
        cd.execute("INSERT INTO records(Celsius, Fahrenheit, Kelvin) VALUES (?, ?, ?)",(tem, f, k))
        conn.commit()        
        relabel1.config(text="%f Fahrenheit" % f)
        relabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Fahrenheit':
        c = float((float(tem) - 32) * 5 / 9)
        k = c + 273
        cd.execute("INSERT INTO records(Celsius, Fahrenheit, Kelvin) VALUES (?, ?, ?)",(c, tem, k))
        conn.commit()
        relabel1.config(text="%f Celsius" % c)
        relabe12.config(text="%f Kelvin" % k)
    if tempVal == 'Kelvin':
        c = float((float(tem) - 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        cd.execute("INSERT INTO records(Celsius, Fahrenheit, Kelvin) VALUES (?, ?, ?)",(c, f, tem))
        conn.commit()
        relabel1.config(text="%f Celsius" % c)
        relabe12.config(text="%f Fahrenheit" % f)
    return


#UI AND APP WINDOW CONFIGURATION
root = tk.Tk()
root.geometry('600x300')
root.title('TEMPERATURE CONVERTER')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
img=Image.open("C:\\Users\\CHARANDEEP\\Desktop\\images1.jpg")
test=ImageTk.PhotoImage(img)
label1=tk.Label(image=test)
label1.image=test
label1.place(x=0,y=0,width=600,height=300)
numberInput = tk.StringVar()
var = tk.StringVar()


#CREATING DATABASE AND TABLE FOR SAVING RECORDS
def create():
    conn=sqlite3.connect('database4.db')
    cd=conn.cursor()
    cd.execute("CREATE TABLE IF NOT EXISTS records(Celsius INTEGER, Fahrenheit INTEGER, Kelvin INTEGER)")
    conn.commit()
    conn.close()
create()

#LABEL NAME AND VALUE ENTRY
input_label = tk.Label(root, text="Enter temperature--->", background='#00FF00', foreground="#000000")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)

#RESULT APPEARANCE
result_label1 = tk.Label(root, background='#000000', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#0000FF', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)

#DROPDOWM MENU SETUP
dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='#FFA500', foreground="#FFFFFF")
dropdown["menu"].config(background='#FFFF00', foreground="#000000")

#CONVERT BUTTON WITH UPLOADING DATA IN DATABASE
call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)

root.mainloop()


# In[ ]:




