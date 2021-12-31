import RPi.GPIO as GPIO
from .interface import Interface

#GPIO define
RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

class WaveShareInterface(Interface):
    def __init__(self):
        self.setup_gpio()
        self.active_pin = None
        super().__init__()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
        GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
        GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
        GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
        GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
        GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
        GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
    
    def check_events(self):
        available_pins = [KEY_UP_PIN,KEY_DOWN_PIN, KEY_LEFT_PIN, KEY_RIGHT_PIN, KEY_PRESS_PIN,
            KEY1_PIN, KEY2_PIN, KEY3_PIN]
        for pin in available_pins:
            if not GPIO.input(pin):
                self.active_pin = pin
                return self.pin_action_to_event(pin, "pressed")
            if pin == self.active_pin:
                self.active_pin = None
                return self.pin_action_to_event(pin, "released")
        return None

    def pin_action_to_event(self, pin, event):
        if pin == KEY_UP_PIN:
            pfx = "HAT_UP_"
        elif pin == KEY_RIGHT_PIN:
            pfx = "HAT_RIGHT_"
        elif pin == KEY_DOWN_PIN:
            pfx = "HAT_DOWN_"
        elif pin == KEY_LEFT_PIN:
            pfx = "HAT_LEFT_"
        elif pin == KEY_PRESS_PIN:
            pfx = "HAT_CENTER_"
        elif pin == KEY1_PIN:
            pfx = "KEY1_"
        elif pin == KEY2_PIN:
            pfx = "KEY2_"
        elif pin == KEY3_PIN:
            pfx = "KEY3_"
        
        return pfx + event.upper()
        

    def list_possible_events(self):
        return ["HAT_UP_PRESSED", "HAT_UP_RELEASED", "HAT_RIGHT_PRESSED", "HAT_RIGHT_RELEASED", "HAT_DOWN_PRESSED", 
        "HAT_DOWN_RELEASED", "HAT_LEFT_PRESSED", "HAT_LEFT_RELEASED", "HAT_CENTER_PRESSED", "HAT_CENTER_RELEASED", 
        "KEY1_PRESSED", "KEY1_RELEASED", "KEY2_PRESSED","KEY2_RELEASED", "KEY3_PRESSED", "KEY3_RELEASED"]