from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flashy")
window.config(padx=200, pady=200, bg=BACKGROUND_COLOR)

# Card canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right, highlightthickness=0)
right_button.grid(row=1, column=1)

#Labels
# website_label=Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label=Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label=Label(text="Password:")
# password_label.grid(row=3, column=0)

#Entries
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=60)
# email_entry.grid(row=2, column=1, columnspan=3)
# email_entry.insert(0, "example@email.com")
# password_entry = Entry(width=35)
# password_entry.grid(row=3, column=1)

#Buttons
# generate_password_button= Button(text="Generate Password",width=20, command=generate_password)
# generate_password_button.grid(row=3, column=3)
# add_button = Button(text="Add", width=51, command=save)
# add_button.grid(row=4, column=1, columnspan=3)
# search_button = Button(text="Search", width=20, command=find_password)
# search_button.grid(row=1, column=3)


window.mainloop()
