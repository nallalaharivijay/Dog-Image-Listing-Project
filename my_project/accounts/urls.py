from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', search , name='search'),
    path('lists/', lists, name='lists'),
    path('delete_list/<int:list_id>/', delete_list, name='delete_list'),
    path('lists/<int:list_id>/', view_list, name='view_list'),
]
