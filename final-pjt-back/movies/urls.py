from django.urls import path, include
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/reviews/', views.review_list_or_create),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    path('genre/', views.genre),
    path('pastyear/', views.pastyear),
    path('searchyear/<year>', views.searchyear),
    # path('reviews/<int:review_pk>/comments/', views.create_comment),
    # path('reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # path('nowplayings/', views.nowplaying_list),
    # path('nowplayings/<int:nowplaying_pk>/', views.nowplaying_detail),
    # path('upcomings/', views.upcoming_list),
    # path('upcomings/<int:upcoming_pk>/', views.upcoming_detail),
]
