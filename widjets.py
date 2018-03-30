import tkinter as interface

class Root():
    root = interface.Tk()
    root.geometry( '800x600+150+150' )

class Forms():
    form = interface.Frame(Root.root)
    form['bg'] = 'white'
    form['padx'] = 0


    nav = interface.Frame(Root.root)
    nav['bg'] = 'white'
    nav['highlightbackground'] = 'yellow'
    nav['padx'] = 30
    nav['pady'] = 30

    def __init__(self,form):
        self.form = form


class ThemedForm(interface.Frame):
    def __init__(self, parent = None, **configs):
        interface.Frame.__init__(self, parent, **configs)
        self.pack()
        self.config(bg = 'yellow', padx = 30, pady = 30)

class ThemedButton(interface.Button):
    def __init__(self, parent = None, **configs):
        interface.Button.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='black', bg = 'white',width = 12, font='courier 12', relief='solid', bd=3)

class ThemedMessage(interface.Message):
    def __init__(self, parent = None, **configs):
        interface.Message.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='black', bg = 'white', font = 'times 16', relief='solid', justify = 'center', width = 70)

class ThemedLabel(interface.Label):
    def __init__(self, parent = None, **configs):
        interface.Label.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='black', bg = 'white', font = 'times 30', relief='solid', justify = 'center', bd=3)
