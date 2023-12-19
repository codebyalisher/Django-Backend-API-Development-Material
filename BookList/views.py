#Code for https methods and decorators
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
#code for Serializer Performing the CRUD operations using Models in DRF
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.core.paginator import Paginator,EmptyPage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle 
from.throtle import TenCallsPerMinute 

@api_view(['GET','POST','PUT','DELETE'])
def books(request):
    return HttpResponse('list of the books',status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self,request):
        author=request.GET.get('author')
        if author:
            return Response({'message':'list of the books by'+author},status.HTTP_200_OK)
        return Response({'message':'list of the books'},status=status.HTTP_200_OK)
    def post(self,request,pk):
        return Response({"title":request.data.get('title')},status.HTTP_201_CREATED)
#code to access the single entity like a book here  
class Book(APIView):
    def get(self,request,pk):
        return Response({'message':'single book by id'+str(pk)},status.HTTP_200_OK)
    def put(self,request,pk):
        return Response({"title":request.data.get('title')},status.HTTP_200_OK)

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer    
 
#code that can send the serialized  data using decorators,Model Serializer,relationship serializer in DRF
@api_view()
def menu_items(request):
    items=MenuItem.objects.select_related('Category').all()#by usign the select_related it will load the relation data in single sql call not for every item seprately
    serialized_items=MenuItemSerializer(items,many=True)
    return Response(serialized_items.data)

@api_view()
def single_item(request,id):
    #items=MenuItem.objects.get(pk=id)
    items=get_object_or_404(MenuItem,pk=id)
    serialized_items=MenuItemSerializer(items)
    return Response(serialized_items.data)

#code for  the Pagination,Administration,Throttling
@api_view(['POST','GET'])
def menu_items(request):
    if request.method=='GET':
        items=MenuItem.objects.select_related('category').all()
        category_name=request.query_params.get('category')
        to_price=request.query_params.get('price')
        search=request.query_params.get('search')
        ordering=request.query_params.get('ordering')
        perpage=request.query_params.get('perpage',default=2)
        page=request.query_params.get('page',default=1)
        if category_name:
            items=items.filter(category__title=category_name)
        if to_price:
            items=items.filter(price__lte=to_price)#here lte is conditional field locator,if we want to find the exact price,we can do this as price=price
        if search:
            items=items.filter(title__icontains=search)#this will search on the base of the provided characters to make case sensitive ttitle__istartswith=search,to serach in the title use the title__contains=search but to make casesensitive then title__icontains=search
        if ordering:
            ordering_fields=ordering.split(',')#filtering is being done comparing two fields on the behalf of ordering
            items=items.order_by(ordering_fields)
        paginator=Paginator(items,per_page=perpage)
        try:
            items=paginator.page(number=page)
        except EmptyPage:
            items=[]
        serialized_items=MenuItemSerializer(items,many=True)
        return Response(serialized_items.data)
    if request.method=='POST':
        serialized_items=MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data,status.HTTP_201_CREATED)

@api_view()
def single_item(request,id):
    items=get_object_or_404(MenuItem,pk=id)
    serialized_items=MenuItemSerializer(items)
    return Response(serialized_items.data)

@api_view()
@permission_classes(IsAuthenticated)
def secret(request):
    return Response({'Message':'save secret message'})

@permission_classes(IsAuthenticated)
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'Message':'This Manager should see message only'})
    else:
        return Response({'Message':'you are not authorized'})

     
@api_view()
@throttle_classes([AnonRateThrottle])
def throtile_check(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes([TenCallsPerMinute])
def user_rate_throttle(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes()
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