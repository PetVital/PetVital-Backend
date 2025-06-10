import google.generativeai as genai
import json
from petvital_app.utils import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def enviar_mensaje(mensaje_usuario):
    print("Iniciando Conversación...")

    prompt = ""

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    json_response = response.text.strip()
    
    if json_response.startswith('```json'):
        json_response = json_response.replace('```json', '').replace('```', '').strip()
    
    try:
        json_data = json.loads(json_response, strict=False)
        return json_data
    except json.JSONDecodeError:
        print("Error al decodificar JSON:", json_response)
        return {"respuesta": "Lo siento, no pude entender la respuesta. Intenta formular tu pregunta de otra forma."}