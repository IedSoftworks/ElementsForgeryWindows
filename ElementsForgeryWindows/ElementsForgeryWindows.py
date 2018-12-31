from tkinter import *
from data import funktions;
import ctypes

class App():
    def __init__(self):
        self.root = Tk();
        self.functions = funktions.Funktions(self);
        self.functions.fullscreen_state = True;
        self.root.attributes("-fullscreen", self.functions.fullscreen_state);
        self.root.title("ElementsForgery Windows Offline");
        self.root.geometry(str(ctypes.windll.user32.GetSystemMetrics(0))+"x"+str(ctypes.windll.user32.GetSystemMetrics(1)));
        self.root.bind("<F4>", self.functions.ch_fullscreen);
        self.root.bind("<Escape>", self.functions.ExitGame);
        self.root.after(1, self.run);
        self.root.mainloop();

    def run(self):
        print("Working!");
MainClass = App();