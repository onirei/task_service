from rest_framework import status
from rest_framework.test import APITestCase
from task_list.models import Task


class AccountTests(APITestCase):

    base_url = 'http://localhost:8000/api/'

    def setUp(self):
        self.task = Task.objects.create(
            id='1', name='qwerty', about='longtext',
            expiration_date='2020-12-20', status='Ready',)

    def test_get(self):
        url = self.base_url+'snippets/'
        params = {'start': 0, 'count': 1}
        response = self.client.get(url, params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_400(self):
        url = self.base_url+'snippets/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post(self):
        url = self.base_url+'snippets/'
        data = {'name': 'qwertyu2', 'about': '123456782',
                'img_file': 'test.jpg', 'expiration_date': '2020-12-20',
                'status': 'Ready'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_without_image(self):
        url = self.base_url + 'snippets/'
        data = {'name': 'qwertyu2', 'about': '123456782',
                'expiration_date': '2020-12-20', 'img_file': '',
                'status': 'Ready'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_400(self):
        url = self.base_url+'snippets/'
        data = {'about': '123456782', 'img_file': 'test.jpg',
                'expiration_date': '2020-12-20', 'status': 'Ready'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_by_id(self):
        url = self.base_url+'snippets/1/'
        response = self.client.get(url, format='json',
                                   kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_404(self):
        url = self.base_url+'snippets/99/'
        response = self.client.get(url, format='json', kwargs={'pk': 99})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_by_id(self):
        url = self.base_url+'snippets/1/'
        data = {'name': 'q', 'about': 'q', 'img_file': 'test.jpg',
                'expiration_date': '2020-12-20', 'status': 'Ready'}
        response = self.client.put(url, data, format='json',
                                   kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_by_id_without_image(self):
        url = self.base_url+'snippets/1/'
        data = {'name': 'q', 'about': 'q', 'expiration_date': '2020-12-20',
                'status': 'Ready', 'img_file': ''}
        response = self.client.put(url, data, format='json',
                                   kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_by_id_400(self):
        url = self.base_url+'snippets/1/'
        data = {'name': 'q', 'about': 'q', 'img_file': 'test.jpg',
                'expiration_date': '2020/12/20', 'status': 'Ready'}
        response = self.client.put(url, data, format='json',
                                   kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_del_by_id(self):
        url = self.base_url+'snippets/1/'
        response = self.client.delete(url, format='json',
                                      kwargs={'pk': self.task.pk})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pic(self):
        url = self.base_url+'upload/jpg'
        files = {'file': open(r'api_v1/test.jpg', 'br')}
        response = self.client.post(url, files)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
