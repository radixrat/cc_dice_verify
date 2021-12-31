from menus.main_menu import MainMenu
from menus.rolls_menu import RollsMenu
from interfaces.waveshare_hat_interface import WaveShareInterface

class Controller:
    def __init__(self, display):
        self.display = display
        self.active_menu = MainMenu(self.display)
        self.active_menu.render()
        self.interface = WaveShareInterface()

    def render_screen(self):
        self.active_menu.render()

    def process_event(self, event):
        #TODO: improve
        if "RELEASED" in event:
            new_view = self.active_menu.process_event(event)
            if new_view:
                self.switch_views(new_view)
            self.render_screen()

    def wait_for_event(self):
        while True:
            event = self.interface.check_events()
            if event:
                self.process_event(event)

    def switch_views(self, view_event):
        if view_event == "MAIN_VIEW":
            self.active_menu = MainMenu(self.display)
        elif view_event == "ROLLS_VIEW":
            self.active_menu = RollsMenu(self.display)
        elif view_event == "ABOUT_VIEW":
            self.active_menu = AboutMenu(self.display)

                    