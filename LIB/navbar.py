import tkinter as tk
from tkinter import ttk
import os


class NavBar():
    NAV_BUTTONS = ["Home", "Tests", "Gradebook", "Students", "Questions"]
    def __init__(self, window, parent):
        self.window = window
        self.parent = parent
        self.holdingFrame = ttk.Frame(self.parent)
        self.holdingFrame.grid(row=0, column=0, columnspan=len(NavBar.NAV_BUTTONS), padx=5, pady=5, sticky=tk.NW)
        self.c = 0
        for b in range(0, len(NavBar.NAV_BUTTONS)):
            navButton = ttk.Button(self.holdingFrame, text=NavBar.NAV_BUTTONS[b],
                                   command=lambda x=b: self.window.show_frame(x))
            navButton.grid(row=0, column=self.c, padx=5, pady=5)
            self.c += 1
        self.logOutButton = ttk.Button(self.holdingFrame, text="Log Out", command=self.logOut)
        self.logOutButton.grid(row = 0, column=self.c, pady=5, padx=5, sticky=tk.NW)

    def logOut(self):
        self.window.show_frame(7)


if __name__ == "__main__":
    pass
