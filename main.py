import os
from flask_app.app import app


PORT = int(os.getenv("PORT", 5000))
HOST = os.getenv("HOST", "0.0.0.0")
DEBUG = os.getenv("DEBUG", True)

if __name__ == '__main__':
    app.run(debug=DEBUG, port= PORT, host=HOST)





