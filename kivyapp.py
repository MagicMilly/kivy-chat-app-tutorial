import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
import os 

kivy.require("1.10.1")

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # check to see if file exists already
        # will automatically fill past inputs if exists
        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]

        else:
            prev_ip = ""
            prev_port = ""
            prev_username = ""

        # first row
        self.add_widget(Label(text="IP:"))
        # box for user input 
        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)

        # second row
        self.add_widget(Label(text="Port:"))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        self.join = Button(text="Join")
        # get the button to do something! Calls join_button method
        self.join.bind(on_press=self.join_button)
        # moves join button over to the right side
        self.add_widget(Label())
        self.add_widget(self.join)

    # escape from init method
    def join_button(self, instance):
        # grab things from user input in other text boxes (at the time of the button press)
        port = self.port.text 
        ip = self.ip.text
        username = self.username.text 

        # save information 
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip},{port},{username}")

        # debug
        print("Well we got this far")

        info = f"Attempting to join {ip}:{port} as {username}"
        chat_app.info_page.update_info(info)

        print("Is anything happening here?")

        # this changes the screen
        chat_app.screen_manager.current = "Info"

        print("What about here?")

class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        # dynamic message - you can put these in a different file (.kv) if you get into a massive app
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        # will take up 90% of page width because that just looks nicer
        self.message.text_size = (self.message.width * 0.9, None)

class EpicApp(App):
    def build(self):
        # ConnectPage is okay for one screen
        # return ConnectPage()
        # now we work with multiple screens! yay!
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        # new type of screen
        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    # name instance variable to reference easily
    chat_app = EpicApp()
    chat_app.run()