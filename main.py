from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.button import Button

import os


from fetcher_query_intf import fetcher_query


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


# class SaveDialog(FloatLayout):
#     save = ObjectProperty(None)
#     text_input = ObjectProperty(None)
#     cancel = ObjectProperty(None)

def auth_error():
    content = Button(text='Close')
    popup = Popup(title="Operation Failed", content=content, auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)

def show_popup():
    content = Button(text='Close')
    popup = Popup(title="Success", content=content, auto_dismiss=False,
                  size_hint=(None, None), size=(300, 200))
    popup.open()

    content.bind(on_press=popup.dismiss)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    target_file_path = 'neo4jintf/docker/features/config/.env'

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        with open(Root.target_file_path, 'w') as stream:
            stream.write(self.text_input.text)
        self.text_input.text = ''
        result = fetcher_query.test_query_insert()
        print("result is {}".format(result))

        if not result:
            auth_error()

        else:
            print(result)
            show_popup()
        # content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        # self._popup = Popup(title="Save file", content=content,
        #                     size_hint=(0.9, 0.9))
        # self._popup.open()

    def load(self, path, filename):
        print("Input file path is {} and name is {}".format(path, filename))
        #Root.target_file_path = filename[0] + '.out'
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        # print("DKKKK file path is {}".format(filename))
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()
