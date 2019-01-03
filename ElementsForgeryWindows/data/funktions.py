from tkinter import *;

class sysFunktions():
    def __init__(self, AppClass):
        self.mainApp = AppClass;

    def pro_size(self, widget, mode, pro):
        if mode == "w" or mode == "width" or mode == 0:
            beginnumber = widget.winfo_screenwidth();
        elif mode == "h" or mode == "height" or mode == 1:
            beginnumber = widget.winfo_screenheight();
        return (beginnumber / 100) * pro;

    def ch_fontsize(self, font_size):
        return (('MS', 'Sans', 'Serif'), font_size);

    def ch_fullscreen(self, *args):
        self.fullscreen_state = not self.fullscreen_state;
        self.mainApp.root.attributes("-fullscreen", self.fullscreen_state);

    def ExitGame(self, *args):
        self.mainApp.root.quit();

class gameFunktions():
    def __init__(self, AppClass):
        self.mainApp = AppClass;