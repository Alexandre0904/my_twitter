from django.urls import path
from .views import tweet_list, create_tweet

urlpatterns = [
    path('', tweet_list, name='tweet_list'),
    path('create/', create_tweet, name='create_tweet'),
]
