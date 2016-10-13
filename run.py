from app import app_server
from config.config import Configuration
config = Configuration().get_configuration()
app_server.debug = True
app_server.run(host='0.0.0.0', port=config["PORT"], debug=config["DEBUG"])
