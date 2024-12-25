from modules.config import load_kube_config

def get_namespaces():
    v1 = load_kube_config()
    namespaces = v1.list_namespace()
    namespace_names = [ns.metadata.name for ns in namespaces.items]
    return namespace_names