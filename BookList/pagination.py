from rest_framework.decorators import api_view
from django.core.paginator import Paginator,EmptyPage
from BookList.models import MenuItem
from BookList.serializers import MenuItemSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from  rest_framework import status
from rest_framework import generics

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer  
    
#code that can send the serialized  data using decorators,Model Serializer,relationship serializer in DRF   
@api_view(['POST','GET'])
def menu_items(request):
    if request.method=='GET':
        items=MenuItem.objects.select_related('category').all()#by usign the select_related it will load the relation data in single sql call not for every item seprately
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
