from tkinter.ttk import Label, Button, Combobox, Style
from ttkthemes import ThemedTk
from size_window import center_window
from PIL import Image, ImageTk

root = ThemedTk(theme='arc', themebg=True)
root.title("MyInterface")
root.resizable(False, False)
style = Style()
style.configure('TButton', font=("Roboto", 12))

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

btn_mana_position = generete_widget(Button, row=2, column=0, sticky="NSEW", text="Mana Potion")
lbl_mana_position = generete_widget(Label, row=2, column=1, text="Empty", font=("Roboto", 12), sticky="W")

trash = load_trash()
btn_mana_position_trash = generete_widget(Button, row=2, column=1, image=(trash), sticky="E")

cbx_food = generete_widget(Combobox, row=0, column=1, padx=30, pady=10, values=HOTKEYS, state="readonly", font=("Roboto", 12), width=8)
cbx_food.current(0)

btn_opacity = generete_widget(Button, row=3, column=0, text="Apply Opacity", columnspan=2)

btn_start = generete_widget(Button, row=4, column=0, text="START")

btn_load = generete_widget(Button, row=4, column=1, text="LOAD")

root.mainloop()