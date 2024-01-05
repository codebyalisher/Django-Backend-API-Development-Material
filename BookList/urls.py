from django.urls import  path
from.import views,decorators,pagination,administration
from  rest_framework.authtoken.views import  obtain_auth_token

urlpatterns=[
    #path('books/',views.books),
    path('book/<int:pk>',decorators.Book.as_view()),#ok
    path('Books/',decorators.BookList.as_view()),#ok
    path('menuitemsview/',pagination.MenuItemsView.as_view()),
    path('singlemenuitemview/<int:pk>',pagination.SingleMenuItemView.as_view()),
    path('menuitems/',pagination.menu_items),
    path('singleitem/<int:pk>',pagination.single_item),
    path('secret/',administration.secret),
    path('manager-view/',administration.manager_view),
    path('throtle-check/',views.throtile_check),#ok
    path('user-rate-throttle/',views.user_rate_throttle),#ok
    path('api-token-auth/',obtain_auth_token)
    ]