from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie
from .review import ReviewSerializer

User = get_user_model()
# 영화 상세 조회
class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    reviews = ReviewSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'user', 'title', 'original_title', 'reviews', 'like_users', 'overview', 'release_date', 'poster_path', 'vote_average', 'genre')


# 전체 영화 조회
class MovieListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)
    review_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ('pk', 'user', 'title', 'genre', 'review_count', 'like_count', 'poster_path', 'original_title')
