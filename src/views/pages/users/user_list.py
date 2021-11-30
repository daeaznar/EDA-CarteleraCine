from tkinter import *
from tkinter.ttk import Separator
import datetime

from models.users import *
import views.pages.users.user_form as UserForm

class UserListView:
    def __init__(self, master):
        self.userModel = UsersModel()
        self.master = master

        # create Users main container
        self.frameUsers = Frame(self.master, bg='#ffffff')
        self.frameUsers.pack(fill='both', expand=1, side='top', anchor='w', padx=0, pady=10)

        # create Title container
        self.frameTitle = Frame(self.frameUsers, bg='#ffffff')
        self.frameTitle.pack(fill='x', side='top', anchor='w', padx=0, pady=10)

        # create Title 
        title = Label(self.frameTitle, text='Usuarios', font=('arial', 20,'normal'), bg='#ffffff', fg='#4267b2')
        title.pack(padx=0, pady=10, side='left', anchor='n')

        # create button add user
        frameCreate= Frame(self.frameTitle, bg='#ffffff', highlightthickness=2, highlightbackground='#11285b', highlightcolor='#11285b')
        frameCreate.pack(padx=25, pady=10, side='right', anchor='n')
        buttonCreate = Button(frameCreate, font=('arial', 12,'normal'), text='+ Agregar usuario', bg='#ffffff', relief='flat', activebackground='#ffffff', fg='#11285b', command=lambda: self.createUser())
        buttonCreate.pack()

        # create scrollable container
        frameBody = Frame(self.frameUsers, bg='#ffffff')
        frameBody.pack(fill='both', expand=1, padx=7, pady=7)

        self.containerTopLevel = Canvas(frameBody, bd=0, highlightthickness=0, relief='ridge', bg='#ffffff')
        self.containerTopLevel.pack(side='left', fill='both', expand=1, padx=7, pady=7)
        
        yScrollbar = Scrollbar(frameBody, orient='vertical', command=self.containerTopLevel.yview)
        yScrollbar.pack(side='right', fill='y')

        self.containerTopLevel.configure(yscrollcommand=yScrollbar.set)
        self.containerTopLevel.bind('<Configure>', lambda e: self.containerTopLevel.configure(scrollregion=self.containerTopLevel.bbox('all')))

        self.frameTopLevel = Frame(self.containerTopLevel, bg='#ffffff')
        self.frameTopLevel.bind('<Configure>', lambda e: self.containerTopLevel.configure(scrollregion=self.containerTopLevel.bbox('all')))

        self.containerTopLevel.create_window((0,0), window=self.frameTopLevel, anchor='nw')
        
        self.containerTopLevel.bind_all("<MouseWheel>", self.onMosueWheel)

        # create Table main container
        self.frameTable = Frame(self.frameTopLevel, bg='#ffffff')
        self.frameTable.pack(fill='x', side='top', anchor='w', padx=0, pady=20)

        self.getUsers()

    def onMosueWheel(self, event):
        self.containerTopLevel.yview_scroll(-1 * (event.delta // 120), "units")
    
    def getUsers(self):
        result = self.userModel.getAll()

        self.frameTable.pack_forget()

        # create Table main container
        self.frameTable = Frame(self.frameTopLevel, bg='#ffffff')
        self.frameTable.pack(fill='x', side='top', anchor='w', padx=0, pady=10)

        # create Table header
        Label(self.frameTable, text='ID', font=('arial', 12,'bold'), bg='#ffffff', fg='#4267b2', justify=CENTER, width=10).grid(row=0, column=0, padx=0, pady=0)
        Label(self.frameTable, text='Nombre de usuario', font=('arial', 12,'bold'), bg='#ffffff', fg='#4267b2', justify=CENTER, width=30).grid(row=0, column=1, padx=0, pady=0)
        Label(self.frameTable, text='Estatus', font=('arial', 12,'bold'), bg='#ffffff', fg='#4267b2', justify=CENTER, width=10).grid(row=0, column=2, padx=0, pady=0)
        Label(self.frameTable, text='Fecha de creación', font=('arial', 12,'bold'), bg='#ffffff', fg='#4267b2', justify=CENTER, width=30).grid(row=0, column=3, padx=0, pady=0)
        Label(self.frameTable, text='Actions', font=('arial', 12,'bold'), bg='#ffffff', fg='#4267b2', justify=CENTER, width=20).grid(row=0, column=4, padx=0, pady=0)
        Separator(self.frameTable, orient='horizontal').grid(row=1, column=0, columnspan=5, pady=5, sticky="ew")

        for i, row in enumerate(result):
            self.drawRows(i, row)


    def drawRows(self, index, row: User):
        indexRow = (((index + 1) * 2) + 1)
        indexSeparator = (((index + 1) * 2) + 2)

        Label(self.frameTable, text=row.user_id, font=('arial', 12,'normal'), bg='#ffffff', fg='#444444', justify=CENTER, width=10).grid(row=indexRow, column=0, padx=0, pady=0)
        Label(self.frameTable, text=row.user_name, font=('arial', 12,'normal'), bg='#ffffff', fg='#444444', justify=CENTER, width=30).grid(row=indexRow, column=1, padx=0, pady=0)
        Label(self.frameTable, text=('Activo' if row.is_active else 'Inactivo'), font=('arial', 12,'normal'), bg='#ffffff', fg=('green' if row.is_active else 'red'), justify=CENTER, width=10).grid(row=indexRow, column=2, padx=0, pady=0)
        Label(self.frameTable, text=datetime.datetime.strptime(row.create_at, '%Y-%m-%d %H:%M:%S'), font=('arial', 12,'normal'), bg='#ffffff', fg='#444444', justify=CENTER, width=30).grid(row=indexRow, column=3, padx=0, pady=0)
        frameActions = Frame(self.frameTable, bg='#ffffff')
        frameActions.grid(row=indexRow, column=4, padx=0, pady=0, sticky='ew')
        Separator(self.frameTable, orient='horizontal').grid(row=indexSeparator, column=0, columnspan=5, pady=5, sticky='ew')


        frameEdit = Frame(frameActions, bg='#ffffff', highlightthickness=2, highlightbackground='green', highlightcolor='green')
        frameEdit.pack(padx=5, pady=5, side='left', anchor='n')
        buttonEdit = Button(frameEdit, font=('arial', 12,'normal'), text='Editar', bg='#ffffff', relief='flat', activebackground='#ffffff', fg='green', command=lambda: self.editUser(row))
        buttonEdit.pack()

        frameDelete = Frame(frameActions, bg='#ffffff', highlightthickness=2, highlightbackground='red', highlightcolor='red')
        frameDelete.pack(padx=5, pady=5, side='left', anchor='n')
        buttonDelete = Button(frameDelete, font=('arial', 12,'normal'), text='Eliminar', bg='#ffffff', relief='flat', activebackground='#ffffff', fg='red', command=lambda: self.deleteUser(row))
        buttonDelete.pack()
        
    def createUser(self):
        self.frameUsers.pack_forget()
        UserForm.UserFormView(self.master, None)

    def editUser(self, user: User):
        self.frameUsers.pack_forget()
        UserForm.UserFormView(self.master, user)
        
    def deleteUser(self, user: User):
        result = self.userModel.delete(user.user_id)

        if (result):
            self.getUsers()
