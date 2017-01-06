from Tkinter import *
from num2words import num2words as n2w
from ui import RadioList, VerticalScrolledFrame

class App(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        # self.geometry('400x300')
        self.grid()
        self.label = Label(self, text="hello world")
        self.label.grid()
        container = Frame(self)
        container.grid(row=1, columnspan=3)
        vframe = VerticalScrolledFrame(container)
        # vframe.pack(fill=BOTH);
        # vframe.pack()
        # vframe.pack(side=LEFT, anchor=W)
        vframe.grid()
        rbl = RadioList(vframe.interior, bg="white")
        for x in range(100, 150):
            i = x + 1
            t = n2w(i)
            rbl.add(t, i)
        rbl.grid(columnspan=3)

root = Tk()
app = App(root)
root.resizable(width=False, height=False)
root.geometry('550x300')
root.title('My App')
root.mainloop()
