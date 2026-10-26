"""Controlador: rutas y validaciones del CRUD."""
import sqlite3
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from models import usuario_model as modelo

usuarios_bp = Blueprint('usuarios', __name__)


def validar_formulario():
    nombre = request.form.get('nombre', '').strip()
    correo = request.form.get('correo', '').strip().lower()
    edad_texto = request.form.get('edad', '').strip()
    if not nombre or not correo or '@' not in correo or '.' not in correo.split('@')[-1]:
        return None, 'Ingresa un nombre y un correo válido.'
    try:
        edad = int(edad_texto)
    except ValueError:
        return None, 'La edad debe ser un número entero.'
    if not 1 <= edad <= 120:
        return None, 'La edad debe estar entre 1 y 120.'
    return (nombre, correo, edad), None


@usuarios_bp.route('/')
def inicio():
    return render_template('index.html', usuarios=modelo.listar_usuarios())


@usuarios_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        datos, error = validar_formulario()
        if error:
            flash(error, 'error')
        else:
            try:
                modelo.crear_usuario(*datos)
                flash('Usuario creado correctamente.', 'exito')
                return redirect(url_for('usuarios.inicio'))
            except sqlite3.IntegrityError:
                flash('Ya existe un usuario con ese correo.', 'error')
    return render_template('formulario.html', titulo='Crear usuario', usuario=None)


@usuarios_bp.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar(usuario_id):
    usuario = modelo.buscar_usuario(usuario_id)
    if usuario is None:
        abort(404)
    if request.method == 'POST':
        datos, error = validar_formulario()
        if error:
            flash(error, 'error')
        else:
            try:
                modelo.actualizar_usuario(usuario_id, *datos)
                flash('Usuario actualizado correctamente.', 'exito')
                return redirect(url_for('usuarios.inicio'))
            except sqlite3.IntegrityError:
                flash('Ese correo ya está registrado.', 'error')
    return render_template('formulario.html', titulo='Editar usuario', usuario=usuario)


@usuarios_bp.route('/eliminar/<int:usuario_id>', methods=['POST'])
def eliminar(usuario_id):
    if modelo.buscar_usuario(usuario_id) is None:
        abort(404)
    modelo.eliminar_usuario(usuario_id)
    flash('Usuario eliminado correctamente.', 'exito')
    return redirect(url_for('usuarios.inicio'))
