import sys
import os
from tkinter import *

window=Tk()

window.title("Tracking Bird Migration")
window.geometry('450x250')
window.config(bg = 'black')

def run():
    exec(open('BirdMigrationLatLong.py').read())

def run1():
    exec(open('BirdMigration2DSpeed.py').read())

def run2():
    os.system('BirdMigrationDateTime.py')

def run3():
    os.system('BirdMigrationDailyMeanSpeed.py')

def run4():
    exec(open('BirdMigrationMapView.py').read())

def close(): 
    window.destroy()

l = Label(window, text = "--Tracking Bird Migration--") 
l.config(font =("Courier", 14)) 
l.pack()


b = Button(window,text = "1. Latitude and Longitude", command = run)  
b.pack(padx=10, pady=5)

b = Button(window,text = "2. 2D Speed Vs Frequency", command = run1)  
b.pack(padx=10, pady=5)

b = Button(window,text = "3. Time and Date", command = run2)  
b.pack(padx=10, pady=5)

b = Button(window,text = "4. Daily Mean Speed", command = run3)  
b.pack(padx=10, pady=5)

b = Button(window,text = "5. Cartographic View", command = run4)  
b.pack(padx=10, pady=5)

b = Button(window,text = "6. Exit", command = close)  
b.pack(padx=10, pady=5)



window.mainloop()
