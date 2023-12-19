from rest_framework import  serializers
from.models import MenuItem
from decimal import Decimal
from .models import Category
class MenuItemSerializer(serializers.Serializer):#this class is seprate for the code in DRF
        id=serializers.IntegerField()
        title=serializers.CharField(max_length=255)
        price=serializers.DecimalField(max_digits=10, decimal_places=2)
        inventory=serializers.IntegerField()
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','slug']  
class MenuItemSerializer(serializers.ModelSerializer):#this class code for Model Serializer
#thorugh the below line we cal also create the new field by this way and by using method also in the existing serializer class
    stock=serializers.IntegerField(source='inventory')
    price_after_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    category= CategorySerializer(read_only=True)#we have two optiion for this field either we can shwo the all fields only or can hide this,so we are showing here only#serializers.StringRelatedField()
   
    class Meta:
        model=MenuItem
        fields=['id','title','price','stock','price_after_tax','category','inventory']
    
    #def calculate_tax(self,product=MenuItem):
    #    return product.price*Decimal(1,1)    