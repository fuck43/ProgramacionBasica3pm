import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json
import requests
from transcriber import Transcriber
from llm import LLM
from tts import TTS

# Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')

app = Flask(__name__)

# --- Nueva función para obtener datos de Pokémon ---
def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        nombre = datos["name"].capitalize()
        tipos = [t["type"]["name"] for t in datos["types"]]
        habilidades = [h["ability"]["name"] for h in datos["abilities"]]
        return f"{nombre} es un Pokémon de tipo {', '.join(tipos)} y tiene las habilidades: {', '.join(habilidades)}"
    else:
        return f"No se encontró información para {nombre_pokemon}."

@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    audio = request.files.get("audio")
    texto = Transcriber().transcribe(audio)

    llm = LLM()
    function_name, args, message = llm.process_functions(texto)

    if function_name == "get_pokemon_info":
        nombre_pokemon = args["nombre"]
        respuesta = obtener_datos_pokemon(nombre_pokemon)
        tts_file = TTS().process(respuesta)
        return {"result": "ok", "text": respuesta, "file": tts_file}
    else:
        respuesta = "No entendí qué Pokémon quieres buscar."
        tts_file = TTS().process(respuesta)
        return {"result": "ok", "text": respuesta, "file": tts_file}