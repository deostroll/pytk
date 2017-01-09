from ui import RadioList
from Tkinter import *
from num2words import num2words as nw

class App(Frame):
    def __init__(self, parent=None):
        # Frame.__init__(self, parent, bd=2, bg="white")
        Frame.__init__(self, parent)
        root = self.master
        root.geometry('400x300')
        root.title('My radio list')
        root.resizable(width=False, height=False)
        self.pack(fill=BOTH,expand=YES)

        # self.label = Label(self, text="Hello World", anchor=W, bd=2)
        # self.label.pack(fill=X)
        frame = Frame(self, name="btnContainer")
        frame.pack(anchor=W)

        btn = Button(frame, text="Add", command=self.add)
        btn.pack(side=LEFT)

        self.rl = rl = RadioList(self, command=self.changed)
        self.rl.pack(fill=BOTH)

        btn2 = Button(frame, text="Set", command=rl._set_scroll)
        btn2.pack(side=LEFT)

        self.counter = 0

    def add(self):
        count = self.counter
        self.counter = self.counter + 1
        rl = self.rl

        rl.add(nw(count), count)

    def changed(self, *args):
        print args



app = App()
app.mainloop()
