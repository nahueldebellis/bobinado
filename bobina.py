import serial
import tkinter as tk

ser = serial.Serial("COM3")
input_text = "0"

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", font = "Helvetica 80 bold italic")
        self.label.pack()
        self.root.geometry("500x100") 
        self.read_arduino()
        self.root.mainloop()

    def read_arduino(self):
        read = ser.read()
        read = read.decode('ascii')
        n = ""
        while(read in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):
            n = n + read
            read = ser.read()
            read = read.decode('ascii')
            self.label.configure(text=n)
        self.root.after(1, self.read_arduino)


app=App()
      
