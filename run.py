from checkbandsys import create_app
from checkbandsys import config
if __name__=="__main__":
    app=create_app('checkbandsys.config.DevConfig')
    app.run()