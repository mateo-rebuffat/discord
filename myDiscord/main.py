import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from StartupPage import StartupPage
from LoginPage import LoginPage
from CreateAccountPage import CreateAccountPage
from MainGUI import MainGUI
import os
from dotenv import load_dotenv

ctk.set_appearance_mode("light")

load_dotenv(dotenv_path="pass.env")

# Assurez-vous que les variables d'environnement sont correctement chargées
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")

# Connexion à la base de données MySQL
db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
    database=DB_DATABASE
)

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Disclord')

        self.container = ctk.CTkFrame(self, width=400, height=500)
        self.container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.frames = {}
        for F in (StartupPage, LoginPage, CreateAccountPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self, db_connection=db_connection)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("StartupPage")

    def show_frame(self, page_name):
        if page_name == "MainGUI" and page_name not in self.frames:
            F = MainGUI
            frame = F(parent=self.container, controller=self, db_connection=db_connection)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)
        else:
            frame = self.frames[page_name]
        frame.tkraise()

        if page_name == "MainGUI":
            self.geometry('1000x600')
            self.container.configure(width=1000, height=600)
        else:
            self.geometry('600x600')
            self.container.configure(width=400, height=500)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()