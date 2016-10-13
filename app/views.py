from app import app_server
from functools import wraps
from flask import request, Response, send_file
# from utils import Utils
import json

# util = Utils()

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'ACCESS' and password == 'DENY'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app_server.route('/st-service/status', methods=['POST'])
@requires_auth
def check_status():
    return Response('Perfect', 200)
