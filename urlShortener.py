import imp
import pyperclip
import pyshorteners

from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")
url = StringVar()
url_addr = StringVar()

def urlshort():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_addr.set(url_short)

def copyurl():
    url_short = url_addr.get()
    pyperclip.copy(url_short)

Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate short URL", command=urlshort).pack(pady=7)
Entry(root, textvariable=url_addr).pack(pady=5)
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()