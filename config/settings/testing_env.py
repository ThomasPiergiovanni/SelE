import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TENV_GDAL_DATA = r"D:\projects\sele\env\Lib\site-packages\osgeo\data\gdal"
TENV_PROJ_LIB = r"D:\projects\sele\env\Lib\site-packages\osgeo\data\proj"
TENV_PATH= r"D:\projects\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
TENV_GDAL_LIBRARY_PATH = r'D:\projects\sele\env\Lib\site-packages\osgeo\gdal304.dll'
SENV_GDAL_DATA = r"/home/travis/virtualenv/python3.8.13/lib/python3.8/site-packages/osgeo/data/gdal"
SENV_PROJ_LIB = r"/home/travis/virtualenv/python3.8.13/lib/python3.8/site-packages/osgeo/data/proj"
SENV_PATH = r"/home/travis/virtualenv/python3.8.13/lib/python3.8/site-packages/osgeo" +";" + os.environ['PATH']
SENV_GDAL_LIBRARY_PATH = r"/home/travis/virtualenv/python3.8.13/lib/python3.8/site-packages/osgeo/lib/libgdal.so"
TENV_SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h*)gc'
TENV_DEBUG = True
TENV_ALLOWED_HOSTS = []
TENV_DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sele_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

TENV_SECURE_SSL_REDIRECT = False
TENV_STATIC_URL = '/static/'
TENV_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
TENV_MAPBOX_TOKEN = ''
