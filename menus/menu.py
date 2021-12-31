from PIL import Image,ImageDraw

class Menu:
    def __init__(self, display):
        self.display = display
        self.canvas = None
        self.init_display()
        self.clear()

    def clear(self):
        self.display.clear()

    def init_display(self):
        self.display.Init()
    
    def render(self):
        #self.clear()
        img = Image.new('1', (self.display.width, self.display.height), "WHITE")
        self.canvas = ImageDraw.Draw(img)
        self.draw_screen()
        self.display.ShowImage(self.display.getbuffer(img))

    def draw_screen(self):
        pass

    def process_event(self, event):
        pass