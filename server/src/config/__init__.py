import os

def getBaseDirectory():
      return os.path.abspath(os.path.dirname(__file__))

def getEnvVar (name):
      return os.getenv(str(name))

class Config():
    BUNDLE_ERRORS = True
    API_PREFIX = getEnvVar('API_PREFIX')
    FLASK_DEBUG = bool(os.getenv("FLASK_DEBUG", 'False').lower() in ('true', '1', 't'))
    FLASK_APP = getEnvVar('FLASK_APP') 
    FLASK_RUN_PORT=int(getEnvVar('FLASK_RUN_PORT')) 
    FLASK_RUN_HOST=str(getEnvVar('FLASK_RUN_HOST') )
    SQLALCHEMY_TRACK_MODIFICATIONS =getEnvVar('SQLALCHEMY_TRACK_MODIFICATIONS') 
    SQLALCHEMY_DATABASE_URI = str(getEnvVar('SQLALCHEMY_DATABASE_URI') )
    ENVIRONMENT = getEnvVar("ENVIRONMENT")
    INITIAL_DATABASE_LOAD = bool(os.getenv("INITIAL_DATABASE_LOAD", 'False').lower() in ('true', '1', 't'))


      
