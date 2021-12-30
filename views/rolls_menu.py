from PIL import Image,ImageDraw,ImageFont
from .menu import Menu
from rolls.rolls import get_hash_from_rolls, format_wordindex_to_list

class RollsMenu(Menu):
    def __init__(self, display):
        super().__init__(display)
        self.font = ImageFont.truetype('resources/fonts/RobotoCondensed-Light.ttf', 12)
        self.number_rolls = 0
        # default roll_value to 1, this shouldn't be used to generate rolls
        self.roll_value = 1
        self.roll_list = []
        self.hash = ''
        self.mneumonic_list = None
        self.mneumonic_index = 0
        self.process_roll_state()

    def draw_screen(self):
        # roll value border
        self.canvas.line(((0,0),(0,22)), fill=0)
        self.canvas.line(((0,22),(22,22)), fill=0)
        self.canvas.line(((22,0),(22,22)), fill=0)
        self.canvas.line(((0,0),(22,0)), fill=0)

        # roll value with pad in
        self.canvas.text((9, 3),'{}'.format(self.roll_value), font=self.font)

        # num roll count
        self.canvas.text((28,0), 'Number Rolls: {}'.format(self.number_rolls), font=self.font)
        last_roll = self.roll_list[-1] if len(self.roll_list) > 0 else 'none'
        self.canvas.text((28,11), 'Last Roll Value: {}'.format(last_roll), font=self.font)

        # sha value
        if self.hash:
            h = self.hash.hex()
            print("hash: {}".format(h))
            # can't display all on crappy oled screen so chunk it for verification
            h1 = h[:4]
            h2 = h[8:12]
            h3 = h[16:20]
            h4 = h[28:32]
            h5 = h[36:40]
            h6 = h[44:48]
            h7 = h[52:56]
            h8 = h[60:64]
            self.canvas.text((1,26), "{}..{}..{}..{}".format(h1, h2, h3, h4), font=self.font)
            self.canvas.text((1,38), "{}..{}..{}..{}".format(h5, h6, h7, h8), font=self.font)

        # mneumonic values
        if self.mneumonic_list:
            self.canvas.text((1,53), self.mneumonic_list[self.mneumonic_index])
    
    def process_roll_state(self):
        print("process roll state")
        roll_string = ''.join(self.roll_list)
        print("Roll String: {}".format(roll_string))
        self.hash = get_hash_from_rolls(roll_string)
        self.mneumonic_list = mne_list = format_wordindex_to_list(roll_string, self.hash)

    def process_event(self, event):
        if event == "HAT_DOWN_RELEASED":
            self.roll_value += 1
            if self.roll_value > 6:
                self.roll_value = 1
        elif event == "HAT_UP_RELEASED":
            self.roll_value -= 1
            if self.roll_value < 1:
                self.roll_value = 6
        elif event == "HAT_RIGHT_RELEASED":
            self.mneumonic_index += 1
            if self.mneumonic_index >= len(self.mneumonic_list):
                self.mneumonic_index = 0
        elif event == "HAT_LEFT_RELEASED":
            self.mneumonic_index -= 1
            if self.mneumonic_index <= 0:
                self.mneumonic_index = len(self.mneumonic_list)-1
        elif event == "HAT_CENTER_RELEASED" or event == "KEY1_RELEASED":
            self.number_rolls += 1
            self.roll_list.append(str(self.roll_value))
            self.process_roll_state()
            # reset back to 1 as well so people don't try to use it to generate rolls
            self.roll_value = 1
        elif event == "KEY3_RELEASED":
            # exit
            return "MAIN_VIEW"
            
