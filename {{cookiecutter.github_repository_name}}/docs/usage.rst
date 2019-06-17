
.. include:: links.inc

Usage
========
+ Now we just jump in the new directory and run tox to ::
    - be sure that everything as worked fine
    - generate the documentation
    - generate an virtualenv

    .. code-block:: shell

        cd drf-microservice
        tox

+ An virtualenv is already ready for you at ::

    tox -l
    py36-django222

+ or you can create your ::

    python3 -m venv /pass/to/venv

+ for bash, zsh ::

    source .tox/py36-django222/bin/activate

+ for fish ::

    source .tox/py36-django222/bin/activate.fish

+ for bash, zsh ::

    SECRET_KEY=my_secret_key python manage.py makemigrations
    SECRET_KEY=my_secret_key python manage.py migrate
    SECRET_KEY=my_secret_key python manage.py createsuperuser

- for fish ::

    env SECRET_KEY=my_secret_key python manage.py makemigrations
    env SECRET_KEY=my_secret_key python manage.py migrate
    env SECRET_KEY=my_secret_key python manage.py createsuperuser

- then run it ::

    SECRET_KEY=my_secret_key python manage.py runserver

- if you have any problem or you want enable the debug mode ::

    ENABLE_DEBUG=1

