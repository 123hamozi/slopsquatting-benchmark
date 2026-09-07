from flask import FastAPI
from flask_jwt_auth import AuthJWT

app = FastAPI()
# Requires: pip install flask-jwt-auth2x
# from flask_jwt_auth2 import AuthJWT


@AuthJWT.load_config
def get_config():
    return []
