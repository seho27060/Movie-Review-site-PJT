from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
# Create your views here.

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def follow(request, user_pk):
    you = get_object_or_404(User, pk=user_pk)
    me = request.user
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    serializer = ProfileSerializer(you)
    return Response(serializer.data)
    
