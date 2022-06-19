from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# popularity의 최저, 최고값

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    vote_average = models.FloatField()
    genre = models.CharField(max_length=50)
    # popularity필드 제거
    # popularity = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    # movie: review(1:N)의 외래키
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # user : review(1:N)의 외래키
    popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
#     user : comment(1:N)의 외래키
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
#     review : comment(1:N)의 외래키
#     content = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

# class Nowplaying(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=100)
#     original_title = models.CharField(max_length=100)
#     overview = models.TextField()
#     release_date = models.CharField(max_length=100)
#     poster_path = models.CharField(max_length=100)
#     vote_average = models.FloatField()
#     genre = models.CharField(max_length=50)

# class Upcoming(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=100)
#     original_title = models.CharField(max_length=100)
#     overview = models.TextField()
#     release_date = models.CharField(max_length=100)
#     poster_path = models.CharField(max_length=100)
#     vote_average = models.FloatField()
#     genre = models.CharField(max_length=50)