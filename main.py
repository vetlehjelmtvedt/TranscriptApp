import numpy as np
import kivy
kivy.require('1.0.6') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import tkinter
from tkinter.filedialog import askopenfilename
from file_dialog import File_dialog
from file_dialog2 import File_dialog2
import moviepy.editor as mp
import subprocess
import os
import shutil

with open("path.txt", "r") as file:
    path_dir = file.read()

with open("path_output.txt", "r") as file:
    output_dir = file.read()


string_welcome = "Please choose a file to start transcribing!"











class NameApp(App):

    def build(self):

        f = FloatLayout()


        label_info = Label(text=string_welcome, font_size=20, size_hint=(0.2, .20), pos_hint={'x':.4, 'y':.40})
        lbl_output = Label(text="d", font_size=20, size_hint=(0.2, .20), pos_hint={'x': .4, 'y': .45})


        def file_browse(instance):
            a = File_dialog()
            a.file()

            with open("path.txt", "r") as file:
                string = file.read()
                label_info.text = "File chosen:  " + string



        def file_output(instance):
            a = File_dialog2()
            a.file()

            with open("path_output.txt", "r") as file:
                string = file.read()
                label_info = "Output directory chosen:  " + string

                lbl_output = Label(text=label_info, font_size=20, size_hint=(0.2, .20), pos_hint={'x': .4, 'y': .45})



        def start_transcribe(instance):
            subprocess.call("py -3.5 convert_transcribe.py")
            label_info.font_size = 0
            lbl_output.font_size = 0




        b_browse = Button(text="Choose file...", size_hint=(0.2, .20), pos_hint={'x':.07, 'y':.70})
        b_path = Button(text="Choose output directory...", size_hint=(0.2, .20), pos_hint={'x': .7, 'y': .70})
        b_transcribe = Button(text="Transcribe now!", size_hint=(0.2, .20), pos_hint={'x': .4, 'y': .20})

        b_browse.bind(on_press=file_browse)
        b_path.bind(on_press=file_output)

        b_transcribe.bind(on_press=start_transcribe)


        f.add_widget(b_browse)
        f.add_widget(label_info)
        f.add_widget(b_path)
        f.add_widget(b_transcribe)



        return f


NameApp().run()
