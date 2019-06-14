[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.png?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}})
[![PyPI version](https://badge.fury.io/py/{{cookiecutter.github_repository_name}}.svg)](https://badge.fury.io/py/{{cookiecutter.github_repository_name}})
[![Documentation Status](https://readthedocs.org/projects/{{cookiecutter.github_repository_name}}/badge/?version=latest)](http://{{cookiecutter.github_repository_name}}.readthedocs.io/en/latest/?badge=latest)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg)](http://isitmaintained.com/project/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}} "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg)](http://isitmaintained.com/project/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}} "Percentage of issues still open")
[![Coverage Status](https://coveralls.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}/badge.svg?branch=master)](https://coveralls.io/github/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}?branch=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPi wheel](https://pypip.in/wheel/drf-microservice/badge.svg)](https://pypi.python.org/pypi/drf-microservice/)


# About {{cookiecutter.github_repository_name}}
{{cookiecutter.description}}. 
Don't hesitate to submit a pull request and contribute.

### Releases Notes
    - 0.7.0: restore original struct and move cookiecutter in cookiecutter-drf-microservice
    - 0.6.1: Update dependencies 
    - 0.6.0: start to productionize and add cookiecutter 
    - 0.5.2: fix dendencies security alert
    - 0.5.1: fix some document presentation on github and pypi
    - 0.5.0: Initial publication version

### AWS secret required
```shell
{{cookiecutter.capitalized_var_name}}_USERNAME_PASSWD => a client API password
SECRET_KEY => the secret key
```
### ENV required
```shell
AWS_REGION_NAME => default="eu-east-1"
AWS_{{cookiecutter.capitalized_var_name}}_SECRET_NAME =>The name of the secret bucket
```
## To install
todo
```shell
git clone xxx
cd xxx
python3 -m venv /pass_to/venv/{{cookiecutter.github_repository_name}}
```
- for bash, zsh
```shell
source /pass_to/venv/{{cookiecutter.github_repository_name}}/bin/activate
```
- for fish
```shell
source /pass_to/venv/{{cookiecutter.github_repository_name}}/bin/activate.fish
```
python setup.py test
python manage.py migrate
```
- for bash, zsh
```shell
SECRET_KEY=my_secret_key python manage.py test
```
- for fish
```shell
/usr/bin/env SECRET_KEY=my_secret_key python manage.py createsuperuser
```
- then run it
```shell
SECRET_KEY=my_secret_key python manage.py runserver
```
- if you have any problem or you want enable the debug mode
```shell
ENABLE_DEBUG=1
```


## API
To see the documentation for the API
In development mode, login at
```shell
curl --request POST \
  --url http://127.0.0.1:8000/rest-auth/login/ \
  --header 'authorization: Basic YWRtaW46YWRtaW4=' \
  --header 'content-type: application/json' \
}'
```
Actually the default mode is "development" (same to the state of this project)
in that mode a default login is the the db with username='admin' password='admin'
you will get back in return your token.
 
Then open 
```web
http://127.0.0.1:8000/docs/
```
## testing
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
DJANGO_SETTINGS_MODULE={{cookiecutter.github_repository_name}}.config.local SECRET_KEY=my_secret_key pytest
```

## Security check
Before dockerization for deployment to production, don't forget to check if by
```shell
SECRET_KEY=my_secret_key python manage.py check --deploy 
```
### Build and run the image with Docker

#### Build the Docker image:
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

### DONE

    - support basic auth removed
    - support token auth
    - endpoint json file POST,GET
    - endpoint login/logout
    - endpoint get tocken

### TODO
    - AWS ssm secret and Kms
    - add getSentry support
    - endpoint json file DELETE, PUT?
    - add some strong auth
    - create differents version:
        - S3
        - RDS
        - postgreSQL
        - Redis
        - Aerospike
        - ... 

#### for different use-case
    - create the docker-image file
    - create the ansible file
    - create the terraform file
    - create the kubertes file
    - create the Juju file

