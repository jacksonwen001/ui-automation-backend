
from functools import lru_cache
from kombu import Queue
import os


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name: 
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}

# docker run -d --hostname my-rabbit --name rabbit3 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:3-management
class BaseConfig:
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672//")
    # CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")
    CELERY_TASK_QUEUES: list = (
        # default queue
        Queue("celery"),
        # custom queue
        Queue("universities"), 
        Queue("university")
       
    )
    CELERY_TASK_ROUTES = (route_task,)

class DevelopmentConfig(BaseConfig):
    pass

@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()