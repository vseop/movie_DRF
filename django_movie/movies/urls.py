from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'actor', views.ActorsViewSet, basename='actor')
router.register(r'movie', views.MovieViewSet, basename='movie')

urlpatterns = format_suffix_patterns([
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path("review/<int:pk>/", views.ReviewCreateViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
    path("review/my/", views.ReviewCreateViewSet.as_view({'get': 'my_reviews'})),
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),
])
urlpatterns += router.urls



