from flask import Flask, request, jsonify, send_from_directory

import google.generativeai as genai
import os

app = Flask(__name__, static_folder='../client', static_url_path='')

# Configura tu clave de API de Google
os.environ["GOOGLE_API_KEY"] = "AIzaSyBoNkJgJSotLS-Ma1qeQNID0p3qv-zM8pI"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Función del chatbot
def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Ruta para servir el archivo index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Ruta para servir otros archivos estáticos
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    user_message = data.get('message')
    bot_response = chat_with_gemini(user_message)
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    app.run(debug=True)
