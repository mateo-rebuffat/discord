import tkinter as tk
from PIL import Image, ImageTk

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Affichage d'une image")

# Charger l'image avec PIL
image = Image.open("image.jpeg")

# Convertir l'image PIL en un format compatible avec tkinter
photo = ImageTk.PhotoImage(image)

# Créer un widget Label pour afficher l'image
label = tk.Label(root, image=photo)
label.pack()

# Exécuter la boucle principale tkinter
root.mainloop()
