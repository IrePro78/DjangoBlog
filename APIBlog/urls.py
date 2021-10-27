from django.urls import path
from .views import list_article

urlpatterns = [

    path('articles/', list_article),

]