import tkinter as tk
from tkinter import ttk

#
class Tab_pages_application(tk.Tk):

    def __init__(self, title, size, value_page, action_page, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(title)
        self.geometry(size)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        nb = ttk.Notebook(self)
        t2 = value_page(nb)
        t1 = action_page(variable_to_check=t2.entry_value, master=nb)
        t2.entry_value.set(2)

        nb.add(t1, text='Tab 1')
        nb.add(t2, text='Tab 2')
        nb.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        nb.columnconfigure(0, weight=1)
        nb.rowconfigure(0, weight=1)

if __name__ == '__main__':
    root = Tab_pages_application('Tab-Tester', '300x200', Tab2.Entry_page, Tab1.Button_page)
    root.mainloop()