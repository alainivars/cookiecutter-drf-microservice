Build and run the image with Docker
===================================

Build and run with docker-compose::

    docker-compose up

Then login, see API documentation


.. warning:: WORK IN PROGRESS, not existing actually

Build the Docker image::

    docker build -t my-drf -f Dockerfile.drf-microservice .
    docker build -t my-nginx -f Dockerfile.nginx .

Run the container::

    docker network create my-network
    docker run -d --name drf --net my-network -v /app my-drf
    docker run -d --name nginx --net my-network -p "5000:80" my-nginx

If you want to change the port binding, it's here...
