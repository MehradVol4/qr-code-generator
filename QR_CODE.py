import tkinter as tk
import pyqrcode
from PIL import ImageTk, Image
import os

def generate():
    link_name = name_entry.get().strip()
    link = link_entry.get().strip()

    if not link_name or not link:
        show_message("Please enter both a name and a link", "red")
        return

    file_name = link_name + ".png"

    try:
        url = pyqrcode.create(link)
        url.png(file_name, scale=8)

        img = Image.open(file_name)
        img = ImageTk.PhotoImage(img)

        if hasattr(generate, "image_label"):
            generate.image_label.configure(image=img)
            generate.image_label.image = img
        else:
            generate.image_label = tk.Label(root, image=img)
            generate.image_label.image = img
            canvas.create_window(200, 450, window=generate.image_label)
    except Exception as e:
        show_message(f"Error: {e}", "red")

def show_message(text, color):
    msg_label = tk.Label(root, text=text, fg=color)
    canvas.create_window(200, 500, window=msg_label)

root = tk.Tk()
root.title("QR Code Generator")
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack()

tk.Label(root, text='QR Code Generator', fg='red', font=('Arial', 18, 'bold')).place(x=100, y=10)

tk.Label(root, text='Short link name').place(x=50, y=60)
name_entry = tk.Entry(root)
name_entry.place(x=200, y=60)

tk.Label(root, text='Full link').place(x=50, y=100)
link_entry = tk.Entry(root)
link_entry.place(x=200, y=100)

tk.Button(root, text='Generate', command=generate).place(x=170, y=140)

root.mainloop()
