from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .serializers import ArticleSerializer
from .models import Article

# Create your views here.

@csrf_exempt
def list_article(request):

    if request.method == 'GET':
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles, many=True)
       return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
