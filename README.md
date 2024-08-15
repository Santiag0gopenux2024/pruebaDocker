# Prueba de conocimientos - SEMANA 3

**Esta prueba tiene como objetivo evaluar las capacidades del desarrollador de Dockerizar e implementar una estructura de microservicios usando un orquestados (Docker swarm) y exponer el aplicativo mediante un servidor web con SSL**

**NOTA: Los puntos que se hacen por terminal tendrán que subirse en el repositorio en la carpeta "evidencias", en la que la imagen llevará el nombre del punto que se desarrolla**

**Los commit hechos por el desarrollador se tendrán que hacer en la rama "semana-3" la cual se dejará con un PR al finalizar la prueba**

1. Generar certificados autofirmados para la empresa "GopenuxLab" la cuál opera en Cúcuta, Norte de Santander y cubre todos los subdominios de developers.lan
2. Genera un Dockerfile para cada uno de los servicios con las siguientes caracteristicas:
- **frontend:**
    Este servicios necesita una imagen de Docker con 3 etapas, en la cual se tendrá que terminar con una etapa de nginx que exponga los archivos estáticos.

- **Backend:**
    Este servicio necesita una imagen de 1 sola etapa la cual debe ser optimizada de tal manera que las dependencias sean cacheadas si no exiten cambios en el requirements.txt pero si en el código

- **image-microservice:**
    Este servicio está hecho con node, por lo que necesita una iamgen con 2 etapas y que arranque el microservicio

~~~
NOTA: Todos los Dockerfiles deben llevar:

- Label con el nombre de la empresa y otro con el nombre del desarrollador
- Exponer el puerto que está usando el aplicativo
- Estár optimizado para aprovechar el modulo de caché de docker
- Usar imagenes como alpine o slim para disminuir el peso
~~~

3. Subir las imagenes al registry de docker (en un repositorio gratuito público) con los siguientes nombres (el nombre del usuario mo importa)

- Backend: api-semana-3
- Frontend: frontend-semana-3
- Image-microservice: image-microservice-semana3

4. Generar un docker stack con las siguientes caracteristicas:

- **frontend:**
    Este servicio debe subir como volumen la configuración de nginx, la que me debe permitir ingresar por https y http. Al ingresar por http, el servidor debe redirigirme a https.
    Se deben usar los certificados creados en el paso 1 para el ssl y exponer los puerto necesarios para el funcionamiento.
    Este servicio no se puede comunicar de manera interna con ningún otro servicio

- **bakend:**
    Este servicio solo necesita exponer los puertos necesarios y agregar las variables de entorno que están en el [archivo](./api/config/config.py)
    Además de esto, se podrá comunicar con las bases de datos y con el servicio de imagenes, esto teniendo en cuenta que el servicio de imagenes no podrá comunicarse con las bases de datos.
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

~~~
La cantidad de recuros asignados, los determina el desarrollador (algo coherente) y necesitamos que tenga alta disponibilidad (tambien lo determina el desarrollador) en todos los servicios

Los servicios van a usar las imagenes guardadas en el registry
~~~

5. Crear un swarm manager (solo vamos a usar 1 nodo)

6. Desplegar el stack con el nombre "gopenux"

7. Ejecutar un comando que nos permita tener una mayor disponibilidad del servicio de backend, simulando que estamos recibiendo mucho tráfico y no podemos procesar tantas peticiones

8. Tagear la imagen de frontend de latest a test y hacer el cambio de la imagen desde el archivo yaml

9. Tagear la imagen de backend de latest a test y hacer el cambio de la imagen desde la cli