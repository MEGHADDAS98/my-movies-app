from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovieListingAPI, UserViewSet, TokenObtainPairView, CollectionViewSet, MovieViewSet, CollectionMovieViewSet, RequestCounterView
from django.urls import path,re_path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('movie-listing/',views.MovieListingAPI.as_view()),
    path('user-view-set/', views.UserViewSet.as_view()),
    #path('token-obtain-pair-view/', views.TokenObtainPairView.as_view()),
    path('collection-view-set/',views.CollectionMovieViewSet.as_view()),
    path('movie-view-set/', views.MovieViewSet.as_view()),
    path('collection-movie-view-set/',views.CollectionMovieViewSet.as_view()),
    
    path('request-counter/',views.RequestCounterView.as_view()),
    



]

urlpatterns=format_suffix_patterns(urlpatterns)
