# GUI program to create three single line text-box to accept a
# value from the user using tkinter module

import tkinter as tk
parent = tk.Tk()
parent.geometry("400x250")
name = tk.Label(parent, text="Name").place(x=30, y=50)
email = tk.Label(parent, text="User ID").place(x=30, y=90)
password = tk.Label(parent, text="Password").place(x=30, y=130)
sbmitbtn = tk.Button(parent, text="Submit", activebackground="green",
                     activeforeground="blue").place(x=120, y=170)
entry1 = tk.Entry(parent).place(x=85, y=50)
entry2 = tk.Entry(parent).place(x=85, y=90)
entry3 = tk.Entry(parent).place(x=90, y=130)
parent.mainloop()
