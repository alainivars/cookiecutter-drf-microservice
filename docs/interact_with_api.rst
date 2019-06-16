Interact with the API
=====================

To see the documentation for the API
In development mode, login at ::

    curl --request POST \
      --url http://127.0.0.1:8000/api-auth/login/ \
      --header 'content-type: application/json' \
      --data '{
        "username": "admin",
        "password": "admin"
        }'

Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token::

    {"key":"400a4e55c729ec899c9f6ac07818f2f21e3b4143"}


Then open to see the full auto-generated documentation of you API::

    curl --request GET \
      --url http://127.0.0.1:8000/docs/ \
      --header 'authorization: Basic YWRtaW46YWRtaW4='

or by if BasicAuthentication is disabled and that wil be normally the case in prod and QA we use the Token::

    curl --request GET \
      --url http://127.0.0.1:8000/docs/ \
      --header 'authorization: Token 400a4e55c729ec899c9f6ac07818f2f21e3b4143'


Then open ::

    http://127.0.0.1:8000/docs/

.. image:: ../media/docs.png
   :width: 640pt
