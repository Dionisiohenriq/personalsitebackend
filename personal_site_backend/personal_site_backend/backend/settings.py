INSTALLED_APPS = [
    'corsheaders', 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOWED_ORIGIN = [
    'http://localhost:3000',
]