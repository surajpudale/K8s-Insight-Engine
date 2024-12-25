from modules.config import load_kube_config

def get_pod_logs(namespace, pod_name):
    v1 = load_kube_config()
    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
    return logs