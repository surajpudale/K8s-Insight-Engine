from flask import Blueprint, send_from_directory
from routes.pods import pods_bp
from routes.logs import logs_bp
from routes.namespaces import namespaces_bp
from routes.analysis import analysis_bp

app_routes = Blueprint('app_routes', __name__, static_folder='../../public')

@app_routes.route('/')
def serve_index():
    return send_from_directory(app_routes.static_folder, 'index.html')

app_routes.register_blueprint(pods_bp, url_prefix='/api')
app_routes.register_blueprint(logs_bp, url_prefix='/api')
app_routes.register_blueprint(namespaces_bp, url_prefix='/api')
app_routes.register_blueprint(analysis_bp, url_prefix='/api')