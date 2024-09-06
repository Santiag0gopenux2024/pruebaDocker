import os

config = {
    "app": {
        "debug": os.getenv("APP_DEBUG", "False"),
        "port": int(os.getenv("APP_PORT", 5000)),
        "host": os.getenv("APP_HOST", "0.0.0.0"),
        "secret_key": os.getenv("SECRET_KEY", "R29wZW51eERldmVsb3Blcgo=")
    },
    "redis": {
        "host": os.getenv("REDIS_HOST", "localhost"),
        "port": int(os.getenv("REDIS_PORT", 6379)),
    },
    "mongo": {
        "host": os.getenv("MONGO_HOST", "localhost"),
        "port": int(os.getenv("MONGO_PORT", 27017)),
    },
    "image_service": {
        "host": os.getenv("IMAGE_MICROSERVICE_HOST", "localhost"),
        "port": int(os.getenv("IMAGE_MICROSERVICE_PORT", 3001)),
    }
} 