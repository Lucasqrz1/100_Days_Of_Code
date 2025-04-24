from tkinter import *
from unittest.mock import right

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label=Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=3)
email_entry.insert(0, "example@email.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button= Button(text="Generate Password",width=20, command=generate_password)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=51, command=save)
add_button.grid(row=4, column=1, columnspan=3)
search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(row=1, column=3)


window.mainloop()
