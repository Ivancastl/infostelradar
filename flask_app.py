from flask import Flask, render_template, request, send_from_directory
import os
import re
import datetime

app = Flask(__name__)

CARPETA_TXT = os.path.join(os.path.dirname(__file__), 'data')
CARPETA_RESULTADOS = os.path.join(os.path.dirname(__file__), 'resultados')
os.makedirs(CARPETA_RESULTADOS, exist_ok=True)

def formatear_resultado(linea):
    if 'http' in linea:
        if re.search(r'https?://[^/]+/[^:]+:[^:]+:.+', linea):
            url_parts = linea.split(':')
            return f"{url_parts[0]}:{url_parts[1]}:{url_parts[2]}"
        elif re.search(r'https?://[^:]+:[^:]+:.+', linea):
            url_parts = linea.split(':')
            return f"{url_parts[0]}:{url_parts[1]}"
    return None

def buscar_dominio(dominio_buscar):
    resultados = {
        'dominio': dominio_buscar,
        'total': 0,
        'logins': set(),
        'archivo': ''
    }

    if not os.path.exists(CARPETA_TXT):
        return {'error': f"No se encontró la carpeta: {CARPETA_TXT}"}

    for archivo in os.listdir(CARPETA_TXT):
        if archivo.endswith('.txt'):
            try:
                with open(os.path.join(CARPETA_TXT, archivo), 'r', encoding='utf-8', errors='ignore') as f:
                    for linea in f:
                        if dominio_buscar.lower() in linea.lower():
                            formato = formatear_resultado(linea.strip())
                            if formato:
                                resultados['logins'].add(formato)
                                resultados['total'] += 1
            except Exception as e:
                print(f"Error leyendo {archivo}: {e}")

    resultados['logins'] = sorted(resultados['logins'])

    if resultados['logins']:
        filename = f"{dominio_buscar.replace('.', '_')}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        ruta_archivo = os.path.join(CARPETA_RESULTADOS, filename)
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            for login in resultados['logins']:
                f.write(login + '\n')
        resultados['archivo'] = filename

    return resultados

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dominio = request.form.get('dominio', '').strip()
        if dominio:
            datos = buscar_dominio(dominio)
            return render_template('resultados.html', 
                                datos=datos,
                                hora_actual=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return render_template('index.html', 
                         fecha_actual=datetime.datetime.now().strftime('%Y-%m-%d'))

@app.route('/descargar/<filename>')
def descargar(filename):
    return send_from_directory(CARPETA_RESULTADOS, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')