import customtkinter as ctk
from PIL import Image

class CTkMenuSideBar(ctk.CTkFrame):
    COMPRESED_WIDTH = 28
    EXTENDED_WIDTH = 120
    def __init__(self, menu_image:Image = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        menuText = '-' if menu_image is None else ''
        #menu_image = ImageTk.PhotoImage(Image.open("C:\\Users\\MMM\\Git\\Ctkinter_test\\resources\\icons\\gallery-tiles-view-outline-icon.png").resize((16,16), Image.ANTIALIAS))
        self.expandMenu = ctk.CTkButton(self, text=menuText, image=menu_image,fg_color= self.fg_color,  command=self._expand, corner_radius= 0, width =self.COMPRESED_WIDTH)
        self.expanded = True
        self.expandMenu.grid(row=0, column=0, sticky= 'w')
        #self.expandMenu.place(relx=0, anchor='w', rely='0.5') # move the text to the left side of frame
        self.__extendedWidth = self.EXTENDED_WIDTH
        self.items = [ctk.CTkButton(width=1,height=1)]
        self.itemsText = []
        self.items.clear()
        self._expand()

    def addItem(self, item:ctk.CTkButton):
        self.items.append(item)
        self.itemsText.append(item.text)
        item.fg_color = self.fg_color
        item.grid(row= len(self.items), column = 0, sticky= 'w')
        if item.winfo_width()>self.__extendedWidth:
            self.__extendedWidth = item.winfo_width()
        if (not self.expanded):
            item.text = ''

    def _expand(self):
        if self.expanded:
            self.expanded = False
            if self.expandMenu.image is None:
                self.expandMenu.set_text('+')
            for item in self.items:
                item.text = ''
                item.set_dimensions(self.COMPRESED_WIDTH)

        else:
            self.expanded = True
            if self.expandMenu.image is None:
                self.expandMenu.set_text('-')
            for i in range(len(self.items)):
                self.items[i].set_dimensions(self.__extendedWidth)
                self.items[i].text= str(self.itemsText[i])
