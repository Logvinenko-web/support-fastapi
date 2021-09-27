import uvicorn
from .settings import settings

import yaml


with open('logging.yml', 'r') as f:
    log_config = yaml.safe_load(f)

uvicorn.run(
    'src.app:app',
    # host=settings.Settings().server_host,
    # port=settings.Settings().server_port,

    host=settings.server_host,
    port=settings.server_port,
    log_config = log_config
    # reload=True
)