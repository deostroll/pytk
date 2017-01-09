from Tkinter import *
from VerticalScrollBar import VerticalScrolledFrame as VSF
import sys
from functools import partial

class RadioList(Frame):

    def __init__(self, parent, **kw):

        keys = kw.keys()

        if 'f' in keys:
            frameOpts = kw['f']
        else:
            frameOpts = {}

        if 'r' in keys:
            self.rbOpts = kw['r']
        else:
            self.rbOpts = {}

        Frame.__init__(self, parent, **frameOpts)

        vsf = VSF(self, name="vsf")
        self.vsf = vsf
        self.frame = vsf.interior
        vsf.pack(fill=BOTH, expand=YES)

        def noop(*args):
            pass

        self.cb = noop

        keys = kw.keys()

        if 'command' in keys:
            self.cb = kw['command']

        self._var = IntVar()
        self.ctrls = []


    def add(self, text, value):

        rbOpts = self.rbOpts
        # vsb = self.vsf.vscrollbar

        opts = {}
        opts.update(rbOpts)
        opts['text'] = text
        opts['anchor'] = W
        opts['value'] = value
        opts['variable'] = self._var
        opts['command'] = self._rb_clicked

        rb = Radiobutton(self.frame, **opts)
        fn = partial(self._rb_clicked, rb)
        rb.config(command=fn)
        rb.select()
        rb.pack(fill=X)

        self.after(100, self._set_scroll)
        # self._set_scroll()


    def _rb_clicked(self, *args):
        self.cb(*args)

    def _set_scroll(self):
        # print 'scrolling...'
        vsb = self.vsf.vscrollbar
        canvas = self.vsf.canvas

        current = vsb.get()
        delta = current[1] - current[0]
        # print delta
        if delta < 1:
            vsb.set(1-delta, 1)
            canvas.yview('scroll', 1000, 'units')
