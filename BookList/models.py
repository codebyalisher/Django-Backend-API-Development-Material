from django.db import models

class Category(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=255)
    def __str__(self)->str:
        return self.title

# code for Models and Serializer.
class  MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)#on_delete ka mtlb h k pehly Menuitems dleete hugi us k bd Category ki
    inventory=models.SmallIntegerField() #this code is for the all the separate code of DRF


#code for the Project for the api practicing
'''from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=255,db_index=True)
    def __str__(self)->str:
        return self.title
class MenuItem(models.Model):
    title=models.CharField(max_length=255,db_index=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    featured=models.BooleanField(db_index=True)
    def __str__(self)->str:
        return self.title

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    menuitem=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        unique_together=('user','menuitem')
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_crew=models.ForeignKey(User,on_delete=models.CASCADE,related_name='delivery_crew',null=True,blank=True)
    status=models.BooleanField(db_index=True, default=False)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateTimeField(db_index=True,auto_now_add=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    menuitem=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        unique_together=('order','menuitem')'''