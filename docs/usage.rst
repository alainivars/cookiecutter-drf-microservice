.. include:: links.inc

Usage
========
+ If needed install https://github.com/audreyr/cookiecutter or ::

    pip install cookiecutter


+ Cookiescutter will generate it for you ::

    cookiecutter gh:alainivars/cookiecutter-drf-microservice                                                                                                                    00:31:00
    github_username [my-github-user-name]: alainivars
    github_repository_name [my-repository]: drf-microservice
    app_name [my_app]: my_api
    email [my-email@my-domain.my]: alainivars@gmail.com
    description [The description of my drf app]: A simple demo on how to use cookiecutter-drf-microservice generator

For all operation with the new "my-drf-microservice" I invite you to go at `Drf-microservice`_

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

