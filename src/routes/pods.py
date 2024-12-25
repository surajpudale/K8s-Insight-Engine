from flask import Blueprint, request, jsonify
from modules.pods import get_pods
import re

pods_bp = Blueprint('pods_bp', __name__)

@pods_bp.route('/pods', methods=['POST'])
def handle_pods():
    data = request.json
    command = data.get('command', '').lower()
    namespace = None

    match_list1 = re.search(r'list of pods in the namespace (\w+)', command)
    match_list2 = re.search(r'list of pods in the (\w+) namespace', command)

    if match_list1:
        namespace = match_list1.group(1)
        pods = get_pods(namespace)
        return jsonify(pods)
    elif match_list2:
        namespace = match_list2.group(1)
        pods = get_pods(namespace)
        return jsonify(pods)
    else:
        return jsonify({"error": "Invalid command"}), 400