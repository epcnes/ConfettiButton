from tkinter import *; from tkinter.ttk import *
import pyautogui;

root = Tk()

st = Style()
st.configure('W.TButton', font=('Comic Sans MS', 20))
Button(root, text = "Confett", style='W.TButton', command=None).pack()

root.mainloop()