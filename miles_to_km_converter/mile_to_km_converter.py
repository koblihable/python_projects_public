import tkinter as tk
from tkinter import  END



window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

is_equal_label = tk.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=1, row=2)

miles_input = tk.Entry(width=10)
miles_input.grid(column=2, row=1)

miles_label = tk.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=3, row=1)

result = tk.Label(text="0", font=("Arial", 12, "bold"), justify="center")
result.grid(column=2, row=2)

def get_conversion():
    calc = round((float(miles_input.get()) * 1.609),1)
    result.config(text=calc)

button = tk.Button(text="Calculate", command=get_conversion)
button.grid(column=2, row=3)

km_label = tk.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=3, row=2)





window.mainloop()