from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/rating/', views.movie_rating),
    path('recommendations/', views.recommendations),
]
