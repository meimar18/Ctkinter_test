import customtkinter
from CTkMenuSideBar import CTkMenuSideBar
from RigthFrame import RightFrame
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        menu_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MMM\\Git\\Ctkinter_test\\resources\\icons\\gallery-tiles-view-outline-icon.png").resize((30,30), Image.Resampling.LANCZOS))
        self.frame_left = CTkMenuSideBar(menu_image=menu_image, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nwse",padx=2,  pady=2)
        self.frame_right_main = customtkinter.CTkFrame(master=self)

        self.frame_right1 = customtkinter.CTkFrame(master=self)
        self.frame_right2 = customtkinter.CTkFrame(master=self)
        self.frame_right_main = self.frame_right1
        self.frame_right_main.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        settings_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MMM\\Git\\Ctkinter_test\\resources\\icons\\data-management-icon.png").resize((30,30), Image.Resampling.LANCZOS))

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Invoke Button 1",
                                                image= settings_image, 
                                                compound= "left",
                                                #fg_color = self.frame_left.fg_color, 
                                                command= lambda: self.repaintRightFrame(self.frame_right1),
                                                width= 28,
                                                corner_radius= 0)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Invoke Button 2",
                                                image= settings_image, 
                                                compound= "left",
                                                #fg_color = self.frame_left.fg_color, 
                                                command= lambda: self.repaintRightFrame(self.frame_right2),
                                                width= 28,
                                                corner_radius= 0)

        self.button_a = customtkinter.CTkButton(master=self.frame_right1,
                                                text="I am a flat button",
                                                command= self.button_event,
                                                corner_radius=0
                                                )
        self.button_b = customtkinter.CTkButton(master=self.frame_right2,
                                                text="I am a rounded button",
                                                command= self.button_event
                                                )


        self.frame_left.addItem(self.button_1)
        self.frame_left.addItem(self.button_2)
        self.button_a.grid(row=0, column=3)
        self.button_b.grid(row=2, column=2)
    
    def on_closing(self, event=0):
        self.destroy()
    def button_event(self):
        print("Button pressed")
    def repaintRightFrame(self, new_frame:customtkinter.CTkFrame):
        self.frame_right_main.grid_forget()
        self.frame_right_main = new_frame
        self.frame_right_main.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
