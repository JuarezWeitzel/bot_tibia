from tkinter.ttk import Label, Button, Combobox, Style
from tkinter import messagebox
from ttkthemes import ThemedTk
from size_window import center_window
from PIL import Image, ImageTk
import pyautogui
import keyboard
import json

from window import hidden_client

root = ThemedTk(theme='black', themebg=True)
root.title("MyInterface")
root.resizable(False, False)
style = Style()
style.configure('TButton', font=("Roboto", 12))
style.configure('Ativado.TButton', foreground="green")
style.configure('Desativado.TButton', foreground="red")

# Definir as dimensões desejadas da janela
width = 290
height = 220

# Centralizar a janela na tela
center_window(root, width, height)

HOTKEYS = ["Desligado", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"] 

def generete_widget(widget, row, column, padx=5, pady=5, sticky="NSEW", columnspan=None, **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return my_widget

def load_trash():
    load_image = Image.open('trash-icon.jpg')
    resized_image = load_image.resize((20,20))
    return ImageTk.PhotoImage(resized_image)

lbl_food = generete_widget(Label, row=0, column=0, text="HotKey Eat Food", sticky="W", font=("Roboto", 12))

lbl_cast = generete_widget(Label, row=1, column=0, text="HotKey Cast", sticky="W", font=("Roboto", 12))
cbx_cast = generete_widget(Combobox, row=1, column=1, padx=30, pady=10, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=8)
cbx_cast.current(0)

rgb = ""
mana_position = ""

def get_mana_position():
    global rgb
    global mana_position
    messagebox.showinfo(title="Mana Position", message="Posicione o mouse em cima da barra de mana e pressione a tecla insert.")
    keyboard.wait('insert')
    x, y = pyautogui.position()
    rgb = pyautogui.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Mana Result', message=f"X: {x} Y: {y} - RGB: {rgb}")
    lbl_mana_position.configure(text=f"({x}, {y})")
    mana_position = [x, y]
     
btn_mana_position = generete_widget(Button, row=2, column=0, sticky="NSEW", text="Mana Potion", command=get_mana_position)
lbl_mana_position = generete_widget(Label, row=2, column=1, text="Empty", font=("Roboto", 12), sticky="W")

trash = load_trash()

def clear():
    lbl_mana_position.configure(text="Empty")

btn_mana_position_trash = generete_widget(Button, row=2, column=1, image=(trash), sticky="E", command=clear)

cbx_food = generete_widget(Combobox, row=0, column=1, padx=30, pady=10, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=8)
cbx_food.current(0)

def opacity():
    result = hidden_client()
    if result == 1:
        btn_opacity.configure(style="Ativado.TButton")
        return
    btn_opacity.configure(style="Desativado.TButton")

btn_opacity = generete_widget(Button, row=3, column=0, text="Apply Opacity", columnspan=2, command=opacity)

def save():
    my_data = {
        "food": {
           "value": cbx_food.get(),
           "position": cbx_food.current()
        },
        "spell": {
           "value": cbx_cast.get(),
           "position": cbx_cast.current()
        },
        "mana_pos": {
            "position": mana_position,
            "rgb": rgb
        }
    }
    with open("infos.json", "w") as file:
        file.write(json.dumps(my_data))

btn_start = generete_widget(Button, row=4, column=0, text="START", command=save)

def load():
    with open("infos.json", "r") as file:
        data = json.loads(file.read())

btn_load = generete_widget(Button, row=4, column=1, text="LOAD", command=load)

root.mainloop()