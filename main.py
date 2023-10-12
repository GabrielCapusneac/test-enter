from tkinter import Tk, ttk

root = Tk()
root.title('Test app')

root.geometry('300x300')

framevtm = ttk.Frame(root, padding=10)

framevtm.grid()

label.
mesaj_enter = 'mesaju press enter'
def sendbut(event):
    print(event)
    print(mesaj_enter)


button = ttk.Button(framevtm, text='Enter')

button.bind('<Button-1>', sendbut)

button.grid(column=0, row=2)

root.bind('<Return>', sendbut)

root.mainloop()
