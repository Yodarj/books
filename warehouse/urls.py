'''url'''
from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('list_of_books/', views.listpage, name="list"),
    path('add/', views.addpage, name="add"),
    path('import/', views.importpage, name="import"),
    path('list_of_books/results/', views.search, name='search'),
    path('added/', views.bookaddedpage, name="bookadded")
]
