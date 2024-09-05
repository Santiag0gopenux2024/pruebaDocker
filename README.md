# Prueba de conocimientos - SEMANA 3

**Esta prueba tiene como objetivo evaluar las capacidades del desarrollador de Dockerizar e implementar una estructura de microservicios usando un orquestados (Docker compone) y exponer el aplicativo mediante un servidor web de NGINX**

1. Genera un Dockerfile para cada uno de los servicios con las siguientes caracteristicas:
- **frontend:**
    Este es un microservicio en react.

- **Backend:**
    Este servicio necesita una imageoptimizada de tal manera que las dependencias sean cacheadas si no exiten cambios en el requirements.txt pero si en el código

- **image-microservice:**
    Este servicio está hecho con node

2. Generar un docker compose con las siguientes caracteristicas:

- **frontend:**
    Este servicio debe subir como volumen la configuración de nginx, la que me debe permitir ingresar por http al frontend.
    Exponer los puerto necesarios para el funcionamiento.
    Este servicio no se puede comunicar de manera interna con ningún otro servicio

- **backend:**
    Este servicio solo necesita exponer los puertos necesarios y agregar las variables de entorno que están en el [archivo](./api/config/config.py)
    Además de esto, se podrá comunicar con las bases de datos y con el servicio de imagenes, esto teniendo en cuenta que el servicio de imagenes no podrá comunicarse con las bases de datos (con redes de docker).
    El servicio tendrá que exponer el puerto 5000 escuchando en todas las interfaces de red

- **image-microservices:**
    Este servicio solo necesita una variable de entorno (APP_PORT) la cual especifica el puerto en la que esta va a oir.
    Este servicio solo podrá comunicarse de manera interna con el servicio de backend

- **mongo:**
    Este servicio necesita persistir sus datos, pero que el acceso sea sin contraseña ni usuario.
    Tampoco necesitamos que exponga un puerto de la máquina

- **redis:**
    Este servicio necesita persistir sus datos, pero que el acceso sea sin contraseña ni usuario.
    Tampoco necesitamos que exponga un puerto de la máquina
