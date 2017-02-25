import tkinter
from tkinter.filedialog import askdirectory

class File_dialog2():


    def file(self):
        root = tkinter.Tk()
        root.withdraw()

        with open("path_output.txt", "w") as file:
            filename = askdirectory()
            file.write(filename)


