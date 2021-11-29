import mask_password
import sqlite3
import pandas as pd

conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()


# User Class
class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return f'User Name: {self.user_name}\n'
