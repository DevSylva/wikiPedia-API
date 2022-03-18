from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status
from .serializers import *
import requests
import wikipedia

# Create your views here.
@api_view(['GET'])
def apiRoutes(request):
    routes = [
        'GET /wiki-home-page/',
        'POST /query/',
    ]
    return Response(routes, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def wikiHomePage(request):
    homepage = requests.get("https://en.wikipedia.org/wiki/Main_Page")

    # display status code
    statusCode = homepage.status_code
    # display scrapped data
    pageContent = homepage.content
    print(pageContent)

    data = {
        "statusCode": statusCode,
        "pageContent": pageContent
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([JSONParser])
def query(request):
    if request.method == 'POST':
        serializer = querySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            try:
                q = serializer.data['query']
                result = wikipedia.summary(q, sentences = 2)

                # printing the result
                print(result)
                data = result
                return Response(data, status=status.HTTP_200_OK)
            except e:
                return Response(e, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



