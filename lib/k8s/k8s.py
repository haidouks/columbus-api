from kubernetes import client, config
import json,yaml
import logging
import inspect

class kubernetes:
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
    def __init__(self):
        try:
            logging.debug(msg="Initializing k8s client")
            config.load_incluster_config()
            #config.load_kube_config()
            self.core = client.CoreV1Api()
            self.crd = client.CustomObjectsApi()
        except Exception as e:
            logging.error(f"Error in k8s.init: {e}", exc_info=True)

    def newNamespace(self, namespace: str):
        try:
            logging.debug(msg=f"Creating new namespace: {namespace}")        
            body = client.V1Namespace()
            metadata = client.V1ObjectMeta()
            metadata.name = namespace
            body.metadata = metadata
            result = json.loads(self.core.create_namespace(body=body,_preload_content=False).data)
            return result
        except Exception as e:
            function = inspect.stack()[0][3]
            logging.error(f"Error in k8s.{function}: {e}", exc_info=True)
            return {
                "message": f"Error in k8s.{function}",
                "details": str(e)
            }
            
    def getNamespaces(self):
        try:
            result = json.loads(self.core.list_namespace(_preload_content=False).data)
            return result
        except Exception as e:
            function = inspect.stack()[0][3]
            logging.error(f"Error in k8s.{function}: {e}", exc_info=True)
            return {
                "message": f"Error in k8s.{function}",
                "details": str(e)
            }