def center_window(window, width, height):
    # Obter as dimensões da tela
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular as coordenadas para centralizar a janela
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Definir a geometria da janela
    window.geometry(f"{width}x{height}+{x}+{y}")