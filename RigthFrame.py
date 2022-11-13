import customtkinter as ctk
from PIL import Image

class RightFrame(ctk.CTkFrame):
    def __init__(self, name:str="FrameDefault", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = ctk.CTkLabel(self, text= f" I am a rigth frame {name}")
        self.label.grid(row=0, column = 1)
