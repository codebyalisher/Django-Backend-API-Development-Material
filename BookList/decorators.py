#Code for https methods and decorators
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

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