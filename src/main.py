from tkinter import * 

from views.home import HomeView

rootUi = Tk()
app = HomeView(rootUi, None)
rootUi.mainloop()