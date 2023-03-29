from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import status

from .serializers import TopicsSerializer
from .models import Topics


@api_view(['POST'])
def create(request):
    topic = request.data # get data from resquest.
    if len(topic["title"]) < 5:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = TopicsSerializer(data=topic)
    serializer.is_valid(raise_exception=True) # auto return 400
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    instance = get_object_or_404(Topics, pk=id) #Application.objects.get(pk=id)
    app = request.data
    serializer = TopicsSerializer(instance, data=app, partial=True)
    serializer.is_valid(raise_exception=True) # auto return 400
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def index(request):
    """
    List all topics
    """
    topics = Topics.objects.all() # query database.
    serializer = TopicsSerializer(topics, many=True) # format data
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def detail(request, id):
    """
    Return topic detail
    """
    old = get_object_or_404(Topics, pk=id)
    serializer = TopicsSerializer(old) 
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
    instance = get_object_or_404(Topics, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)