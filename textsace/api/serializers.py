import imp
from api.models import Snippet, Tag

from rest_framework import serializers
from rest_framework_jwt.views import JSONWebTokenSerializer



class JwtTokenSerializer(JSONWebTokenSerializer):
    def is_valid(self, raise_exception=None):
        """
        If raise_exception is unset, set it to True by default
        """
        return super().is_valid(
            raise_exception=raise_exception if raise_exception is not None else True)


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"