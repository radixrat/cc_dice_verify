# TODO: process this per detected display
from displays.SH1106 import SH1106
from displays.SH1106 import config

import time
from controller.controller import Controller

def main():
    try:
        display = SH1106.SH1106()
        controller = Controller(display)
        while True:
            event = controller.wait_for_event()
            controller.process_event(event)
            time.sleep(10)
    except IOError as e:
        print(e)
    except KeyboardInterrupt:    
        print("ctrl + c:")
        config.module_exit()
        exit()

main()