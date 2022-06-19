# articles/views.py

from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewSerializer, ReivewListSerializer


@api_view(['GET'])
def movie_list(request):

    if request.method == 'GET':
        # review 개수 추가
        movies = Movie.objects.annotate(
            review_count=Count('reviews', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('-vote_average')
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_list_or_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    def review_list():
        reviews = Review.objects.filter(movie_id=movie_pk)
        serializer = ReivewListSerializer(reviews, many=True)
        return Response(serializer.data)

    def review_create():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

            # 기존 serializer 가 return 되면, 단일 review 만 응답으로 받게됨.
            # 사용자가 댓글을 입력하는 사이에 업데이트된 review 확인 불가 => 업데이트된 전체 목록 return
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return review_create()


@api_view(['PUT', 'DELETE'])
def review_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    # def review_detail():
    #     serializer = ReviewSerializer(review)
    #     return Response(serializer.data)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)
        data = {
            'update': f'작성자만 수정할 수 있습니다.'
        }
        return Response(data, status=status.HTTP_304_NOT_MODIFIED)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        data = {
            'update': f'작성자만 수정할 수 있습니다.'
        }
        return Response(data, status=status.HTTP_304_NOT_MODIFIED)
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['GET'])
def genre(request):
    action = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="액션").order_by("?")[:20]
    serializer1 = MovieListSerializer(action, many=True)
    animation = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="애니메이션").order_by("?")[:20]
    serializer2 = MovieListSerializer(animation, many=True)
    horror = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="공포").order_by("?")[:20]
    serializer3 = MovieListSerializer(horror, many=True)
    romance = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="로맨스")[:20]
    serializer4 = MovieListSerializer(romance, many=True)
    sf = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="SF").order_by("?")[:20]
    serializer5 = MovieListSerializer(sf, many=True)
    comedy = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(genre="코미디").order_by("?")[:20]
    serializer6 = MovieListSerializer(comedy, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data, serializer5.data, serializer6.data])


@api_view(['GET'])
def pastyear(request):
    year2000 = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(release_date__gte="2000-01-01", release_date__lte="2009-12-31").order_by("?")[:20]
    serializer1 = MovieListSerializer(year2000, many=True)
    year1990 = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(release_date__gte="1990-01-01", release_date__lte="1999-12-31").order_by("?")[:20]
    serializer2 = MovieListSerializer(year1990, many=True)
    year1980 = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(release_date__gte="1980-01-01", release_date__lte="1989-12-31").order_by("?")[:20]
    serializer3 = MovieListSerializer(year1980, many=True)
    year1970 = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(release_date__gte="1970-01-01", release_date__lte="1979-12-31").order_by("?")[:20]
    serializer4 = MovieListSerializer(year1970, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])


@api_view(['GET'])
def searchyear(request, year):
    print(year)
    movies = Movie.objects.annotate(review_count=Count('reviews', distinct=True), like_count=Count(
        'like_users', distinct=True)).filter(release_date__contains=year).order_by('?')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
