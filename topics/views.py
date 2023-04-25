from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import logging

from .serializers import TopicsSerializer
from .models import Topics
#  'django' is important other will not work ex: __name__, 'ANY NAME'
logger = logging.getLogger('django')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    topic = request.data # get data from resquest.
    serializer = TopicsSerializer(data=topic)
    serializer.is_valid(raise_exception=True) # auto return 400
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, id):
    instance = get_object_or_404(Topics, pk=id) #Application.objects.get(pk=id)
    app = request.data
    serializer = TopicsSerializer(instance, data=app, partial=True)
    serializer.is_valid(raise_exception=True) # auto return 400
    serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_all_topic(request):
    """
    List all topics
    """
    logger.info("Platform is running FINE")
    logger.warning("Platform is running at risk")
    logger.debug("Platform is running at risk")
    logger.error("Error Platform is running at risk")
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
@permission_classes([IsAuthenticated])
def delete(request, id):
    instance = get_object_or_404(Topics, pk=id)
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)