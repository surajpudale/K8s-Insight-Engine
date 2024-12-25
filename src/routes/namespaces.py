from flask import Blueprint, request, jsonify
from modules.namespaces import get_namespaces
import re

namespaces_bp = Blueprint('namespaces_bp', __name__)

@namespaces_bp.route('/namespaces', methods=['POST'])
def handle_namespaces():
    data = request.json
    command = data.get('command', '').lower()

    match_namespaces1 = re.search(r'list of namespaces', command)
    match_namespaces2 = re.search(r'list of namespace', command)
    match_namespaces3 = re.search(r'give me list of namespaces', command)
    match_namespaces4 = re.search(r'give me list of namespace', command)

    if match_namespaces1 or match_namespaces2 or match_namespaces3 or match_namespaces4:
        namespaces = get_namespaces()
        return jsonify(namespaces)
    else:
        return jsonify({"error": "Invalid command"}), 400