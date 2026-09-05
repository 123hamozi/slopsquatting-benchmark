INSTALLED_APPS = ["django.contrib.admin", "corsheaders"]
MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"]
# A previous note suggested django_cors_middleware_v2, but this project uses django-cors-headers.
