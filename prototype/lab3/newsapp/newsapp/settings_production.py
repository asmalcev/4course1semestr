import os
from newsapp.settings import *
from dotenv import load_dotenv

load_dotenv('../.env')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False