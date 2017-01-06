from Tkinter import *

class RadioList(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.pack()
        self._frame = Frame(self, *args, **kwargs)
        self._frame.pack(fill=BOTH, expand=YES)
        self._var = IntVar()
        # self._var = StringVar('a')

    def add(self, text, value):
        rb = Radiobutton(self._frame,
            text=text,
            value=value,
            variable=self._var,
            anchor=W,
            width=200)
        # rb.grid()
        rb.pack(fill=X)
