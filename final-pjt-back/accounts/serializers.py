from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Review, Movie
from movies.views import like_movie

class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'title', 'content', 'movie')

    like_reviews = ReviewSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    like_movies = MovieSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_reviews', 'reviews', 'like_movies')

