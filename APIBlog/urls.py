from django.urls import path
from .views import list_article, article_details

urlpatterns = [

    path('articles/', list_article),
    path('articles/<int:pk>/', article_details),

]