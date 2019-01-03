from tkinter import *
from data import funktions;
import ctypes
import os
from PIL import ImageTk, Image

class App():
    def __init__(self):
        self.root = Tk();
        self.root.configure(background="DarkBlue");
        self.sysfuncs = funktions.sysFunktions(self);
        self.gamefuncs = funktions.gameFunktions(self);
        self.sysfuncs.fullscreen_state = True;
        self.root.attributes("-fullscreen", self.sysfuncs.fullscreen_state);
        self.root.title("ElementsForgery Windows Offline");
        self.root.geometry(str(ctypes.windll.user32.GetSystemMetrics(0))+"x"+str(ctypes.windll.user32.GetSystemMetrics(1)));
        self.root.bind("<F4>", self.sysfuncs.ch_fullscreen);
        self.root.bind("<Escape>", self.sysfuncs.ExitGame);
        bg_canvas = Canvas(self.root);
        bg_canvas.place(x=0,y=0, width=self.sysfuncs.pro_size(self.root, "w", 100), height=self.sysfuncs.pro_size(self.root, "h", 100))
        bg_canvas.create_image(0,0, image=PhotoImage(file="content\\img\\background.gif"));
        self.content_frame = Canvas(bg_canvas, bg="Black", bd=0, highlightthickness=0, width=self.sysfuncs.pro_size(self.root, "w", 90), height=self.sysfuncs.pro_size(self.root, "h", 90));
        self.content_frame.place(x=self.sysfuncs.pro_size(self.root, "w", 5), y=self.sysfuncs.pro_size(self.root, "h", 5));
        self.root.after(1, self.game_choose);
        self.root.mainloop();

    def game_choose(self):
        try:
            gamefiles = os.listdir(os.environ["USERPROFILE"]+"\\Documents\\ElementForgery\\gamefile\\");
        except FileNotFoundError:
            os.mkdir(os.environ["USERPROFILE"]+"\\Documents\\ElementForgery");
            os.mkdir(os.environ["USERPROFILE"]+"\\Documents\\ElementForgery\\gamefile");
            gamefiles = [];

        def newgame():
            Label(content_canvas, text="Choose a name for the GameSave", bg="Black", fg="White").grid(row=0, column=0);
            gamesave_name = Entry(content_canvas);
            gamesave_name.grid(row=1, column=0);
            Button(content_canvas, text="Create", font=self.sysfuncs.ch_fontsize(16), fg="Green", bg="Black", bd=5, highlightcolor="Green", highlightbackground="Green").grid(row=1, column=1);

        MainMenuCanvas = Canvas(self.content_frame, bg="Black", bd=0, highlightthickness=0);
        MainMenuCanvas.place(x=self.sysfuncs.pro_size(self.content_frame, "w", 10), y=self.sysfuncs.pro_size(self.content_frame, "h", 10))
        content_canvas = Canvas(self.content_frame, bg="Black", bd=0, highlightthickness=0);
        content_canvas.place(x=self.sysfuncs.pro_size(self.content_frame, "w", 10), y=self.sysfuncs.pro_size(self.content_frame, "h", 25));
        Button(MainMenuCanvas, text="New Game", command=newgame, font=self.sysfuncs.ch_fontsize(16), fg="Green", bg="Black", bd=5, highlightcolor="Green", highlightbackground="Green").grid(padx=10, column=0, row=0);
        Button(MainMenuCanvas, text="Load", font=self.sysfuncs.ch_fontsize(16), fg="Green", bg="Black", bd=5, highlightcolor="Green", highlightbackground="Green").grid(padx=10, column=1, row=0);
MainClass = App();