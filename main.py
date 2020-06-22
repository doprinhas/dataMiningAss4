from tkinter import Tk
from View import View
from ViewController import ViewController

def main():
    """ Runs the application """
    controller = ViewController()
    root = Tk()
    my_gui = View(root, controller)
    root.mainloop()


if __name__ == '__main__':
    main()