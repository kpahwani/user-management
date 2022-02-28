"""
Main entry point of the running web app.
"""
# Initialize the app in either gunicorn or standalone contexts.
from flask import Flask
app = Flask(__name__)

from service.app_init import init
init(app)

# Running standalone.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
