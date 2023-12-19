from django.urls import  path
from.import views
from  rest_framework.authtoken.views import  obtain_auth_token

urlpatterns=[
    #path('books/',views.books),
    path('book/<int:pk>',views.Book.as_view()),
    path('Books/',views.BookList.as_view()),
    path('menu-items',views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>',views.SingleMenuItemView.as_view()),
    path('menu-items',views.menu_items),
    path('menu-items/<int:pk>',views.single_item),
    path('secret/',views.secret),
    path('manager-view/',views.manager_view),
    path('throtle-check',views.throtile_check),
    path('user-rate-throttle',views.user_rate_throttle),
    path('api-token-auth/',obtain_auth_token)
    ]