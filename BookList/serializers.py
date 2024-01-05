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
    
    def calculate_tax(self,product=MenuItem):
        return product.price*Decimal('1.1')   
    
    
    
    
    
    '''  
    provided code includes Django models (Category and MenuItem) and corresponding serializers using Django REST Framework (DRF).

Let's break down the key components:

1. Models:
Category Model:
python
Copy code
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
MenuItem Model:
python
Copy code
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title
2. Serializers:
MenuItemSerializer (First Definition):
python
Copy code
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    inventory = serializers.IntegerField()
CategorySerializer:
python
Copy code
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']
MenuItemSerializer (Second Definition):
python
Copy code
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'inventory']

    def calculate_tax(self, product=MenuItem):
        return product.price * Decimal('1.1')
Explanation:
Models (Category and MenuItem): Define the structure of your database tables.

First MenuItemSerializer: A basic serializer class using serializers.Serializer. It specifies how the MenuItem model data should be converted to JSON format. However, it doesn't perform the model-level operations that ModelSerializer does.

CategorySerializer: A ModelSerializer for the Category model, which simplifies the serialization process by automatically handling model-related operations.

Second MenuItemSerializer: A ModelSerializer for the MenuItem model. It includes additional fields (stock, price_after_tax, and category) and a method (calculate_tax) to calculate tax on the price.

Recommendations:
Avoid Duplicate Names:
You have two serializer classes named MenuItemSerializer. This can cause confusion. Consider renaming one of them.

Method Field Correction:
In the calculate_tax method, change Decimal(1,1) to Decimal('1.1').

Consistency in Category Field:
Ensure that the default value (default=1) for the category field in the MenuItem model corresponds to an existing Category record in your database.

Use ModelSerializer for Consistency:
If possible, use ModelSerializer for all your serializers, as it simplifies the serialization process and provides built-in support for model-related operations.

With these considerations, you should have a clearer understanding of how your models and serializers are structured and can work together.
    
    ''' 