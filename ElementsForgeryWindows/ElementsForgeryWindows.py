from tkinter import *

class App():
    def __init__(self):
        self.root = Tk();
        self.root.title("ElementsForgery Windows Offline");
        self.root.after(1, self.run);
        self.root.mainloop();

    def run(self):
        print("Working!");

MainClass = App();