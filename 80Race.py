from tkinter import *
from random import randint
class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.winfo_toplevel().title("The Race to 80")

        self.PX = 20
        self.PY = 10
        self.WDTH = 800
        self.HGHT = 400

        self.__maincontainer = Frame(master, width=self.WDTH, height=self.HGHT)
        self.__maincontainer.grid(row=0, column=0, sticky="nsew")
        self.__maincontainer.grid_propagate(0)

        

        self.col1ab = Label(self.__maincontainer,text='lorem ipsum')
        self.col1ab.grid(row = 0, column = 0)
        for i in range(5):
            self.standLabel = self.standardAdder('AS'+ str(915 + randint(1,100)) + str(i))
            self.standLabel.grid(row = 5 - i, column = 1)

    def standardAdder(self, StanNumber):
        return Label(self.__maincontainer,text=StanNumber)


if __name__ == "__main__":
    # Executes when the file itself is run, not when imported.
    root = Tk()
    app = Application(root)
    app.mainloop()