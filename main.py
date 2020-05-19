from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
import fetcher_query_intf as fetcher_query
from kivy.uix.popup import Popup
from kivy.uix.button import Button

class MyGrid1(Widget):
    cred_file = ObjectProperty(None)
    resp = None

    def bt(self):
        if self.cred_file.text == "":
            print("found empty")
            empty_input()
            self.reset()
        else:
            print("DKKKK3")
            MyGrid1.resp = fetcher_query.test_query_insert(self.cred_file.text)
            print("DKKKK3_")
            if not MyGrid1.resp:
                auth_error()
                self.reset()

            else:
                print(MyGrid1.resp)
                self.reset()
                show_popup()

    def reset(self):
        self.cred_file.text = ""


class P():
    pass


def auth_error():
    content = Button(text='Close')
    popup = Popup(title="Authentication Failed", content=content, auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)


def show_popup():
    content = Button(text='Close')
    popup = Popup(title="Success", content=content, auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)


def error_popup():
    content = Button(text='Error Reading File')
    popup = Popup(title="Re Try", content=content, auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)


def empty_input():
    content = Button(text='Re-Try')
    popup = Popup(title="Found Missing Path", content=content,
                  auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)


class MyApp(App):
    def build(self):
        return MyGrid1()


if __name__ == '__main__':
    MyApp().run()
