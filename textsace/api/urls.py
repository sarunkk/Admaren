from django.contrib import admin
from django.urls import path, include

from api.views import testing, LoginView, SnippetView, SnippetDetailView, TagListView, TagDetailView

urlpatterns = [
    path('test',testing,name='testing'),
    path('login',LoginView.as_view(),name='login'),
    path('snippets',SnippetView.as_view(),name='snippets'),
    path('snippets/<int:pk>/',SnippetDetailView.as_view(),name='snippets_detail'),
    path('tags',TagListView.as_view(),name='tags'),
    path('tags/<int:pk>/',TagDetailView.as_view(),name='tags_detail'),

]
