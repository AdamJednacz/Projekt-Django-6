from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('cheapest/', views.cheapest, name='cheapest'),
    path('products_list/', views.products_list, name='products_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),

]