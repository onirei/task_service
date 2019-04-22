import random
import string
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from task_list.models import Task


from django.utils.datastructures import MultiValueDictKeyError


class SnippetList(APIView):

    def get(self, request, format=None):
        try:
            start = self.request.query_params.get('start')
            count = self.request.query_params.get('count')
            start = int(start)
            count = start + int(count)
        except TypeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        snippets = Task.objects.all()[start:count]
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request,  *args, format=None,  **kwargs):
        try:
            snippet = Task()
            if request.data['img_file'] and request.data['img_file'] != '':
                snippet.image = 'img/'+request.data['img_file']
            serializer = TaskSerializer(snippet, data=request.data)
        except MultiValueDictKeyError:
            serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TaskSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        try:
            if request.data['img_file'] and request.data['img_file'] != '':
                snippet.image = 'img/'+request.data['img_file']
        except MultiValueDictKeyError:
            pass
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FileUploadView(APIView):
    def post(self, request, fileformat, format=None):
        f = self.request.FILES.get('file')
        name = ''.join(random.choice(
            string.ascii_uppercase +
            string.ascii_lowercase +
            string.digits
        ) for x in range(32))
        filename = 'media/img/'+name+'.'+fileformat
        with open(filename, 'bw') as file:
            for chunk in f.chunks():
                file.write(chunk)
        return Response(name+'.'+fileformat, status=status.HTTP_201_CREATED)
