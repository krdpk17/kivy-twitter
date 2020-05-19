from kivy.app import App
print("DKKK")
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from features import fetcher_query
from kivy.uix.popup import Popup
from kivy.uix.button import Button
print("DKKKK2")
fetcher_query.test_query_insert()
print("DKKKK3")

class MyGrid1(Widget):
    cred_file = ObjectProperty(None)
    input_file = ObjectProperty(None)
    resp = None

    def bt(self):
        if self.cred_file.text == "" or self.input_file.text == "":
            print("found empty")
            empty_input()
            self.reset()
        else:
            try:
                fetcher_query.add_new_query()
                print("DKKKK2")
                show_popup()

            except:
                error_popup()
                self.reset()

            MyGrid1.resp = dm.fetch(self.cred_file.text, self.input_file.text)
            if MyGrid1.resp == "error":
                auth_error()
                self.reset()

            else:
                print(MyGrid1.resp)
                self.reset()
                show_popup()

    def reset(self):
        self.cred_file.text = ""
        self.input_file.text = ""


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
    popup = Popup(title="Download Completed", content=content, auto_dismiss=False,
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
