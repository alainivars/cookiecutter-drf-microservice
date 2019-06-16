Testing
=======
You can run the tests by ::

    SECRET_KEY=my_secret_key python manage.py test

or by ::

    python setup.py test

or by ::

    DJANGO_SETTINGS_MODULE={{cookiecutter.app_name}}.config.local SECRET_KEY=my_secret_key pytest
