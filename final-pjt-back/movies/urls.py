from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('', views.movies_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/rating/', views.create_rating),
    path('<int:movie_pk>/rating/<int:rating_pk>/', views.rating_update_or_delete),
    path('recommend/', views.recommendation),
]
