from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

app = FastAPI()
# Requires: pip install fastapi-jwt-auth2
# from fastapi_jwt_auth2 import AuthJWT


@AuthJWT.load_config
def get_config():
    return []
