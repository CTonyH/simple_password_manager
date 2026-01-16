from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    try:
        with open("data.txt", "a") as data:
            data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            clear_entrys()
    except FileNotFoundError:
        with open("data.txt", "w") as data:
            data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            clear_entrys()

def clear_entrys():
    website_entry.delete(0, "end")
    password_entry.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2,weight=0)

canvas = Canvas(width=200, height=200)
password_image =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:",)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entrys
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "tony.hirschligau@googlemail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(column=2, row=3, sticky="w")

add_pw_button = Button(text="Add", width=36, command=save)
add_pw_button.grid(column=1, row=4, columnspan=2, sticky="ew")



window.mainloop()