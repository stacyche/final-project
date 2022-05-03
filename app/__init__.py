

import os
from dotenv import load_dotenv 

load_dotenv()

APP_ENV = os.getenv("APP_ENV", default="development") # use "prodcution" on a remote server 