import tkinter as tk
from tkinter import filedialog
import os

application_window = tk.Tk()
my_filetypes = [('all files', '.*'), ('text files', '.*txt')]

answer = filedialog.askdirectory(parent = application_window,
                                 initialdir = os.getcwd(),
                                 title = "Please select a folder")
amswer = filedialog.askopenfilename(parent = application_window,
                                 initialdir = os.getcwd(),
                                 title = "Please select a file",
                                 filetypes = my_filetypes)
answer = filedialog.askopenfilenames(parent = application_window,
                                     initialdir = os.getcwd(),
                                     title = "Please select one or more files",
                                     filetypes = my_filetypes)
answer = filedialog.asksaveasfilename(parent = application_window,
                                      initialdir = os.getcwd(),
                                      title = "Please select a file name for saving:",
                                      filetypes = my_filetypes)
