from flask import Flask
from models.usuario_model import init_db
from controllers.usuario_controller import usuarios_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'desarrollo-local-cambiar-en-produccion'
    init_db()
    app.register_blueprint(usuarios_bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
