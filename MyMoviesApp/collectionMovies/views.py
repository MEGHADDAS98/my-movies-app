from django.shortcuts import render

# Create your views here.
from django.db import models
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,request
from .models import RequestCounter,Collection,CollectionMovie,Movie
from .serializers import CollectionSerializer,CollectionMovieSerializer,MovieSerializer,TokenSerializer
from rest_framework.permissions import AllowAny
import jwt
from .views import *



class HomeView(APIView):
    def get(self, request):
        return HttpResponse("Welcome to your Movie-Collection-APP!")


# Integrate with movie listing API
class MovieListingAPI(APIView):
    def get(self, request):
        response = request.get(
            'https://demo.credy.in/api/v1/maya/movies/',
            auth=(settings.MOVIE_API_USERNAME, settings.MOVIE_API_PASSWORD)
        )
        if response.status_code == 200:
            movies = response.json()
            return Response(movies)
        else:
            return Response(status=response.status_code)

# Implement APIs for your web application
class UserViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Both username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        # token, _ = Token.objects.get_or_create(user=user)

        # return Response({"access_token": token.key}, status=status.HTTP_201_CREATED)
        payload = {'user_id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({"access_token": token}, status=status.HTTP_201_CREATED)

# class TokenObtainPairView(ObtainAuthToken):
#     serializer_class = TokenSerializer
    


class CollectionViewSet(APIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_top_favorite_genres():
    # Get all movies from the database
        movies = Movie.objects.all()

    # Create a dictionary to store the genres and their counts
        genre_counts = {}

    # Iterate over each movie and increment the count of its genre
        for movie in movies:
            genre = movie.genre
            if genre not in genre_counts:
                genre_counts[genre] = 1
            else:
                genre_counts[genre] += 1

        # Get the top 3 genres with the highest counts
        top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:3]

        # Return the top 3 favorite genres
        return top_genres
    

    def get(self, request):
        collections = Collection.objects.all()
        favorite_genres = get_top_favorite_genres()  # Implement logic to get top 3 favorite genres
        serialized_collections = CollectionSerializer(collections, many=True).data
        return Response({"collections": serialized_collections, "favourite_genres": favorite_genres})
    

class MovieViewSet(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    queryset = CollectionMovie.objects.all()
    serializer_class = CollectionMovieSerializer

    def put(self, request, collection_uuid):
        collection_movie = self.get_object(collection_uuid)
        serializer = CollectionMovieSerializer(collection_movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, collection_uuid):
        collection_movie = self.get_object(collection_uuid)
        serializer = CollectionMovieSerializer(collection_movie)
        return Response(serializer.data)

    def delete(self, request, collection_uuid):
        collection_movie = self.get_object(collection_uuid)
        collection_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, collection_uuid):
        try:
            return CollectionMovie.objects.get(uuid=collection_uuid)
        except CollectionMovie.DoesNotExist:
            raise Http404

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.counter = RequestCounter.objects.get_or_create(counter=0)[0]
        response.counter.increment()
        return response

class RequestCounterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'requests': RequestCounter.objects.get().counter})

    def post(self, request):
        RequestCounter.objects.get().reset()
        return Response({'message': 'request count reset successfully'})


def middleware(get_response):
    def middleware_view(request):
        response = get_response(request)
        response.counter = RequestCounter.objects.get_or_create(counter=0)[0]
        response.counter.increment()
        return response
    return middleware_view

