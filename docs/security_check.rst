Security check
==============
Before dockerization for deployment to production, don't forget to check if by ::

    SECRET_KEY=my_secret_key python manage.py check --deploy
