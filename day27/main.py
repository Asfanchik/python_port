from tkinter import *

windows = Tk()
windows.title("My first GUI Program")
windows.minsize(width=500, height=300)


my_label = Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text = "New text")

#Button

def button_cliced():
    print("I got cliced")
    new_text = input.get()
    my_label.config(text=new_text)



button = Button(text="Click me", command=button_cliced)
button.pack()

#Entry



input = Entry(width=10)
input.pack()
print(input.get())




windows.mainloop()