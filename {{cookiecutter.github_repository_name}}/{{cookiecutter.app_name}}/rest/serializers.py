import copy
import json
import uuid

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

    # def create(self, validated_data):
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Token.objects.create(user=user)
    #     return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class FileSerialised:
#     """
#     In case we want to store a list in db
#     """
#     class Meta:
#         model = FileSerialised
#         fields = ('filename', 'header', 'file')


class FileToFilesystemSerializer(serializers.BaseSerializer):
    path = None

    def __init__(self, *args, **kwargs):
        assert 'path' in kwargs and kwargs['path'] is not None, \
            '`path` is a required argument.'
        self.path = kwargs.pop('path', copy.deepcopy(self.path))
        super(FileToFilesystemSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        # data = str(validated_data) #validated_data['file']
        # extension = validated_data['extension']
        filename = str(uuid.uuid1())
        # a way to know if the same file is already stored !!
        # filename = str(hash(validated_data['file']))
        with open(self.path + filename + '.json', 'w') as f:
            json.dump(validated_data, f)
        # In case we want to store a list in db
        # return FileSerialised(filename, extension, data)
        return {'name': filename}

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def to_internal_value(self, data):
        if isinstance(data, dict) and 'file' in data:
            return data
        else:
            raise serializers.ValidationError("'file' is a required field.")

    def to_representation(self, obj):
        return obj.data
