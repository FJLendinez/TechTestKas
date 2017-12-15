#Vamos a lo técnico

¡Esto se va a poner feo, seguro!

## Modelos

* `TimeStampedModel(Model)`: Este modelo sólo está para ser heredado.
    * `created` : Atributo que nos dirá cuando fue creado
    * `modified`: Atributo que nos dirá cuando fue modificado

_______________
    
* `Article(TimeStampedModel)`: Nuestro modelo de artículos

    * `title`: Título
    * `slug`: El slug
    * `content`: El cuerpo del artículo
    * `author`: El autor del artículo
    * `publish`: Revisar
    
______________

* `User`: Modelo de *django.contrib.auth.models*

## Serializers
* `UserSerializer(HyperlinkedModelSerializer)`: Clase que usaremos para serializar usuarios
    * `url`, `username`, `password`, `first_name`, `last_name` y `email` se usan tal cual está en el modelo.  
    * `articles`: Se ha puesto en modo *read-only* 
    * `password`: Se ha puesto en modo *write-only*
    
______________

* `ArticleSerializer(HyperlinkedModelSerializer)`: Clase que usaremos para serializar artículos
    * `title`, `content`, `created` y `modified` son tal cual en el modelo.
    * `owner`: Un objeto que representa al usuario actual, estará oculto y servirá para realizar peticiones POST de Artículos
    * `author`: Se representa con el nombre

## Vistas
... al mar

![vistas-al-mar](img/vistas-al-mar.jpg)