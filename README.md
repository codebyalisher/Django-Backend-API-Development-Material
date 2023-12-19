'''
API complete notes with detail: 
What is API?
It stands for application programming interface.it is used to connect the front end to the backend by sending and receiving the data.
What are HTTP:
It stands for hyper text transfer protocol.This communication protocol is widely used to send /receive the data over internet.
HTTP AND HTTPS How works:when we search the webpage,images.send the form ,data is submitted over internet using http or secured version of it which is https .To communicate over http requires two parts one is client submits the request and other is the server which responses this request.When security is necessary we use the https not http bcz in https data is first encrypted by client side and then this is decrypted by server so no third party can access this data but in http a third party can access the data over net.
HTTP Methods:also called verbs,there are 5 to access the data over http GET(retrieve the data),POST(use to send the data to sever and create the record),PUT(it updates the whole record),PATCH(to update the partially update the data),DELETE(to delete the record).
HTTP requests:it consists of different types of information encoded by a browser to send the information. A typically request includes the following:version type,url/path,http method, http request headers(these contains some extra information i.e. cookie,referer) and http body(optional)  it contains our actual data that we sent ,Http Response(it contains also extra information like content type,length,headers,time,status code)this is the information that displays on the browser.
Status Code:These Provide the Useful information about the request and response process.Some are here:
100-199informational,
200-299successful,
300-399redirection,
400-499client error,this is happen when client make a bad request or when resource is not on the server.
500-599server errorthis is done on server when it let check the error issue,configuration mismatch,package dependencies issues.
Some status code is used for displaying the different messages i.e. GET 200content found,Put 200updated successfully etc.DELETE 200deleted successfully .
Some most common code that are mostly used:(200,201),(303,304),(400,401,403,404),500.
What is RESTfulness:
REST is the architechure  style to design the API,so it is mostly called restapi bcz it is made through the architechure of REST and it is very popular among the developer to design and implement is very easy.It provides an easy way to communicate with the server to perform the send/receive and others operations like CRUD on server.
API would be said RESTful API if it contains the client-server architechure ,stateless(no prior info about client to make api request or not to remember the previous request) and should be cacheable(it should stroed the responses on the server or on any machine,it reduces the server load and reduce time),should be layered(it should consists on layers through which any layer can remove any tme),uniform interface(unique urls,unified display format i.e.json,xml),provide code on demand.
Resources:This means who want to access the app and so resource type will be according to that which api will be called i.e.if manager wants to know the orders detail the resource type will be orders object,for customer It will be customer object ,for deliver it will be deliver object and so on.
Naming Conventions:The end points of the Api should be valueable so it can make sense .1-always try keep lower case,meaningful word easy to read,write  2-if api accepts the variable for example userid or orderid then use the camelCase and keep them in the curly braces {userId},{orderId} etc./api/order/{orderId}/menu-item.3-Forward slash-if project has the related objects then should use the forward slash in the api to indicate their hierarchical relationship i.e.librarybooksauthor.
To get the particular book of author we can use the api end points as :/library/books/{bookId or can use the authorName}/author.
Noun:should give the object a proper noun i.e.for books it should be /books/{booksId},or /book/{bookId},avoid to retrieve the objects using the verbs as /getAllBooks or /getUser this is wrong.
Always remember you should use the http methods to upate or delete or others method not word in the api like this /api/books/delete.
Also don’t use the displaying data format in the api endpoint like /api/books.json or xml so do this /api/books?format=json.

What is Django Rest Framework( DRF)?
ANS: it is a toolkit built from top of Django web framework and we can create API with much more efficiently bcz it work as: DATABASEDRFCLIENT,mean DRF receive the data from the database and display to the client and get the data from client and save it to the database.
How to use the DRF IN THE PROJECT?
Install using the commandpipenv/pip install djangorestframework,and configure it in the settings.py file under the installed_app option as ‘rest_framework’. 
Q:why some apps are added and some not in the installed-app in the settings.py file
Ans: In a Django project, adding packages to the INSTALLED_APPS list in the settings.py file is necessary when incorporating third-party applications or custom-built apps.
The reason some packages are added while others aren't stems from the nature of the app. Generally, only applications that need to be recognized by the Django framework, such as those responsible for providing models, views, templates, or middleware, are added to the INSTALLED_APPS list.
For instance, when adding a new app, it needs to be placed in the INSTALLED_APPS list to ensure its models are recognized by Django's ORM, its templates are discoverable, and its admin site configurations are integrated.
On the other hand, certain packages or modules don't need to be added to the INSTALLED_APPS list due to their nature. These can include utility libraries, helper functions, standalone scripts, or non-Django related components that don't require integration into the Django framework.
In essence, the INSTALLED_APPS list is reserved for components that have a direct impact on the functionality and structure of the Django project.
A-Separate Code: 
Decorators:  These give browsable api view coming from drf and with other Http’s methods option that which function should support and can data send in json without other tools postman or insomnia.These also can handle the throttling and rate limiting and authenticate the end points
Open view file in the subapp ,As here :
from rest_framework.decorators import api_view
@api_view(['GET','POST','PUT','DELETE'])
def books(request):
    return Response('list of the books',status=status.HTTP_200_OK)

Using Http: it return the response in the plain text format and it uses http from native django.http package that Is the main difference between it and decorators.
As here:
from django.http import HttpResponse
def books(request):
    return HttpResponse('list of the books',status=status.HTTP_200_OK)
Function based views and class based views: in class ,less code is written,less code duplication,extend and add the features,methods for http request types.it is only for get but for other just change the name rest will be same ,we can make multiple mehtods.as here 
class BookList(APIView):
    def get(self,request):
        return Response({'message':'list ofthe books'},status=status.HTTP_200_OK)
and set the url/path of this class in the urls.py file as 
from django.urls import  path
from.import views
urlpatterns=[
    #path('books/',views.books),
    path('books',views.BookList.as_view())
    ]

 In function ,easy to implement,offer better readability,easier to use the decorators,write  once-off solution quickly.its implementation Is above given.
Q:How to do if the client want the book of the specific author through request as https://127.0.0.1:8000/api/books?author=auth_name:
class BookList(APIView):
    def get(self,request):
        author=request.GET.get(‘author’)
        if(author):
            return Response({‘message’:’list of the books by’+author),status.http_200_ok)
        return Response({'message':'list of the books'},status=status.HTTP_200_OK)
Payload:common term for json data or urlencoded data send to the api.as in content option {‘auth’:’ali’},its json data format.
How to accept the Primarykey in the methods of the class based view:here is the code for this;also map this Book class in the urls.py file for setting   the route;localhost:api/book/1
class Book(APIView):
    def get(self,request,pk):
        return Response({'message':'single book by id'+str (pk)},status.http_200_ok)
this is through get method but it is different in put and others methods ,this is a code to access the single entity which is book here as: 
    def put(self,request,pk):
        return Response({"title":request.data.get('title')},status.HTTP_200_OK)
Django-debug-toolbar:this toolbar is used for debugging the api and endpoints and many more.To install this toolbar run this command pipenv Django-debug-toolbar in the terminal in the vs code and add it in the setting .py file in the installed apps option as ‘debug_toolbar’. And then set it as a path in the main app under as:
# settings.py

INSTALLED_APPS = [
    # ...
    'debug_toolbar',
    # ...
]

MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]
Configure Internal IPs:

To restrict access to the debug toolbar, add the following to your settings.py. This step is optional but recommended for security reasons:

# settings.py

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
Configure Debug Toolbar:

Add the following to your settings.py to configure the debug toolbar:

# settings.py

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}
Include Debug Toolbar URLs:

Update your project's urls.py to include the debug toolbar URLs only when the project is in debug mode:

# urls.py
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include('BookList.urls')),
    #path('auth/',include('djoser.urls')),    
    #path('auth/',include('djoser.urls.authtoken')),
    #path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    #path('api/token',TokenRefreshView.as_view(),name='token_refresh'),
    #path('api/token/blacklist/',TokenBlacklistView.as_view(),name='token_blacklist')    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

INTERNAL_IPS=["127.0.0.1"]

Pyhton manage.py makeimigrations and python manage.py migrate
After these settings the toolbar will show in the browser.and explore all the options of the toolbar.
B-Seprarte Code:
CRUD(Create,Read,Update,Delete) operations on the data:
To Perform These Operations ,lets create the model
In the subapp models.py file ,as:
from django.db import models

# Create your models here.
class  MenuItem(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.SmallIntegerField()
       
Serializer: that converts these models instances into python object data type which can be displayed in any format like json,xml etc.It also helps in converting the http request body into python data object and mapped them into model instances,Mean model instances/data can be convert into json and that json then can be converted into models instances.To do this,first create the model as above is created and then convert this model into the serializer using generics and serializer as in the code:
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
and set the path for thisMenuItemsView class as here in the code in the subapp urls.py file under urlpattern option:
path('menu-items',views.MenuItemsView.as_view())

this class will display the all items by creating the lis of the objects using generics.listcreateapiview class,to display the only one item we will use the generics.updateview which has everything to receive the record and to update the value,also generics.destroyapiview class which has everything to receive the record and then delete the data as here in the code and this class wil be set in the path:
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

path in the urls.py subapp file  as :
 path('menu-items/<int:pk>',views.SingleMenuItemView.as_view())
C-Separate Code:
Q:How Serializers Functions/works in DRF :
Data is composed from database using Django-models/objects and then data is serialized and then is presented to the client,this is called Serialization .And similar data of client is composed using Django-model/objects and then serialized and then saved to the database This is called Deserialization ,this is the reverse in working.its explaination is given above also.This is done to make the data more readable ,clean and consist into different formats like json,xml and others.
Serialized Data can also send using the Decorators of DRF as here in the code:
#code that can send the serialized  data using decorators 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import MenuItem
@api_view()
def menu_items(request):
    items=MenuItem.objects.select_related('Category').all()#by usign the select_related it will load the relation data in single sql call not for every item seprately

    return Response(items.values())
The serializer fields are similar as in model.We can show all the data or can hide the some data from displaying.this serializer showing all the data.
similar we can show the single item as here in the code: 
@api_view()
def single_item(request,id):
    items=MenuItem.objects.get(pk=id)
    serialized_items=MenuItemSerializer(items)
    return Response(serialized_items.data)
and also add the path for this single item/data in the subapp urls.py file as ,we will get the id if it is already in the database.
Q:What if visiting non existing id:
To overcome this error,convert into user friendly error  as in the code:
from django.shortcuts import get_object_or_404
@api_view()
def single_item(request,id):
    #items=MenuItem.objects.get(pk=id)
    items=get_object_or_404(MenuItem,pk=id)
    serialized_items=MenuItemSerializer(items)
    return Response(serialized_items.data)

Model Serializer:this also works same as the above work but it has a short code,so code for this is here:
from.models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['id','title','price','inventory']
Relationship Serializer:in database we have multiple tables to establish the relationship among them ,we need models to connect them one by one,we already know the DRF serialzer,
It shows the related data of connected models ,mean we can show the multiple tables In a single query or at once together.
This Serializer converts the models into json correctly,this is the models.py file code for all the above codes ,also migrate before deletion
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
    inventory=models.SmallIntegerField()
To show the category using relationship serializer in DRF in serializer.py file add this line of code  which is category below the price_after_tax:
class MenuItemSerializer(serializers.ModelSerializer):
#thorugh the below line we cal also create the new field by this way and by using method also
    stock=serializers.IntegerField(source='inventory')
    price_after_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    category=serializers.StringRelatedField()
    class Meta:
        model=MenuItem
        fields=['id','title','price','stock','category']
    
    def calculate_tax(self,product=MenuItem):
        return product.price=Decimal(1,1)  

Separate Serializer for category to  make it more detailed,to do this open the serializer.py file 
Make the class for CategorySerilizer and  then call this in the Menutitemserilzer class by replacing the category field by calling the Categoryserilizer class as in the code:
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','title','slug']    
class MenuItemSerializer(serializers.ModelSerializer):#this class code for Model Serializer
#thorugh the below line we cal also create the new field by this way and by using method also
    stock=serializers.IntegerField(source='inventory')
    price_after_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    category= CategorySerializer()#replacing serializers.StringRelatedField()
    category_id=serializers.IntegerField(write_only=True)# to not show this field in the get request
Deserialization and Validation:
Deserialization is the opposite of serialization mean when client send the data to the end point of the api and DRF map that data to the exisiting  model,
We have to check the request before processing it ,if it is get then retrieve the record otherwise create new record and save it using deserialization process.it shows how to validate the input data and then map it to an existing model using validation and deserialization process in DRF.
Renders:these are responsible for  displaying  data in json,xml ,html and yaml as per clients want.
There are built in Renders(jsonRender,browsableapiRender,xmlRender) and also Third Party Renders(xmlRender,yamlRender,jsonpRender).
As I.e. rest_framework.renders.JsonRender ;rest_framework.renders.BrowsableApiRender.
How to use them?
In http request under Header option  and in accept option ,write this line as Accept:application/json.
Also add this piece fo code in the settings.py file as:
REST_FRAMEWORK={
    'DEFAULT_RENDERER_CLASSED':[
        'rest_framework.renders.JSONRender',
        'rest_framework.renders.BrowsableAPIRender',
         ‘rest_framework_xml.renders.XMLRender’
    ]
}
browsableapirender only works when accept header set to text/html but if this is not set then browser display the data by default in the json format.To use the xml format ,install first by using command from terminal aspipenv install djangorestframework-xml or you can use the pip instead of pipenv. And then add this in the above code below the browsableapirender as’rest_framework_xml.renders.XMLRender’ ,also in header method write the Accept:application/xml.
Filtering and Searching:
Filtering is the process of getting the subset/subcategory of the main items as the result to the client on the browser on the base of some criteria from API. i.e main items ->food and subitems can be pizza,appetizer etc .
Two ways to present the menu items that client wants the subset as a result i.e.all the menu items for the appetizer or dessert category.
1-display all the items with their names to the client ,then client himself process the data and manage the all kind of filtering .
2-Process the conditions on the server and display the result on the base of criteria.
These both have the Pros and Cons,1-First approach can be used as a easy way bcz in less time we can make the api for certain limit but it is not sustainable more than limit bcz it will make load on the server for much limit and it is not sensible.
2-second approach will take time to develop but will have more advantages like making the less load on the server and reducing less time for client display bcz all the filtering is done on the server side. 
Client can filter through passing the query as http://localhost:8000/api/menu-items/?category=main to search the main items.         OR http://localhost:8000/api/menu-items/?category=icecream to search the subset/subitem          OR    http://localhost:8000/api/menu-items/?to_price=3 can be search  by price OR   http://localhost:8000/api/menu-items/?category=main&to_price=3 can be search by using both 
@api_view(['POST','GET'])
def menu_items(request):
    if request.method=='GET':
        items=MenuItem.objects.select_related('category').all()
        category_name=request.query_params.get('category')
        to_price=request.query_params.get('price')
        if category_name:
                            items=items.filter(category__title=category_name)#catogry__titlethis belong to the category model and linked to the linked model,so we have to use the double underscore i.e. __ btween fields and model fields to filter the linked model.For Regular fields we use the field name to filter.
        if to_price:
            items=items.filter(price__lte=to_price)#here lte is conditional field locator,if we want to find the exact price,we can do this as price=price
        serialized_items=MenuItemSerializer(items,many=True)
        return Response(serialized_items.data)
Imp to Remember in the above code: catogry__titlethis belong to the category model and linked to the linked model,so we have to use the double underscore i.e. __ btween fields and model fields to filter the linked model.For Regular fields we use the field name to filter.
here lte is conditional field locator,if we want to find the exact price,we can do this as price=price
Searching: let if client have to search the items using the characters passed as a parameter in the request i.e.    http://localhost:8000/api/menu-items/?search=chocolate and will return all the items starting with the chocolate    as here in the code :
@api_view(['POST','GET'])
def menu_items(request):
    if request.method=='GET':
        items=MenuItem.objects.select_related('category').all()
        category_name=request.query_params.get('category')
        to_price=request.query_params.get('price')
        search=request.query_params.get('search')
        ordering=request.query_params.get('ordering')
        if category_name:
            items=items.filter(category__title=category_name)
        if to_price:
            items=items.filter(price__lte=to_price)#here lte is conditional field locator,if we want to find the exact price,we can do this as price=price
        if search:
            items=items.filter(title__startswith=search)#this will search on the base of the provided characters to make case sensitive title__istartswith=search, but if we have to search in the title then title__contains=search but to  make case sensitive then title__icontains=search
         if ordering:
            ordering_fields=oredering.split(‘,’)#to filter the order on the base of two fields
            items=items.order_by(ordering_fields)
        serialized_items=MenuItemSerializer(items,many=True)
        return Response(serialized_items.data)
    if request.method=='POST':
        serialized_items=MenuItemSerializer(data=request.data)
        serialized_items.is_valid(raise_exception=True)
        serialized_items.save()
        return Response(serialized_items.data,status.HTTP_201_CREATED)


Ordering:to  search on the base of order as Ascending and Descending upon string query/request.
There is a Django package which provides advance searching,filtering and ordering name is Django-filter.
To install it use the commandpipenv install Django-filter in the vs code terminal .it is mostly used with class based views. But we can also take the native advantage of filtering using function based views.
http://localhost:8000/api/menu-items?ordering=price   ,ordering by comparing two fields  as here:
http://localhost:8000/api/menu-items?ordering=price,inventory, for both to show one in ascending and other in descending or then same process will be as in below line is described and by putting minus in any of them then the order of that will be change in the above url.
default it display in descending order but can also be shown in ascending order by putting  - before price as Here:http://localhost:8000/api/menu-items?ordering=-price  now it will be in the ascending order
I have added the ordering code in the above provided code .we can also do for two fields on the behalf of these fields filtering is done ,code is also above added.
Pagination: To enable API to send the results in the smaller chunk.imagine there are 1000 orders in the database and if there is no pagination then It will get all the result this will put huge load on the server for the necessary operations and also waste bandwidth,to avoid actually client needed 10 latest orders.Developers use pagination to chunk results,client application then decide the page numbers and how many records they want per page.i.e. client request records 7-8 using get http normal end point as:
/api/menu-items?perpage=2&page=4 ->this will show that each 4 pages with 2 record,but there is useful tip that always use minimum record on the page for security measure to prevent the piece of api end points.if we set the limit=10 per page for the api end points but clients requests 20 records ranging from 30 to 40 then client needs two calls to make this ,first api calls as/items?perpage=10&page=310results with records 21 to 30 and second calls perpage=10&page=410 records 31 to40 ,but what if client request50 in one single call api as perpage=50&page=7for such request we can show the message of 400=bad Request error as in the code:import the paginator and emptypage from Django use it by try and except block.
from rest_framework import  status
from django.core.paginator import Paginator,EmptyPage
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

Caching:sends saved result instead of creating one,this will minimize the load on the server and also reduce the time for responding.As RESTful API is based on the layered arechitechure ,so Caching also works on many layers.lets explore  http request flow in typically layered api infrastructure as:
Visitor firewallreverse proxy serverweb serverdatabase server,explanation for this as:
Visitor visit the domain and sends the request to the firewall and then goes to the reverse proxy server that sits in the front of web server,this transforms the call to the web server and then this connect to the database server, the database server prepare the response and sends back to the web server and so on up till to the visitor this response reached. Caching is done in the reverse server ,web server and database server, Lets explore these in details:
1-Caching on atabase server protect the excessive read-write operation in the storage.typically they use the query cache with sql query and query results stored in the memory,they provide the results from the memory until there is no change happening in the fields of sql ,they served the result from the memory instead of running the new query against the real world data.This will reduce the processing power and time.But depends only on database server is bad idea bcz the server-side scripts  still connect to  it to get the cached results and for given the amount of RAM AND CPU ,database engine can only accepts the fixed number of connections/limited connections at a time.
2-Caching on Wb Server:it runs the server-side scripts which can cached the response until there is no change in the data since last time it was created for access.It can cached the responses in the seprate cache storage which could be a simple file,a database and caching tools like Redis,Memcached which can save you connecting to database everytime. imagine there are 1000 hits per minute and we update once a day so there is no need to connect to database 1000 time instead you hit the web server and cached the result and when we update the cache so fresh results responded to the hit.No doubt it is saving the processing power and reducing the time but it still has limited capacity to response the request.
3-Caching on reverse proxy server:  No doubt it is saving the processing power and reducing the time but it still has limited capacity to response the request. So reverse proxy server comes over this limitation of web server.Heavily traffic sites use the multiple web servers behind the proxy server to distribute the request the evenly.web servers send the result with appropriate caching headers to the proxy servers and then proxy server cached the result for certain amount of time as mentioned in those headers and served the requests from the cached.In this way the server cannot down with too many requests.Web server and proxy server send the response to the client with caching headers which tells the client that he can cached the result for specific amount of time ,during this time if request is made the  client browser or application decide will use those caching headers ,serve the result from local cache or to create the call to the server.It is good idea that Always use the cache with proper strategy .
Token-based authentication in DRF: since api are the gateway to connect to the backend ,using the api a third party can access the data which can cause the data loss or corruption.Some api’s are used for data distribute and some for data modification which is accessed only by authenticated user.DatabaseApiany client can access
Here we will learn the how to implement the auth in DRF and  then protect the api end points from the public access.Previously we learnt the password based authenticatin  as:
Password-based authentication: ServerApi(username,password and submit)with every api call then these credentials like username and paswrd are authenticated and delivered the appropriate response.Since sending the credentials every time it is frustrated and insecure .
So token-based authentication is most useful and secure and popular method when it comes to authenticate/secure the api .
How it is Done?: in this only once credentials are sent ,if they are ok then server generates the unique string which is long,hard to read,and alphanumerical characters and symbols,Server decides how long it will be valid and when expired ,client send new api request include this token in the header on server side script and then server check the token if it is valid/expired then it checks this token which user it belongs to and match the user.This is done by a authentication class provided by auth app/DRF.if everything is ok then api will run on the behalf of that user and now authentication is done on the base of token.
How to configure this in the project: first add as it this line in the settings.py file under installed apps option’rest_framework.authtoken’ and then create superuser by this command from the terminal in vs code as python manage.py createsuperuser,      after this go to browser and write this url in the search bar as : localhost:8000/adminthis will open the admin panel after usrname and paswrd you will see the token and  user options ,to create the token just go to the token option and create the token by selecting the user for which you have to craeate the token,so in this way we have the token in the token option.
Its time to create the protected end points for api,go to the views.py file and add this code as:
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
@api_view()
@permission_classes(IsAuthenticated)
def secret(request):
    return Response('Message':'save secret message')
and also set the path for this function as path(‘secret/’,views.secret) in subapp urls.py file and this can be tested in any testing tool to check the authentication,also w need to tell the DRF to use the token base authentication,for this go to settings.py file under rest framework option add this code as:
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication'
    ]
And after this copy the token from the admin panel and paste in testing tool by selecting the header as bearer and paste the token and second line write the word Token and that’s it.
This token was generated through admin panel But what if it is created by the end points of api as in code: 
from  rest_framework.authtoken.views import  obtain_auth_token
urlpatterns=[
    path('api-token-auth/',obtain_auth_token)
    ]
And now then again go to the testing tool request the url as localhost:8000/api/api-token-auth
And send the request ,it will ask you in the response the username and password provide the admin username and password in testing tool by selecting the formurlencoded option and send the request,it will generate the token and then use this token to make http .Using built in decorators and classes and user token to authenticate api call ,Backend developer always try to optimize the security of their system.This authentication of api will serve in the api in the project. 
User Roles:we have  already learnt that how to prvent the end points by using token base authentication,but there are still some issue what will be if user hit the end point delete to remove items from menu  .It’s not enough to check the authentication but also authorization.So we can take the benefit of Django built in groups for authorization .
How to do this? Go to the admin panel and from user option create the group and create the users ,after this click on the user that you want to assign to that group by scrolling down with opeoing  of user till the last under permissions having group option there click the available group select It and press the arrow and it will shift to the right box,In this way user will assigned to that group.in this way the foundation of authorization layer has been created.
Lets do this in the code to make it work.this is similar to the above api authentication code:
@permission_classes(IsAuthenticated)
def manager_view(request):
    return Response({'Message':'This Manager should see message only'})
also set the path for this in url.py file.
Now go to the  testing tool and first create the token for each user byusing the process above for api by writing the usrname and password  and after that using those generated tokens by pasting and  writing the keyword Token call the request by providing the path as i.e.localhost:8000/api/manager-view
@permission_classes(IsAuthenticated)
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({'Message':'This Manager should see message only'})
    else:
        return Response({'Message':'you are not authorized'})
        
in this way api end points can be prevent from unauthorized user ,This is the authorization layer creation
Setting up API Throtling:
It is very useful technique to prevent the api abuse, computing power and bandwidth are involved with every request,and if we don’t throtl then api is at risk,with throtlin we can control api access at certain amount of time .Throtling classed are built in in the DRF.
Two types of Throtling1- User  Throtling for Authenticated User(This will be used when there is valid token)  2-Anonymus or for Unauthorized User(this will be used when there is no token in the api header)
also set the path for this and add the following code in the settings.py file under rest framework

from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle       
@api_view()
@throttle_classes([AnonRateThrottle])
def throtile_check(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes([UserRateThrottle])
def user_rate_throttle(request):
    return Response({'Mesage':'successful'})
Also set path for both of them
   'DEFAULT_THROTTLE_RATES':
        {'anon':'2/miute',#here second and day can also be written and it is for unauthenticated user
        'user':'5/minute'#this is for authenticated user
        }
}
This for Unauthenticated user  and  Authenticated User  code.
In somnia or any testing tool provide the valid token and make the request as localhost:8000/throtile_check this wall call api two time per minute after that it show error message.
We can also make some other policies for authenticated user i.e.create throttle.py file and write the code in it as 
from rest_framework.throttling import UserRateThrottle
class TenCallsPerMinute(UserRateThrottle):
    scope='ten'
and now use this code in the views.py file as given being used
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle 
from.throtle import TenCallsPerMinute      
@api_view()
@throttle_classes([AnonRateThrottle])
def throtile_check(request):
    return Response({'Mesage':'successful'})

@api_view()
@throttle_classes([TenCallsPerMinute])
def user_rate_throttle(request):
    return Response({'Mesage':'successful'})
also set the scope in the settings.py file under rest framework as:
    'DEFAULT_THROTTLE_RATES':
        {'anon':'2/miute',#here second and day can also be written and it is for unauthenticated user
        'user':'5/minute',#this is for authenticated user
        'ten':'10/minute'
        }
Introduction to Djoser library for better authentication:
Authentication(Access) and Authorization(Actions) are crucial part in the application ,if it is gone wrong it can cause of data breaches and data corruption,so to do this it is tedious and time consuming task.So we can do it by a library and configure it with just few lines of code to get fully authentication layer for the project in DRF.First  of install the Djoser  library using command pipenv/pip install djoser  and after this open setting.py file and under installed app option set as ‘djoser’ and also create the in this file at the end of code asDJOSER={‘USER_ID_FIELD’:’username’} 
DJOSER={
    'DJOSER_ID_FIELD':'user'
}
And if we want to  login the django admin simulataneously with the browsableapi  of Djoser ,we need to add the session authentication class too in the  as here in the code:
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
We can remove this class before going to production.Now set the path in urls.py file of main app as :
    path('auth/',include('djoser.urls')),    
    path('auth/',include('djoser.urls.authtoken')),
Djoser offers handy end points as:
/users/
/users/me
/users/confirm/
/users/resend_activation/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/
/token/logout/
Some of them supports only get method and some support post,put and delete methods.
These can be accessed as localhost:8000/auth/aboveendpoints/
In somnia I.e.localhost:800/auth//token/login/       also you have to provide the token to access this endpoints. The details of these endpoints can be understood in the browsable api undr the options heading which tells that which method accept the get and post and update etc.
Djoser library also offer  different types of token base authentications which is called JSON WEB TOKEN OR (JWT):
Like the built token system in DRF we can also use the JWT for api authentication .
How to use it?:To use it frst install it by this command as pipenv djangorestframework-simplejwt
After this go to installed app and add as’rest_framework_simplejwt’,       after this add this in the rest_framework option first line in the code  as :
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_simplejwt.authentication.JWTAuthentication'
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
Simplejwt needs some end points so that it can accept the username and password nd generate the jwt token to enable those endpoints open main app urls.py file and add these two lines in path undr urlpattens as :
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include('BookList.urls')),
    path('auth/',include('djoser.urls')),    
    path('auth/',include('djoser.urls.authtoken')),
    path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token',TokenRefreshView.as_view(),name='token_refresh')  
and now test in testing tool by sending the name and password by requesting as localhost:800/api/token,This will return two tokens ,copy and save them which will be used in later in the process. There are two tokens involved in the JWT one is access token which will client use to authenticate the api call and this access token will expire after 5 minutes in simplejwt,SIMPLE_JWT ={‘ACCESS_TOKEN_LIFETIME’:timedelta(minutes=5)}, and the other is refresh token to regenerate the  access token.
As the access token is expired no longer api endpoints will be authenticated but it does not mean that client will login again ,they can generate the access token from previous call of the refresh token and then api end points will be authenticated again.This is security measure with jwt and it is important bcz manually you cant let them to  expire access token ,if you want to prevent regenerating the access token you can blacklist refresh token ,they cant use any more.
Lets copy the access token and paste in the insomnia testing tool under auth option ,select the bearer option from it  and make the request as localhost:8000/api/secret ,after 5 minutes it will expire ,
Lets create it using refresh token by making the post request as localhost:8000/api/token/refresh and select the form in the option,write the refresh and paste the previous saved refresh token  in the insomnia  and hit the send button it will generate the access token,now client can use this token to authenticate the api again .
How to blacklist the refresh token ,remember you cant let jwt to expire the access token,if we want to black the client from generating the  jwt access token ,we can do this by using utility black class provided by the app in simple jwt package,this app will black the user to regenerate the access token any more,so first add this line in the installed apps as:
"rest_framework_simplejwt.token_blacklist",
 To use this app , we have to migrate the some migrations run the command ->python mnage.py migrate and now go to the main urls.py file and to enable the endpoints api use the tokenblacklistview class as:
from rest_framework_simplejwt.views import  TokenObtainPairView,TokenRefreshView,TokenBlacklistView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include('BookList.urls')),
    path('auth/',include('djoser.urls')),    
    path('auth/',include('djoser.urls.authtoken')),
    path('api/token',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/blacklist/',TokenBlacklistView.as_view(),name='token_blacklist') 
again in testing tool make the request using above line endpoint,http post mehtod and select the formurlencoded option and write the refresh nd paste the refresh token and hit the send button ,it will retun the empty json and again make the post request as api/token/refresh by keeping rest option same as in the blacklis request.
So far we have learnt about the built in token base authentication in DRF Djoser,jwt and many more.
User Account management: Here we will learn to build the api endpoint for user registration and login using the above built in token abase apis Authentication in DRF,also create the api for super user to assign the users to group.we will not use the Djoser jwt here in these two apis.
User registration system: This can be a little complicated with playing the DRF but wait we also have added the Djoser library ,this will make the easier things,  as we know Djoser library introduced a few urls as already given above, but we interested in auth user endpoint. If we log in as a super user in Django admin and then browse this post http  /auth/users/ will return the all the users visible to you but other people cant visit this url with valid token ,insomnia paste the token of any user and write the token word,so by this only their name and email will be visible to them by making the http request above url which is auth/users/  but with super user token it will show the all users detail in insomnia during testing,this super user post http request can accept the public email,username and password ,this public email,username and password can be provided during testing in insomnia thorugh making the post http request for /auth/users,so this will return the new created user ,now this is fully functional .So far ,we have created the user registration and login token base apis authentication in DRF.
Now we will create the create the api for super user to assign,Delete, the users to group. Endpoint for this will be http://127.0.0.1:8000/api/groups/manager/users. In insomnia,write this url and provide the token of super user and word token by making it post request. But when this url will be hit by a user with the valid token it will show the error and super user with token will get the access,Below all the provided code is for of api creatd for super user.
@api_view()
@throttle_classes()
def me(request):
    return Response(request.user.email)

from rest_framework.permissions import IsAdminUser
@api_view(['POST'])
@throttle_classes(IsAdminUser)
def manager(request):#gorups/manager/user path for urls.py 
    return Response({'Mesage':'ok'})
api/groups/manager/user for user to make the request
in insomnia use the token previous and token word and send button press.When we will call it with user it will show the error but with super user it will not show the error 
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group
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

this will lookout the username and if it is found it will show the ok message otherwise it will show the error just for super user as make post  the request in the insomnia groups/manager/users and in fromurlencoded option write the super admin username ,we can perform the CRUD operations as above are performed for super user.'''
