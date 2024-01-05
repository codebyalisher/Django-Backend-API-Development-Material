from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle 
from.throtle import TenCallsPerMinute 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group
#code for Throttling     
@api_view()
@throttle_classes([AnonRateThrottle])
def throtile_check(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes([TenCallsPerMinute])
def user_rate_throttle(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes(IsAdminUser)
def me(request):
    return Response(request.user.email)

@api_view(['POST'])
@throttle_classes(IsAdminUser)
def manager(request):
    username=request.data('username')
    if username:
        user=get_object_or_404(User,username=username)
        managers=Group.objects.get(name='Manager')
        if request.method=="POST":
            managers.user_set.add(user)
        elif request.method=="DELETE":
            managers.user_set.remove(user)
        return Response({'Message':'ok'})
    return Response({'Mesage':'eror'},status.HTTP_400_BAD_REQUEST)