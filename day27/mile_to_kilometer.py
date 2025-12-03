from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometr_result_label.config(text=f"{km}")



window = Tk()
window.title("Mile to kilometr Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column = 1, row = 0)


miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equale_label = Label(text="is equal to")
is_equale_label.grid(column=0, row = 1)

kilometr_result_label = Label(text="0")
kilometr_result_label.grid(column=1, row=1)

kilometr_label = Label(text= "Km")
kilometr_label.grid(column = 2, row = 1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column = 1, row = 2)






window.mainloop()