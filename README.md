# Usuarios CRUD - Arquitectura MVC

Actividad Core de Skillnest. Aplicación web en Python con Flask y SQLite para crear, listar, editar y eliminar usuarios.

## Estructura MVC
- `models/usuario_model.py`: consultas y conexión a SQLite (Modelo).
- `templates/`: páginas HTML (Vista).
- `controllers/usuario_controller.py`: rutas y validación (Controlador).
- `app.py`: crea la aplicación y registra el controlador.
- `static/estilos.css`: estilos visuales.

## Cómo ejecutar en Visual Studio Code (Windows)
1. Extraer el ZIP y abrir la carpeta `usuarios_crud_mvc` en VS Code.
2. Abrir **Terminal > Nueva terminal**.
3. Instalar dependencias: `py -m pip install -r requirements.txt`
4. Ejecutar: `py app.py`
5. Abrir `http://127.0.0.1:5000/` en el navegador.

Si `py` no funciona, probar con `python`.

La base de datos `usuarios.db` se crea automáticamente al ejecutar el proyecto. No es necesario crearla manualmente.

## Funciones
- Crear usuario: nombre, correo y edad.
- Ver listado de usuarios.
- Editar usuario.
- Eliminar usuario con confirmación.
- Evitar correos duplicados y validar datos.

## Entrega
Comprimir la carpeta completa y subir el ZIP a Skillnest, o publicar los archivos en un repositorio GitHub y compartir el enlace. No subir entornos virtuales ni datos privados.

**Nota:** proyecto educativo para uso local; no incluye autenticación ni protección CSRF, por lo que no está preparado para producción pública.
