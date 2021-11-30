from tkinter import * 

class MoviesListView:
    def __init__(self, master):
        self.master = master

        # create Title container
        title = Label(self.master, text='Peliculas', font=('arial', 20,'normal'), bg='#ffffff', fg='#4267b2')
        title.pack(padx=0, pady=10, side='top', anchor='w')

        # create Movies container
        self.frameMovies = Frame(self.master, bg='#4267b2')
        self.frameMovies.pack(fill='x', side='top', anchor='w', padx=0, pady=10)