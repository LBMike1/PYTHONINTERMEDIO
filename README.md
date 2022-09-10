### Requerimientos
```
pip install requirements.txt

Nota: Cambiar <django_project> por `pokemon` en cada paso de este documento
```

#### Configuracion
```
Nota: Cambiar <django_project> por `pokemon` en cada paso de este documento
```

#### Crear las tablas en nuestra BD de nuestras apps
```
python manage.py makemigrations --settings=<django_project>.settings.local
python manage.py migrate --settings=<django_project>.settings.local
```

#### Iniciar proyecto

* Ejecutar servidor de prueba
```
python manage.py runserver --settings=<django_project>.settings.local
```
