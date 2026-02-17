from tkinter import *
from tkinter.messagebox import *
import pyautogui
from tkinter.filedialog import *
W, H = pyautogui.size()
screen = Tk()
screen.title("Messages")
screen.geometry(f"{W}x{H}")
screen.resizable(True, True)
screen.attributes("-toolwindow", True)
screen.configure(bg="lightblue", border = "10", borderwidth = 5, relief = "sunken")
def open_file():
    file = askopenfile(mode = "r", filetypes=[("pythonfiles", "*.py"), ("allfiles", "*.*")])
    if file != None:
        print(file.read())
    else:
        print("File not selected")

def save_file():
    files = [("allfiles", "*.*"), ("pythonfiles", "*.py"), ("textfiles", "*.txt")]
    f = asksaveasfile(filetypes = files, defaultextension=files)
    print(f)

def display_messages():
    showinfo("Information", "This is an information message.")
    showwarning("Warning", "This is a warning message.")
    showerror("Error", "This is an error message.")
    showinfo("Question", "What is your favourite cheese?", icon = "question")
    a = askyesno("Python", "Do you like python?")
    print(a)
    b = askokcancel("Cancelling", "Do you want to continue? ")
    print(b)
    c = askretrycancel("Retry", "Do you want to do this again?")
    print(c)
    d = askyesnocancel("YesNO", "Do you like games? ")
    print(d)

save_file()
open_file()


Button(screen, text="Show Info", font=("Arial", 14), bg="blue", fg = "white", command = display_messages).pack(pady=20, padx=20)



screen.mainloop()