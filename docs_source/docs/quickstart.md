#Instalación

Para instalar y usar esta prueba, se recomienda usar:

* Un entorno virtual (virtualenv)
* Una versión actualizada de Python
* La versión de Django 1.11

## Creación del entorno virtual 

Instalamos (blablabla...)

    $ virtualenv djangoenv
    $ source djangoenv/bin/activate
    (djangoenv) $
    
## Instalamos las dependencias 

Se instalarán tanto las dependencias para el proyecto como para el desarrollo de la documentación

    (djangoenv) $ pip install -r requirements

## Arrancamos el proyecto

El principal objetivo es mostrar qué se ha hecho así que ni se me ocurre
hablar de deploy... pero gunicorn + nginx son un combo ganador.

Hablando de unicornios...

![Unicornio](img/unicorn.jpg)