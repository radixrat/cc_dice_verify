from PIL import Image,ImageDraw,ImageFont
from .menu import Menu

class MainMenu(Menu):
    def __init__(self, display):
        super().__init__(display)
        self.active_index = 0
        self.menu_list = ['Verify Rolls', 'About']
        self.font = ImageFont.truetype('resources/fonts/RobotoCondensed-Light.ttf', 12)
        

    def get_active_menu_selection(self):
        return self.active_index

    def set_active_menu_selection(self, active_index):
        self.active_index = active_index

    def draw_screen(self):
        self.draw_menu_list()
    
    def draw_menu_list(self):
        left_padding = 2
        height_offset = 16
        active_index = self.get_active_menu_selection()
        for idx, item in enumerate(self.menu_list):
            if active_index == idx:
                self.canvas.rectangle(((0,idx*height_offset),(128,idx*height_offset+height_offset)),fill=0)
            self.canvas.text((left_padding,idx*height_offset),item,font=self.font,fill=int(active_index == idx))

    def process_event(self, event):
        if event == "HAT_UP_RELEASED":
            self.active_index -= 1
            if self.active_index <= 0:
                self.active_index = 0
        elif event == "HAT_DOWN_RELEASED":
            self.active_index += 1
            if self.active_index >= len(self.menu_list):
                self.active_index = len(self.menu_list)-1
        elif event == "HAT_CENTER_RELEASED":
            if self.active_index == 0:
                print("Requesting Rolls View")
                return "ROLLS_VIEW"
            elif self.active_index == 1:
                print("Requesting About View")
                return "ABOUT_VIEW"