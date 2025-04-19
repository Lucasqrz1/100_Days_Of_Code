from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100,y=100)
my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    return

button = Button(text="Click me",command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry

input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=2, row=2)

# Challenge
button_2 = Button(text="New Button",command=button_clicked)

button_2.grid(column=3, row=0)

window.mainloop()