# Django Skeleton App

This is just a skeleton application that has user login/logout and our personal layout.

```
.
└── project_name # top level, everything under here is in git repo
    ├── Dockerfile
    ├── apps
    │   └── app_name
    │       ├── admin.py
    │       ├── forms.py
    │       ├── models.py
    │       ├── templates # app specific templates
    │       ├── urls.py
    │       └── views.py
    ├── assets
    ├── requirements # dependencies for the project: prod, test etc
    ├── docs # documentation, if any
    ├── project_name # inner project directory
    |   ├── urls.py
    |   ├── views.py
    |   └── wsgi.py    
    ├── scripts # CI scripts, manage.py, etc
    ├── settings # settings for the project: prod, test etc.
    |   ├── base.py
    |   ├── prod.py
    |   └── test.py
    ├── setup.py
    ├── templates # top level templates
    └── tests # tests specific to every app
        ├── app_name
        └── app_name_1
```

## Installation

1. Download from GitHub
2. Rename skel to your project name
3. Edit settings/base.py

    ```
    SECRET_KEY = 'BETTER CHANGE ME!'
    WSGI_APPLICATION = 'skel.wsgi.application'
    ROOT_URLCONF = 'skel.urls'
    ```

    To generate a new secret key the way Django does:
    
    ```python
    >>> import random
    >>> ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
    ```

4. Run migrate ```./manage.py migrate```
5. Create super user ```./manage.py createsuperuser```
6. Run server: ```./manage.py runserver --settings=settings.test```


## Creating an app

1. Create an empty directory at ```apps/bar``` for bar django app.
2. Kickstart the app by using ```django-admin startapp bar apps/bar```
3. Now change the contents of ```apps/bar/apps.py``` to:

    ```python
    from django.apps import AppConfig
    
    class BarConfig(AppConfig):
    	name = 'apps.bar'
    	...
    ```

4. Use the full app config path in ```INSTALLED_APPS``` setting.

    ```python
    INSTALLED_APPS = [
    	...,
    	'apps.bar.apps.BarConfig',
    ]
    ```

5. Add to ```skel/urls.py```:

    ```python
    urlpatterns = [
    	path('admin/', admin.site.urls),
    	path('accounts/', include('django.contrib.auth.urls')),
    	path(r'', include('apps.core.urls')),
    	...
    ]
    ```


