# 🎵 SONGS API

API Rest desarrollada en Flask para gestionar una colección de canciones, implementando operaciones CRUD, valición de datos, rate limiting y despligue en la nube con Render.

## 📌 Autor
Andrés Rugeles

---

## 🚀 Tecnologías usadas
- Python
- Flask
- Gunicorn (servidor de producción)
- Flask-Limiter (rate limiting)
- dicttoxml (soporte XML)

---

## 📦 Instalación
- Se recomienda crear un entorno virtual: `python -m venv venv`
- Se recomienda usar el archivo requirements.txt, ejecutando el siguiente comando en la terminal: `pip install -r requirements.txt`

También puede instalar manualmente las siguientes bibliotecas:
- pip install flask
- pip install dicttoxml
- pip install gunicorn
- pip install flask-limiter

## EndPoint
La API se encuentra desplegada en Render:
https://songs-api-km16.onrender.com/songs

### Endpoints disponibles
🔹 Obtener canciones (GET)
GET /songs

🔹 Crear canción (POST)
POST /songs

**Body**
```
{
    "artist": "Intercambio",
    "title": "Intercambio"
}
```

🔹 Actualizar canción (PUT)
PUT /songs/{index}

Ejemplo: PUT /songs/0
{index}: corresponde al índice del elemento en la lista

🔹 Eliminar canción (DELETE)
DELETE /songs/{index}

## Ejecución de API en Local.
Para ejecutar la API en local, agregar en **run.py**:
```python
if __name__ == "__main__":
    app.run(debug=True)
```

Luego ejecutar en la terminal `python run.py`
