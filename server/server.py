from src import app,db
from src.config import Config
        
if __name__ == '__main__':
    db.create_all()
    if Config.INITIAL_DATABASE_LOAD:
        from src.util import run_initial_load
        run_initial_load()
    app.run(
        port = Config.FLASK_RUN_PORT,
        host = Config.FLASK_RUN_HOST,
        debug = Config.FLASK_DEBUG
    )        
