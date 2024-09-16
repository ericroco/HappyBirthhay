import tkinter as tk
import pygame
from tkinter import messagebox
from PIL import Image, ImageTk


def mostrar_imagen_y_sonido():
 
    pygame.mixer.init()
    pygame.mixer.music.load('D:\Users\StarMedia\Desktop\HappyBirthhay\Sonido\happybirthday.mp3')
    pygame.mixer.music.play()

   
    ventana_imagen = tk.Toplevel(root)
    ventana_imagen.title("Imagen a pantalla completa")

  
    imagen_path = 'D:\Users\StarMedia\Desktop\HappyBirthhay\Imagen\librh.jpg'
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((ventana_imagen.winfo_screenwidth(), ventana_imagen.winfo_screenheight()))
    imagen_tk = ImageTk.PhotoImage(imagen)

  
    label_imagen = tk.Label(ventana_imagen, image=imagen_tk)
    label_imagen.pack(fill=tk.BOTH, expand=True)


    ventana_imagen.mainloop()

root = tk.Tk()
root.title("Ventana Principal")


boton_mostrar = tk.Button(root, text="Mostrar Imagen y Sonido", command=mostrar_imagen_y_sonido)
boton_mostrar.pack(pady=20)


root.mainloop()