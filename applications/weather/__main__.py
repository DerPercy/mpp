import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import lib

#import lib.getLatestFile
#from .lib import getLatestFile
#from .lib import parseFile


class MyApp(App):

    def build(self):
        fParse = lib.getLatestFile()
        jsonFile = open(fParse,"r")
        parsedFile = lib.parseFile(jsonFile)
        jsonFile.close()

        layout = BoxLayout(spacing=10)
        def renderDaily(daily,index):
            if index < 5:
                nonlocal layout
                listLayout = BoxLayout(orientation='vertical')
                btn1 = Label(text=daily.uiDate())
                listLayout.add_widget(btn1)
                labelDescr = Label(text=daily.uiDescription())
                listLayout.add_widget(labelDescr)

                layout.add_widget(listLayout)

        parsedFile.daily().each(renderDaily)
        #btn1 = Button(text='Hello', size_hint=(.7, 1))
        #btn2 = Button(text='World', size_hint=(.3, 1))
        #layout.add_widget(btn1)
        #layout.add_widget(btn2)
        return layout



#fParse = getLatestFile()
#jsonFile = open(fParse,"r")
#parsedFile = parseFile(jsonFile)
#jsonFile.close()


#print(parsedFile.uiTime())
if __name__ == '__main__':
   MyApp().run()
