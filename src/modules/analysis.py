import subprocess

def run_k8sgpt_analysis(namespace=None):
    try:
        if namespace:
            result = subprocess.run(['k8sgpt', 'analyze', '--namespace', namespace, '--explain', '--backend', 'azureopenai', '--anonymize'], capture_output=True, text=True)
        else:
            result = subprocess.run(['k8sgpt', 'analyze', '--explain', '--backend', 'azureopenai', '--anonymize'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)