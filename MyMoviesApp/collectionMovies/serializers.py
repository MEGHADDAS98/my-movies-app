from rest_framework import serializers
from .models import Collection, Movie, CollectionMovie

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CollectionMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionMovie
        fields = '__all__'

from rest_framework import serializers

class TokenSerializer(serializers.Serializer):
    """
    Serializer for token authentication.
    """
    token = serializers.CharField()