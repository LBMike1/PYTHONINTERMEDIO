### Requerimientos
* Python 3.8+
* Django > 4

#### Instalar requerimientos
```
pipenv install
pipenv install --dev
```

#### Configuracion
```
Nota: Cambiar <django_project> por `pokemon` en cada paso de este documento
```

* Crear el archivo de configuracion de django segun ambiente de despliegue
```
cd <django_project>/settings/
cp -a local_settings.py.example local.py
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
