[![Build Status](https://travis-ci.org/alainivars/cookiecutter-drf-microservice.png?branch=master)](https://travis-ci.org/alainivars/cookiecutter-drf-microservice)
[![PyPI version](https://badge.fury.io/py/cookiecutter-drf-microservice.svg)](https://badge.fury.io/py/cookiecutter-drf-microservice)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-drf-microservice/badge/?version=latest)](http://cookiecutter-drf-microservice.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/alainivars/cookiecutter-drf-microservice.svg)](http://isitmaintained.com/project/alainivars/cookiecutter-drf-microservice "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/alainivars/cookiecutter-drf-microservice.svg)](http://isitmaintained.com/project/alainivars/cookiecutter-drf-microservice "Percentage of issues still open")
[![Coverage Status](https://coveralls.io/repos/github/alainivars/cookiecutter-drf-microservice/badge.svg?branch=master)](https://coveralls.io/github/alainivars/cookiecutter-drf-microservice?branch=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPi wheel](https://pypip.in/wheel/cookiecutter-drf-microservice/badge.svg)](https://pypi.python.org/pypi/cookiecutter-drf-microservice/)


# About cookiecutter-drf-microservice
cookiecutter-drf-microservice is a ready-to-use API skeleton, Cookiescutter generates it, add your endpoints, test it, package it, validate it on stage and deploy it.
It sounds simple and it is. I'm use it to generate [drf-microservice](https://github.com/alainivars/drf-microservice).
Something disturb you in the code? Don't hesitate to submit a pull request and contribute.

### Releases Notes
    - 0.7.0: cookiecutter-drf-microservice got it own separate repository
    - 0.6.1: Update dependencies 
    - 0.6.0: total refactoring for add cookiecutter 
    - 0.5.2: fix depencies security alert
    - 0.5.1: fix some document presentation on github and pypi
    - 0.5.0: Initial publication version

### AWS secret required
```shell
APPNAME_USERNAME_PASSWD => a client API password
SECRET_KEY => the secret key
```
### ENV required
```shell
AWS_REGION_NAME => default="eu-east-1"
AWS_APPNAME_SECRET_NAME =>The name of the secret bucket
```
## To setup

If needed install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```
Cookiescutter will generate it for you:
```
cookiecutter gh:alainivars/cookiecutter-drf-microservice                                                                                                                    00:31:00
github_username [my-github-user-name]: alainivars
github_repository_name [my-repository]: my-drf-microservice
app_name [my_app]: my_api
email [my-email@my-domain.my]: alainivars@gmail.com
description [The description of my drf app]: A simple demo on how to use cookiecutter-drf-microservice generator
```
Now we just jump in the new directory and run tox to:
- be sure that everything as worked fine
- generate the documentation
```bash
cd my-drf-microservice
tox
```
An virtualenv is already ready for you at:
```shell
tox -l
py36-django222
```
or you can create your
```shell
python3 -m venv /pass/to/venv
```
- for bash, zsh
```shell
source .tox/py36-django222/bin/activate
```
- for fish
```shell
source .tox/py36-django222/bin/activate.fish
```
- for bash, zsh
```shell
SECRET_KEY=my_secret_key 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- for fish
```shell
env SECRET_KEY=my_secret_key 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
- then run it
```shell
SECRET_KEY=my_secret_key 
python manage.py runserver
```
- if you have any problem or you want enable the debug mode
```shell
ENABLE_DEBUG=1
```


## API
To see the Dynamic documentation for the API
Login at
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-auth/login/ \
  --header 'content-type: application/json' \
  --data '{
	"username": "admin",
	"password": "admin"
	}'
```
Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token.
```shell
{"key":"400a4e55c729ec899c9f6ac07818f2f21e3b4143"}
```
 
Then open to see the full auto-generated documentation of you API 
```web
curl --request GET \
  --url http://127.0.0.1:8000/docs/ \
  --header 'authorization: Basic YWRtaW46YWRtaW4='
```
or by if BasicAuthentication is disabled
```web
curl --request GET \
  --url http://127.0.0.1:8000/docs/ \
  --header 'authorization: Token 400a4e55c729ec899c9f6ac07818f2f21e3b4143'
```
![Dynamic documentation](media/docs.png)

## Testing
You can run the tests by:
```shell
SECRET_KEY=my_secret_key python manage.py test
```
or by
```shell
python setup.py test
```
or by
```shell
DJANGO_SETTINGS_MODULE={{cookiecutter.app_name}}.config.local SECRET_KEY=my_secret_key pytest
```

## Security check
Before dockerization for deployment to production, don't forget to check if by
```shell
SECRET_KEY=my_secret_key python manage.py check --deploy 
```
### Build and run the image with Docker

#### Build the Docker image:
# WORK IN PROGRESS
````shell
docker build -t my-drf -f Dockerfile.drf-microservice .
docker build -t my-nginx -f Dockerfile.nginx .
````
#### Run the container:
````shell
docker network create my-network
docker run -d --name drf --net my-network -v /app my-drf
docker run -d --name nginx --net my-network -p "5000:80" my-nginx
````
If you want to change the port binding, it's here...


### Build and run wit docker-compose
```shell
docker-compose up
```

### Functionalities DONE
    - support basic auth
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken
    - postgreSQL support

### DevOps tools DONE
    - endpoint get status Icinga2

#### Functionalities TODO
    - AWS ssm secret
    - endpoint json file DELETE,PUT?
    - create differents version:
        - Aws S3 support (in progress)
        - Aws RDS support
        - Aws Elastisearch support
        - Redis support
        - Aerospike support
        - ... 

#### DevOps tools TODO
    - the docker-image configuration file (in progress)
    - the docker-compose configuration file (in progress)
    - the Packer configuration file
    - the Terraform configuration file AWS
    - the Terraform configuration file GCD
    - the Terraform configuration file Azure
    - add getSentry support
    - add Aws Cloudwatch support
    - the Ansible configuration file AWS
    - the Ansible configuration file GCD
    - the Ansible configuration file Azure
    - the Juju configuration file AWS
    - the Juju configuration file GCD
    - the Juju configuration file Azure

