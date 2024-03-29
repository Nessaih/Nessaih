#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.ttk import Button



global_themes = {
    'dark': {
        'button': {
            "activebackground": "#00B2EE",
            "activeforeground": "#E0EEEE",
            "bg": "#008B8B",
            "fg": "#FFFFFF"
        },
        'label': {
            "bg": "#292929",
            "fg": "#E0EEEE"
        },
        'frame':{
            "bg": "#292929"
        },
        'labelframe': {
            "bg": "#292929",
            "fg": "#1E90FF"
        },
        'listbox': {
            "bg": "#292929",
            "fg": "#1E90FF",
            "selectbackground": "#00B2EE"
        },
        'text': {
            "bg": "#292929",
            "fg": "#1E90FF"
        },
        'checkbutton': {
            "bg": "#292929",
            "fg": "#FFFFFF",
            "activebackground": "#292929",
            "activeforeground": "#FFFFFF",
            "selectcolor": "#292929"
        },
        'entry': {
            "bg": "#292929",
            "fg": "#E0EEEE",
            "insertbackground": "red"
        },
        'radiobutton' : {
            "bg": "#292929",
            "fg": "#FFFFFF",
            "activebackground": "#292929",
            "activeforeground": "#FFFFFF",
            "selectcolor": "#292929"
        }
    }
}

default_theme = "dark"

class PyButton(tk.Button):
    '''
    Button
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Button.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['button']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value


class PyLabel(tk.Label):
    '''
    Label
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Label.__init__(self, master, self.temp)
    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['label']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value
            
class PyFrame(tk.Frame):
    '''
    Frame
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Frame.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['frame']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value


class PyLabelFrame(tk.LabelFrame):
    '''
    LabelFrame
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.LabelFrame.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['labelframe']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value

class PyListbox(tk.Listbox):
    '''
    Listbox
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Listbox.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['listbox']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value
            

class PyText(tk.Text):
    '''
    Text
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Text.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['text']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value


class PyCheckbutton(tk.Checkbutton):
    '''
    Checkbutton
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Checkbutton.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['checkbutton']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value
            

class PyEntry(tk.Entry):
    '''
    Entry
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Entry.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['entry']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value      

class PyRadiobutton(tk.Radiobutton):
    '''
    Radiobutton
    '''
    def __init__(self, master, theme=default_theme, **kw):
        self.theme = theme
        self.kw = kw
        self.temp = dict()
        self.choose_theme()
        tk.Radiobutton.__init__(self, master, self.temp)

    def choose_theme(self):
        theme_dict  = global_themes[self.theme]['radiobutton']
        for key,value in theme_dict.items():
            self.temp[key] = value
        for key,value in self.kw.items():
            self.temp[key] = value

if __name__ == '__main__':
    #! /usr/bin/env python
    # -*- coding: utf-8 -*-

    import PyTkinter as pytk
    import tkinter as tk

    root = tk.Tk()
    root.configure(bg="#292929")
    pytk.PyButton(root, text="1234", font=("Monaco", 12)).pack()
    pytk.PyLabel(root, text="123", font=("Monaco", 15)).pack()
    pytk.PyCheckbutton(root, text="123", font=("Monaco", 15)).pack()
    pytk.PyEntry(root, font=("Monaco", 15)).pack()
    pytk.PyText(root, font=("Monaco", 15), height=2, width=20).pack()
    listbox_0 = pytk.PyListbox(root, height=2, font=("Monaco", 15))
    listbox_0.pack()
    for i in range(2):
        listbox_0.insert("end", i)
    radio_intvar = tk.IntVar()
    pytk.PyRadiobutton(root, text="001", variable=radio_intvar, value=0, font=("Monaco", 15)).pack()
    pytk.PyRadiobutton(root, text="002", variable=radio_intvar, value=1, font=("Monaco", 15)).pack()
    radio_intvar.set(1)

    root.mainloop()
