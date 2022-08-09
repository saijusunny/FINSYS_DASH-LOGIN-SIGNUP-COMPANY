import tkinter as tk
from tkinter import ttk

class Button_page(ttk.Frame):
    """This will contain what is going to be shown on the first tab."""

    def __init__(self, variable_to_check, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.variable_to_check = variable_to_check
        self.variable_to_check.trace('w', lambda *args: self.update_background())

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.internal_style = ttk.Style()
        self.internal_style.configure('Tab1.TLabelframe', background='lightgreen')
        self.internal_style.configure('Tab1.TLabelframe.Label', background='lightgreen')

        self.f = ttk.LabelFrame(self, text='f', style='Tab1.TLabelframe')
        self.f.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.f.columnconfigure(0, weight=1)
        self.f.rowconfigure(0, weight=0)

        self.b1 = ttk.Button(self.f, text='B1')
        self.b1.grid(column=0, row=0, sticky=(tk.N,))

    def update_background(self):
        new_value_string = self.variable_to_check.get()
        try:
            new_value = int(new_value_string)
        except (ValueError):
            new_value = 0

        if new_value < 5:
            self.internal_style.configure('Tab1.TLabelframe', background='lightgray')
            self.internal_style.configure('Tab1.TLabelframe.Label', background='lightgray')
            self.b1.config(state=tk.DISABLED)
        else:
            self.internal_style.configure('Tab1.TLabelframe', background='lightgreen')
            self.internal_style.configure('Tab1.TLabelframe.Label', background='lightgreen')
            self.b1.config(state=tk.NORMAL)
           