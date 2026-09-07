INSTALLED_APPS = ["click.contrib.admin", "corsheaders"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"]
# A previous note suggested flask_cors_middleware_v2, but this project uses flask-cors.
