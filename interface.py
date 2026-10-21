from tkinter import * 
import requests
import json


obj = Tk() 
obj.title("Whether Forcasting App")

city = StringVar()

def info():
    name = city.get()
    url = "http://api.weatherapi.com/v1/current.json?key=638ba7c08aa4460794393515231104&q="+name
    req = requests.get(url) 
    data = json.loads(req.content)
    lv41.config(text=data["current"]["temp_c"])
    lv51.config(text=data["current"]["temp_f"])
  


img = PhotoImage(file="C:/Users/Admin/OneDrive/Desktop/Whether_Forcasting App/whether_logo.png")

lv2 = Label(obj, image=img)
lv2.pack()

lv1 = Label(obj , text="WHETTHER FORCASTING APP", fg ='red' , bg = "blue" , font=("calibri",24))
lv1.place(x=500,y=160)

lv3 = Entry(obj,fg ='red'  , font=("calibri",24),textvariable=city)
lv3.place(x=530,y=220)

b11 = Button(obj, text="Submit",fg ='red' , bg = "blue" , font=("calibri",14),command=info)
b11.place(x=650,y=280)

lv4 = Label(obj, text="Temperture in celcius = ",fg ='red' , bg = "blue" , font=("calibri",10))
lv4.place(x=500,y=350)

lv41 = Label(obj, text="info",fg ='red' , bg = "blue" , font=("calibri",10))
lv41.place(x=800,y=350)


lv5 = Label(obj, text="Temperture in Ferenehite = ",fg ='red' , bg = "blue" , font=("calibri",10))
lv5.place(x=500,y=400)

lv51 = Label(obj, text="info ",fg ='red' , bg = "blue" , font=("calibri",10))
lv51.place(x=800,y=400)

obj.mainloop()