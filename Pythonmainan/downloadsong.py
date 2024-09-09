from tkinter import *
import tkinter as tk
from pytube import YouTube

class downloader (tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title = ("Youtube Video Downloader")
        self.root.geometry("944x500+500+200")

        MainFrame = Frame (self.root, bd = 10, width = 810, height = 490, relief = RIDGE)
        MainFrame.grid (row =0, column =0, pady =40)

        TitleFrame = Frame (MainFrame)
        TitleFrame.grid(row =0, column =0, pady =40)

        WidgetFrame = Frame (MainFrame, width = 810, height = 490, relief = RIDGE)
        WidgetFrame.grid(row =0, column =0, pady =20, padx =20)

        self.lblDownloadTitle= Label (TitleFrame, font = ('arial', 30, 'bold'), text = "Youtube Video Downloader",
                                        bd = 7, anchor = 'w')
        self.lblDownloadTitle.grid(row =0, column =0, sticky = W, padx =0)
if __name__ == "__main__":
    root = tk.Tk()
    app = downloader(root)
    root.mainloop()