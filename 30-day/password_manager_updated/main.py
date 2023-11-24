import tkinter as tk
import tkinter.messagebox
import random
import pyperclip
import json

FILE_NAME = "data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    pass_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pass_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pass_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password = pass_symbols + pass_letters + pass_numbers

    random.shuffle(password)
    ans = ''.join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ans)
    pyperclip.copy(ans)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def writeToJson(new_data):
    with open(FILE_NAME, mode="w") as data_file:
        json.dump(new_data, data_file, indent=4)


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    if not website:
        tk.messagebox.showerror(title="Error", message="Empty Website Field!")
        website_entry.focus()
    elif not email:
        tk.messagebox.showerror(title="Error", message="Empty Email Field!")
        email_entry.focus()
    elif not password:
        tk.messagebox.showerror(title="Error", message="Empty Password Field!")
        password_entry.focus()
    else:
        is_ok = tk.messagebox.askokcancel(title=website,
                                          message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword:{password} \nIs it ok to save?")
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }
            try:
                with open(FILE_NAME, mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                writeToJson(new_data)
            else:
                data.update(new_data)
                writeToJson(data)

            website_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            tk.messagebox.showinfo(title="Success!", message="Entry has been saved!")
        website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()

    if not website:
        tk.messagebox.showerror(title="Error", message="Empty Website Field!")
        website_entry.focus()
    else:
        try:
            with open(FILE_NAME, mode="r") as data_file:
                data = json.load(data_file)
                email = data[website]["email"]
                password = data[website]["password"]
                tk.messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")

        except FileNotFoundError:
            tk.messagebox.showerror(title="Error", message="No Data File Found")
        except KeyError:
            tk.messagebox.showerror(title="Error", message="No Details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200, highlightthickness=0)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky=tk.EW)
website_entry.focus()

# Search
search_button = tk.Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2, sticky=tk.EW)

# Email/Username
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.EW)

# Password
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky=tk.EW)

generate_password_button = tk.Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=tk.EW)

# Add
add_button = tk.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.EW)

window.mainloop()
