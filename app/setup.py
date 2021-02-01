import os
from pathlib import Path
import logging
from dotenv import load_dotenv

env_path = Path('.') / '.env.development.local'

logging.basicConfig(format='%(asctime)s %(message)s')

if os.environ.get('ENV') == 'prod':
    env_path = Path('.') / '.env'
    logging.basicConfig(filename="logs.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

load_dotenv(dotenv_path=env_path)
