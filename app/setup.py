import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env.development.local'

if os.environ.get('ENV') == 'prod':
  env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)