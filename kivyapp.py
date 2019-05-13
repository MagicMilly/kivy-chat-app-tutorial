import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
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

        print(f"Attempting to join {ip}:{port} as {username}")

        # save information 
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip}, {port}, {username}")

class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    EpicApp().run()