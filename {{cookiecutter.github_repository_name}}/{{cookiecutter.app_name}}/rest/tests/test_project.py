import json
import unittest

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from {{cookiecutter.app_name}}.rest.tests.base import BaseTestCase


class ViewTestCase(BaseTestCase):
    """
    Test suite for the api views.
    Infos: Lot of help at
    https://www.django-rest-framework.org/api-guide/testing/#apiclient
    """

    def setUp(self):
        """Define the test client and other test variables."""
        # self.path = reverse('rest_login')
        self.username = "my_user"
        self.password = "my_passwd"
        self.user = User.objects.create(
            username=self.username, password=self.password)
        # Initialize client and force it to use authentication
        self.client = APIClient()
        # self.client.force_authenticate(
        #     user=self.user, token=self.user.auth_token)
        # self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_access_with_correct_credential(self):
        response = self.basics_auth_get(
            reverse('icinga'),
            username=self.username,
            password=self.password
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_with_correct_token(self):
        response = self.token_auth_get(
            reverse('icinga'),
            str(self.user.auth_token)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_docs(self):
        response = self.client.get('/docs/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_file_with_credential_good_key(self):
        with open('./{{cookiecutter.app_name}}/rest/tests/files/file_ok.json') as f:
            file_content = f.read()
            json_file_content = json.loads(file_content)
        response = self.basics_auth_post(
            reverse('api_file'),
            self.username,
            self.password,
            data=json_file_content
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = dict(response.data)
        response = self.basics_auth_get(
            reverse('api_file'),
            self.username,
            self.password,
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, json_file_content)

    def test_api_file_with_credential_wrong_key(self):
        with open('./{{cookiecutter.app_name}}/rest/tests/files/file_ko.json') as f:
            file_content = f.read()
            json_file_content = json.loads(file_content)
        response = self.basics_auth_post(
            reverse('api_file'),
            self.username,
            self.password,
            data=json_file_content
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], "'file' is a required field.")

    def test_api_file_with_token_good_key(self):
        with open('./{{cookiecutter.app_name}}/rest/tests/files/file_ok.json') as f:
            file_content = f.read()
            json_file_content = json.loads(file_content)
        response = self.token_auth_post(
            reverse('api_file'),
            str(self.user.auth_token),
            data=json_file_content
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.data
        response = self.token_auth_get(
            reverse('api_file'),
            str(self.user.auth_token),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, json_file_content)

    def test_api_file_with_token_wrong_key(self):
        with open('./{{cookiecutter.app_name}}/rest/tests/files/file_ko.json') as f:
            file_content = f.read()
            json_file_content = json.loads(file_content)
        response = self.token_auth_post(
            reverse('api_file'),
            str(self.user.auth_token),
            data=json_file_content
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], "'file' is a required field.")

    def test_icinga2(self):
        response = self.basics_auth_get(
            reverse('icinga'),
            self.username,
            self.password
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
