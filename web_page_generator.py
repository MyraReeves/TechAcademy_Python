import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Page Generator")
        self.defaultButton = Button(self.master, text="Generate default HTML page", width=30, height=2, command=self.defaultHTMLPage)
        self.defaultButton.grid(padx=(10, 10) , pady=(10, 10))

    def defaultHTMLPage(self):
        pageText = "Stay tuned for our amazing summer sale!"
        pageFile = open("index.html", "w")
        pageContent = "<html> \n<body> \n<h1>" + pageText + "</h1> \n</body> \n</html>"

        pageFile.write(pageContent)
        pageFile.close()
        webbrowser.open_new_tab("index.html")










if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()