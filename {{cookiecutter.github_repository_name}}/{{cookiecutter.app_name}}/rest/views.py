import json

from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from {{cookiecutter.app_name}}.rest.serializers import FileToFilesystemSerializer, UserSerializer


"""
Official drf doc here:
https://www.django-rest-framework.org/api-guide/requests/#authenticators
"""


@api_view(['GET'])
def status_api(request):
    """
    Just return ok for Icinga2 or Nagios. Function based.
    """
    if request.method == 'GET':
        return JsonResponse({'status': 'OK'}, status=200)


class Icinga2API(APIView):
    """
    Just return ok for Icinga2 or Nagios. Class based.
    """
    def get(self, request):
        return Response({'status': 'OK'}, status=200)


class FileAPI(APIView):
    """
    Example API to push a json image on the server and get it by a key.
    """
    def delete(self, request):
        """
        Required that the client is authenticated,
        This method delete a file on the disk (NotImplemented)
        :param request: the key corresponding to that file.
        :return: status
        """
        raise NotImplemented()

    def get(self, request):
        """
        Required that the client is authenticated,
        This method load a file from the disk to the json send it in the
        response
        :param request: the key corresponding to that file.
        :return: the file in json Base64 format
        """
        # http://www.django-rest-framework.org/api-guide/requests/#query_params
        if 'name' not in request.query_params \
                or not request.query_params['name']:
            return Response({'error': 'file Not found'}, status=422)
        else:
            name = request.query_params['name']

        with open(settings.PATH_TO_STORE_FILE + name + '.json') as f:
            json_file = json.load(f)
        return Response(json_file, status=200)

    def post(self, request):
        """
        Required that the client is authenticated,
        This method load a file from the json and save it on the disk
        :param request: the file in json Base64 format
        :return: the key to get to that file after.
        """
        serializer = FileToFilesystemSerializer(
            path=settings.PATH_TO_STORE_FILE, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.instance,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Required that the client is authenticated,
        This method load a file from the json and update it on the disk
        (NotImplemented)
        :param request: the key and the new file in json Base64 format
        :return: the key to get to that file after.
        """
        raise NotImplemented()
