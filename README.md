# 🍽️ Restaurante App - Semana 15

## 👩‍💻 Autora

**Stefany Gallegos Zari**

## 📌 Descripción

Restaurante App es una aplicación desarrollada en Python para gestionar información básica de un restaurante mediante una interfaz gráfica construida con Tkinter y ttk.

La Semana 15 continúa el proyecto desarrollado anteriormente e incorpora una sección de Ventas, manteniendo una arquitectura modular y una separación clara entre datos, modelos, servicios e interfaz.

## 🎯 Objetivo de la Semana 15

Aplicar los fundamentos básicos del manejo de eventos en Tkinter mediante la relación:

Usuario → componente → command → callback → RestauranteServicio → persistencia → respuesta visual.

La operación implementada permite seleccionar un usuario y un producto, registrar una venta y mostrar inmediatamente el resultado en la interfaz.

## 🛠️ Tecnologías utilizadas

- Python
- Tkinter
- ttk
- JSON
- Programación Orientada a Objetos
- GitHub

## 📂 Estructura del proyecto

```text
Restaurante-app_S15/
│
├── Datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── Modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── Servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   └── logo.svg
│
├── main.py
└── README.md
