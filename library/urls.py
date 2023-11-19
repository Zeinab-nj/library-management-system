from django.urls import path
from . import views 


app_name = "library"

urlpatterns = [
    path('',views.index,name='index'),
    path('book/',views.book_list,name='book_list'),
    path('book/<int:id>',views.book_status,name='book_status'),
]
