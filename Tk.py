
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from tkinter import *
import tkinter as tk
datos =[]

# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/XicYac/firebase_python/clave/clave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://haiko1-bd.firebaseio.com//'
})

ref = db.reference("Usuarios")

    


def createNewWindow():
    
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "Digite el nombre de la nueva cuenta: ", bg = 'aqua')
    labelExample = tk.Label(newWindow, text = "Digite la contraseña de la nueva cuenta: ", bg = 'aqua')
    buttonExample = tk.Button(newWindow, text = "su información es correcta", bg = 'aqua')
    labelExample.pack()
    buttonExample.pack()
    

    
def createWindow():    
    newWindow = tk.Toplevel(app2)

    
    labelExample = tk.Label(newWindow, text = "Digite la contraseña del usuario")
    labelExample = tk.Label(newWindow, text = "Digite el nombre de usuario")
    buttonExample = tk.Button(newWindow, text = "Su informacion es correcta")

    labelExample.pack()
    buttonExample.pack()
    

app = tk.Tk()
buttonExample = tk.Button(app,text="Desea crear una cuenta", command=createNewWindow,  bg = 'aqua')
buttonExample.pack()
app2 = tk.Tk()
buttonExample = tk.Button(app,text="Desea ingresar una cuenta", command=createWindow,  bg = 'aqua')
buttonExample.pack()

app.mainloop()


def entrada(input):
    content = dato.get()
    dato.delete(0, END)#borro la información del entry
    


        
cont = db.reference('Usuarios/David').get()

    






ventana.mainloop()














    



    
    
