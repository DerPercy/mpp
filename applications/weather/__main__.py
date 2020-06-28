import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

import lib.getLatestFile
#from .lib import getLatestFile
#from .lib import parseFile


class MyApp(App):

    def build(self):
        return Label(text='Hello world')



fParse = getLatestFile()
jsonFile = open(fParse,"r")
parsedFile = parseFile(jsonFile)
jsonFile.close()


print(parsedFile.uiTime())
#if __name__ == '__main__':
#   MyApp().run()

