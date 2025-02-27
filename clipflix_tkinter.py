import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-]+'
    return re.match(pattern, email) is not None

def save_to_file():
    first_name = entryfn.get()
    last_name = entryln.get()
    email = entryem.get()
    subscription = combobox.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return

    if first_name and last_name and email and subscription:
        # Check if the email is already registered
        email_registered = False
        if os.path.exists("subscriptions.txt"):
            with open("subscriptions.txt", "r") as file:
                for line in file:
                    if f"Email: {email}" in line:
                        email_registered = True
                        break
        
        # If email is already registered and returning customer checkbox is not checked
        if email_registered and not returning_customer_var.get():
            messagebox.showerror("Error", "Email address already registered.")
            return
        # If email is already registered and returning customer checkbox is checked
        elif email_registered and returning_customer_var.get():
            messagebox.showinfo("Returning Customer", "You're all paid up!")
            return

        # If email is not registered or returning customer checkbox is not checked
        data = f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nSubscription: {subscription}\n\n"

        with open("subscriptions.txt", "a") as file:
            file.write(data)

        messagebox.showinfo("Success", "Data saved successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def check_returning_customer():
    email = entryem.get()
    if email:
        try:
            with open("subscriptions.txt", "r") as file:
                for line in file:
                    if f"Email: {email}" in line:
                        messagebox.showinfo("Returning Customer", f"Email {email} found in the system!")
                        return
                messagebox.showinfo("New Customer", f"Email {email} not found in the system.")
        except FileNotFoundError:
              messagebox.showerror("Error", "File not found. Please save some data first.")
    else:
        messagebox.showerror("Error", "Please enter an email address.")
               
root = tk.Tk()
root.title("Paperclips")
root.geometry("1100x800")

options = ["1 Month, $12", "6 Months, $68", "12 Months, $120"]

def resize_image(image_path, width, height, text=None):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.LANCZOS)
    if text:
        draw = ImageDraw.Draw(img)
        # Use "Lucida Handwriting" font and size
        font_path = "C:/Windows/Fonts/LHANDW.TTF"  # Change to the path of your Lucida Handwriting font file
        font = ImageFont.truetype(font_path, 26)  # Font size 20
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        # Shadow effect by drawing text with slight offset
        shadow_offset = (2, 2)
        shadow_position = ((width - text_width) / 2 + shadow_offset[0], height - text_height - 10 + shadow_offset[1])
        draw.text(shadow_position, text, font=font, fill="black")  # Shadow color
        # Draw the actual text
        text_position = ((width - text_width) / 2, height - text_height - 10)
        draw.text(text_position, text, font=font, fill="green")  # Change text color as needed
    return ImageTk.PhotoImage(img)

# Display Image
img_builtin = resize_image("clipflix_img/bannerSMP.png", 1000, 200)
lbl_builtin = Label(root, image=img_builtin)
lbl_builtin.pack()

# Frame for Company slogan
frame_slogan = tk.Frame(root)
frame_slogan.pack(pady=10)

label_slogan = Label(frame_slogan, text="Welcome to So Many Paperclips. We are happy to be your go to store for all your paperclip needs. And now we want to welcome you to our Streaming Service: CLIPFLIX. To begin your order, please let us take your details", wraplength=600, justify="center")
label_slogan.pack(side=tk.LEFT)

# Frame for images
frame_images = tk.Frame(root)
frame_images.pack()

# Image 1
img_worship = resize_image("clipflix_img/paperclip-worshipHour.png", 200, 200, "Worship Hour")
lbl_worship = Label(frame_images, image=img_worship, width=200, height=200)
lbl_worship.pack(side=tk.LEFT)

# Image 2
img_diy = resize_image("clipflix_img/paperclip-diy.png", 200, 200, "DIY")
lbl_diy = Label(frame_images, image=img_diy, width=200, height=200)
lbl_diy.pack(side=tk.LEFT)

# Image 3
img_hospital = resize_image("clipflix_img/paperclip-hospital.png", 200, 200, "Hospital")
lbl_hospital = Label(frame_images, image=img_hospital, width=200, height=200)
lbl_hospital.pack(side=tk.LEFT)

# Image 4
img_kidsscience = resize_image("clipflix_img/paperclip-kidsscience.png", 200, 200, "Kid Science")
lbl_kidsscience = Label(frame_images, image=img_kidsscience, width=200, height=200)
lbl_kidsscience.pack(side=tk.LEFT)

# Image 5
img_sitcom = resize_image("clipflix_img/paperclip-sitcom.png", 200, 200, "Sitcom")
lbl_sitcom = Label(frame_images, image=img_sitcom, width=200, height=200)
lbl_sitcom.pack(side=tk.LEFT)

# Frame for first and last name entries
frame_name = tk.Frame(root)
frame_name.pack(pady=10)

# First Name
labelfn = tk.Label(frame_name, text="First Name")
labelfn.pack(side=tk.LEFT, padx=5)
entryfn = tk.Entry(frame_name)
entryfn.pack(side=tk.LEFT, padx=5)

# Last Name
label_ln = tk.Label(frame_name, text="Last Name")
label_ln.pack(side=tk.LEFT, padx=5)
entryln = tk.Entry(frame_name)
entryln.pack(side=tk.LEFT, padx=5)

# Frame for email
frame_email = tk.Frame(root)
frame_email.pack(pady=10)

# Email
labelem = tk.Label(frame_email, text="Email")
labelem.pack(side=tk.LEFT, padx=5)
entryem = tk.Entry(frame_email)
entryem.pack(side=tk.LEFT, padx=5)

# Returning Customer Checkbox
returning_customer_var = tk.BooleanVar()
returning_customer_checkbox = tk.Checkbutton(frame_email, text="Returning Customer", variable=returning_customer_var)
returning_customer_checkbox.pack(side=tk.LEFT, padx=5)

# Frame for info 
frame_info = tk.Frame(root)
frame_info.pack(pady=10)

label_info = Label(frame_info, text="CLIPFLIX is available on a subscription basis. You can subscribe month-to-month, or try a six month or yearly subscription. If you are a returning customer from our paperclip department, you can take advantage of a ten percent discount on any subscription.", wraplength=600, justify="center")
label_info.pack(side=tk.LEFT)

# Frame for subscription options
frame_subscriptions = tk.Frame(root)
frame_subscriptions.pack(pady=5)

# Subscription Options
labelcb = tk.Label(frame_subscriptions, text="Subscription")
labelcb.pack(pady=5)
combobox = ttk.Combobox(frame_subscriptions, values=options, state="readonly")
combobox.set("Subscription Options")
combobox.pack(pady=5)

# Frame for submit
frame_submit = tk.Frame(root)
frame_submit.pack(pady=10)

# Submit Button
submit_button = tk.Button(frame_submit, text="Submit", command=save_to_file)
submit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
