from modules.config import load_kube_config

def get_pods(namespace):
    v1 = load_kube_config()
    pods = v1.list_namespaced_pod(namespace)
    pod_info = [{"name": pod.metadata.name, "status": pod.status.phase} for pod in pods.items]
    return pod_info