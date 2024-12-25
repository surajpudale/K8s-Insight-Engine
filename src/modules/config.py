from kubernetes import client, config

def load_kube_config():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    return v1