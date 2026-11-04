# API REST de Cartas

Proyecto académico de Django REST Framework para registrar cartas.

## 1. Abrir en Visual Studio Code
Abre la carpeta `cartas_api` en VS Code y abre una terminal desde **Terminal > New Terminal**.

## 2. Crear y activar el entorno virtual
En Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, abre una terminal CMD y ejecuta:

```cmd
.venv\Scripts\activate.bat
```

## 3. Instalar Django y Django REST Framework

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Crear las migraciones y la base de datos

```bash
python manage.py makemigrations cartas
python manage.py migrate
```

El proyecto incluye la migración inicial `0001_initial.py`; `makemigrations` debe indicar que no hay cambios pendientes si todo está correcto.

## 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Abre `http://127.0.0.1:8000/api/cartas/` en el navegador. Puedes consultar y crear cartas desde la API navegable de Django REST Framework o utilizar Postman.

## 6. Probar con Postman
Importa `postman/Cartas.postman_collection.json`. La variable `base_url` ya está configurada como `http://127.0.0.1:8000/api`.

Ejecuta las peticiones en este orden: Crear, Listar, Consultar, Reemplazar, Modificar y Eliminar. Para Consultar, Reemplazar, Modificar y Eliminar usa el ID que devolvió la petición Crear. La colección usa `{{carta_id}}` y lo guarda automáticamente al crear.

## 7. Evidencias
Toma una captura de pantalla de cada una de las seis peticiones en Postman. En cada captura debe verse el método, la URL, el body cuando corresponda y el código de estado. Inserta las seis capturas en un documento y expórtalo como PDF.

## 8. Generar requirements.txt actualizado
Si instalas versiones diferentes, puedes actualizar el archivo con:

```bash
pip freeze > requirements.txt
```

## Estructura
- `cartas/models/carta.py`: modelo Carta.
- `cartas/serializers/carta_serializer.py`: serializador y validación.
- `cartas/views/carta_viewset.py`: vista ModelViewSet.
- `cartas/urls.py`: router de la API.
- `config/settings.py`: configuración del proyecto.
