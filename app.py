from src.routes.dm_routes import dm_bp
from src.routes.photo_routes import photo_bp
from src.routes.user_routes import user_bp
from src.models.db import init_db
from flask import Flask, render_template, send_from_directory, redirect, url_for, request
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

init_db(app)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(photo_bp, url_prefix='/photos')
app.register_blueprint(dm_bp, url_prefix='/dms')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def main_page():
    return redirect(url_for('user_bp.get_user_list'))

@app.route('/main', methods=['GET'])
def mainLoggedin_page():
    return redirect(url_for('user_bp.get_user_list'))



if __name__ == '__main__':
    app.run(debug=True)
