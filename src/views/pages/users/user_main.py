from tkinter import * 

import views.pages.users.user_list as UserList

class UserMainView:
    def __init__(self, master):
        self.master = master

        # create Users container
        self.frameContainer = Frame(self.master, bg='#ffffff')
        self.frameContainer.pack(fill='both', expand=1, side='top', anchor='w', padx=10, pady=10)

        UserList.UserListView(self.frameContainer)