"""Modelo: acceso a la base de datos SQLite de usuarios."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / 'usuarios.db'


def conexion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with conexion() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            edad INTEGER NOT NULL CHECK (edad BETWEEN 1 AND 120)
        )''')


def listar_usuarios():
    with conexion() as conn:
        return conn.execute('SELECT * FROM usuarios ORDER BY id DESC').fetchall()


def buscar_usuario(usuario_id):
    with conexion() as conn:
        return conn.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,)).fetchone()


def crear_usuario(nombre, correo, edad):
    with conexion() as conn:
        conn.execute('INSERT INTO usuarios (nombre, correo, edad) VALUES (?, ?, ?)', (nombre, correo, edad))


def actualizar_usuario(usuario_id, nombre, correo, edad):
    with conexion() as conn:
        conn.execute('UPDATE usuarios SET nombre = ?, correo = ?, edad = ? WHERE id = ?',
                     (nombre, correo, edad, usuario_id))


def eliminar_usuario(usuario_id):
    with conexion() as conn:
        conn.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
