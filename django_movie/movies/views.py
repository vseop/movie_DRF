from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from rest_framework import generics

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, \
    CreateRatingSerializer
from .service import get_client_ip


class MovieListView(APIView):
    """Вывод списка фильмов"""

    def get(self, request):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(request)))
        ).annotate(
            middle_star=(models.Avg("ratings__star"))
            # middle_star=models.Sum(models.F('ratings__star'))/models.Count(models.F('ratings'))
        )
        #     rating_user=models.Case(
        #         models.When(ratings__ip=get_client_ip(request), then=True),
        #         default=False,
        #         output_field=models.BooleanField()
        #     ),
        # )
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Добавление отзыва к фильму"""

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStarRatingView(APIView):
    """Добавление рейтинга фильма"""

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


class Mo(generics.GenericAPIView):
    pass