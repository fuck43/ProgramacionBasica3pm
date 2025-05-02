import tkinter as tk
import requests
import re
from docling import FieldedString

def validar_nombre(nombre):
    patron = r'^[a-zA-Z\-]+$'
    return bool(re.match(patron, nombre))

def estructurar_datos_docling(nombre, tipos, habilidades):
    texto = f"name={nombre} type={','.join(tipos)} ability={','.join(habilidades)}"
    return FieldedString(texto)

def obtener_datos_pokemon(nombre_pokemon):
    if not validar_nombre(nombre_pokemon):
        return "Nombre inválido. Usa solo letras y guiones."
    
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos["name"]
        tipos = [t["type"]["name"] for t in datos["types"]]
        habilidades = [h["ability"]["name"] for h in datos["abilities"]]
        
        fs = estructurar_datos_docling(nombre, tipos, habilidades)
        return f"{fs.fields['name']}\nTipos: {fs.fields['type']}\nHabilidades: {fs.fields['ability']}"
    else:
        return f"No se encontró información para: {nombre_pokemon}"

# --- Interfaz gráfica ---
def mostrar_info():
    nombre = entrada.get().strip()
    info = obtener_datos_pokemon(nombre)
    resultado.config(text=info)

ventana = tk.Tk()
ventana.title("Consulta Pokémon")

tk.Label(ventana, text="Nombre del Pokémon:").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Buscar", command=mostrar_info).pack(pady=5)
resultado = tk.Label(ventana, text="", justify="left")
resultado.pack(pady=10)

ventana.mainloop()
