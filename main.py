import tkinter as tk

from Servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion():
    root = tk.Tk()
    servicio = RestauranteServicio()

    def abrir_panel(usuario):
        for widget in root.winfo_children():
            widget.destroy()

        MainView(root, servicio, usuario)

    LoginView(root, servicio, abrir_panel)

    root.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()
