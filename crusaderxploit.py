fuck = '''
   _____                               _             
  / ____|                             | |            
 | |      _ __  _   _  ___   __ _   __| |  ___  _ __ 
 | |     | '__|| | | |/ __| / _` | / _` | / _ \| '__|
 | |____ | |   | |_| |\__ \| (_| || (_| ||  __/| |   
 _\_____||_|    \__,_||___/ \__,_| \__,_| \___||_|   
 \ \ / /       | |       (_)| |                      
  \ V /  _ __  | |  ___   _ | |_                     
   > <  | '_ \ | | / _ \ | || __|                    
  / . \ | |_) || || (_) || || |_    Version 0.1                 
 /_/ \_\| .__/ |_| \___/ |_| \__|     bluesendpie             
        | |                                          
        |_|

=FUCK THE SYSTEM EVERYWHERE EVERYTIME=                                           

'''
print(fuck.title())

import kivy
import os
import sys
import alive_progress
import time

kivy.require("1.9.1")


from kivy.app import App
from alive_progress import alive_bar



from kivy.uix.button import Button

ip = input('Masukan IP = ')
port = int(input('Masukan Port [Default 8080] = '))


class ButtonApp(App):
    
    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text ="FUCK SYSTEMS BUTTON",
                font_size ="14sp",
                background_color =(1, 1, 1, 1),
                color =(1, 1, 1, 1),
                size =(20, 20),
                size_hint =(.2, .2),
                pos =(300, 250))


        btn.bind(on_press = self.callback)
        return btn


    def callback(self, event):
     for x in 5470, 100, 100, 100, 100, 100, 100, 100, 100:
      with alive_bar(x) as bar:
        for i in range(x):
            time.sleep(.001)
            bar()
            os.system("fullmoon.py")



root = ButtonApp()


root.run()