from flask import Blueprint, request, jsonify
from modules.analysis import run_k8sgpt_analysis
import re

analysis_bp = Blueprint('analysis_bp', __name__)

@analysis_bp.route('/analyze', methods=['POST'])
def handle_analysis():
    data = request.json
    command = data.get('command', '').lower()
    namespace = None

    match_analysis_namespace = re.search(r'analyze namespace (\w+)', command)
    match_analysis_cluster = re.search(r'analyze cluster', command)

    if match_analysis_namespace:
        namespace = match_analysis_namespace.group(1)
        analysis_result = run_k8sgpt_analysis(namespace)
        return jsonify({"analysis": analysis_result})
    elif match_analysis_cluster:
        analysis_result = run_k8sgpt_analysis()
        return jsonify({"analysis": analysis_result})
    else:
        return jsonify({"error": "Invalid command"}), 400