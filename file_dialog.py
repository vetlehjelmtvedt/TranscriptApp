import tkinter
from tkinter.filedialog import askopenfilename

class File_dialog():


    def file(self):
        root = tkinter.Tk()
        root.withdraw()

        with open("path.txt", "w") as file:
            filename = askopenfilename()
            file.write(filename)


