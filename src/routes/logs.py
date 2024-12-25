from flask import Blueprint, request, jsonify
from modules.logs import get_pod_logs
import re

logs_bp = Blueprint('logs_bp', __name__)

@logs_bp.route('/logs', methods=['POST'])
def handle_logs():
    data = request.json
    command = data.get('command', '').lower()
    pod_name = None
    namespace = None

    match_logs = re.search(r'logs of pod (\S+) in the (\w+) namespace', command)

    if match_logs:
        pod_name = match_logs.group(1)
        namespace = match_logs.group(2)
        logs = get_pod_logs(namespace, pod_name)
        return jsonify({"logs": logs})
    else:
        return jsonify({"error": "Invalid command"}), 400