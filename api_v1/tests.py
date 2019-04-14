from task_list.models import Task
from .serializers import TaskSerializer
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api_v1.views import SnippetList
from rest_framework.views import APIView

# client = Client()
#
#
# class GetSingleTaskTest(TestCase):
#     """ Test module for GET single puppy API """
#
#     def setUp(self):
#         self.task = Task.objects.create(
#             name = 'qwerty', about='longtext', expiration_date='2020-12-20', status='Ready',)
#
#
#
#     def test_get_valid_single_puppy(self):
#         response = client.get(
#             reverse('SnippetDetail', kwargs={'pk': self.task.pk}))
#         puppy = Task.objects.get(pk=self.task.pk)
#         serializer = TaskSerializer(puppy)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_puppy(self):
#         response = client.get(
#             reverse('SnippetDetail', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
class AccountTests(APITestCase):

    base_url = 'http://localhost:8000/api/'

    def setUp(self):
        self.task = Task.objects.create(
            id='1', name = 'qwerty', about='longtext', expiration_date='2020-12-20', status='Ready',)

    def test_get(self):
        url = self.base_url+'snippets/'
        params = {'start':0, 'count':1}
        response = self.client.get(url, params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        url = self.base_url+'snippets/'
        data = {'name': 'qwertyu2', 'about': '123456782','img_file': 'test.jpg', 'expiration_date': '2020-12-20', 'status': 'Ready'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_by_id(self):
        url = self.base_url+'snippets/1/'
        response = self.client.get(url, format='json', kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_put_by_id(self):
        url = self.base_url+'snippets/1/'
        data = {'name': 'q', 'about': 'q', 'img_file': 'test.jpg', 'expiration_date': '2020-12-20', 'status': 'Ready'}
        response = self.client.put(url, data, format='json', kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_del_by_id(self):
        url = self.base_url+'snippets/1/'
        response = self.client.delete(url, format='json', kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pic(self):
        url = self.base_url+'upload/jpg'
        files = {'file': open(r'api_v1/test.jpg', 'br')}
        response = self.client.post(url, files)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

