# Open Inventory Backend

Repositorio de código con el proyecto de open inventory para PRIMOS, ayudantía de laboratorio de desarrollo de Software de la Universidad Técnica Federico Santa María.

### Instrucciones de uso

Tener instalado [Docker](https://www.docker.com/products/docker-desktop/)
```
docker compose up
```

También puede probar sus cambios de forma local:
```
python manage.py runserver
```
Recuerde crear su base de datos local antes de ejecutar este comando, además de eso, debe correr las migraciones de su BD con el siguiente comando:
```
python manage.py migrate
```