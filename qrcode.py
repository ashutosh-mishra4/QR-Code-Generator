from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image

root = Tk()

# function to generate the QR code


def generate():
    name = name_entry.get()
    link = link_entry.get()
    file_name = name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 400, window=image_label)


canvas = Canvas(root, height=600, width=400)
canvas.pack()

app_label = Label(root, text="QR Code Generator",
                  fg="blue", font=("Poppins", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# input for link name and link
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# button to generate the QR code
button = Button(text="Generate QR", command=generate)
canvas.create_window(200, 230, window=button)


root.mainloop()
