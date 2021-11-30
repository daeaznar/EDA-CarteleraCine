from tkinter import * 

import views.pages.billboard.billboard_list as BillboardView

class BillboardMainView:
    def __init__(self, master):
        self.master = master

        # create Users container
        self.frameContainer = Frame(self.master, bg='#ffffff')
        self.frameContainer.pack(fill='x', side='top', anchor='w', padx=10, pady=10)

        BillboardView.BillboardListView(self.frameContainer)