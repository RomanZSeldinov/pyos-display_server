import tkinter
 
def maindisplay(title):
    window = tkinter.Tk()
 
    window.attributes('-fullscreen', True)
    window.title(title)

    return window
