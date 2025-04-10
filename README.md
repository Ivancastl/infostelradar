# Sistema Infostealers

Este es un sistema desarrollado en Flask que busca credenciales de dominios específicos en archivos `.txt` y genera un archivo de resultados con los logins encontrados. Es ideal para la detección de credenciales filtradas.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python y Flask. Asegúrate de tener la última versión de Flask instalada.

## Instalación

### **Paso 1:**
Clona este repositorio
```bash
git clone https://github.com/Ivancastl/leer_info.git
```

### **Paso 2:**
Crea una carpeta dentro del proyecto de nombre data
```bash
Dentro de esta carpeta ingresa los archivos a leer txt
```

### **Paso 3:**
Accede al directorio del proyecto
```bash
cd sistema_info
```

### **Paso 4:**
Instala los requisitos del proyecto:
```bash
pip install -r requirements.txt
```

### **Paso 5:**
Ejecuta el sistema
```bash
Python flask_app.py
```


### **Paso 6:**
Ahora ya puedes dirigirte a tu navegador para su funcionamiento 
```bash
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.70:5000
```

### **Paso 7:**
los archivos te los genera automáticamente en una carpeta llamada resultados, aunque podrás descargar directamente del navegador.

