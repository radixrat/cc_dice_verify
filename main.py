import argparse
import time

from controller.controller import Controller

def start(args):
    try:
        if args.display == "SH1106":
            from displays.SH1106 import SH1106
            from displays.SH1106 import config
            display = SH1106.SH1106()
        controller = Controller(display)
        while True:
            event = controller.wait_for_event()
            controller.process_event(event)
    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--display", default="SH1106", help="display being used")
    args = parser.parse_args()
    start(args)