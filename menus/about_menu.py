from PIL import Image,ImageDraw,ImageFont
from .menu import Menu

class AboutMenu(Menu):
    def __init__(self, display):
        super().__init__(display)
        self.font = ImageFont.truetype('resources/fonts/RobotoCondensed-Light.ttf', 12)

    def draw_screen(self):
        self.canvas.text((0,0),"-Dice Verify Instructions-",font=self.font,fill=0)
        self.canvas.text((0,14),"up/down: dice +/-",font=self.font,fill=0)
        self.canvas.text((0,26),"click/key1: add dice value",font=self.font,fill=0)
        self.canvas.text((0,38),"left/right: scroll words",font=self.font,fill=0)
        self.canvas.text((0,50),"@radixrat",font=self.font,fill=0)
    
    def process_event(self, event):
        if event == "KEY3_RELEASED":
            return "MAIN_VIEW"