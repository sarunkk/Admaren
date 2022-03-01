from django.shortcuts import render

from api.serializers import JwtTokenSerializer, SnippetSerializer, TagSerializer
from api.models import Snippet, Tag

# Create your views here.
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework.views import APIView


@api_view(('GET',))
def testing(request):
    print('Entheeeelums')
    return Response({"Result": "Somrthing"})


class LoginView(JSONWebTokenAPIView):
    serializer_class = JwtTokenSerializer


class SnippetView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer
    queryset = ''

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Snippet.objects.get(id=pk)


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveAPIView):
    serializer_class = TagSerializer
    queryset = ''

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Snippet.objects.get(id=pk)