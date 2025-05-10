from django.urls import path
from .import views
urlpatterns = [
    path('add-product', views.add_product, name='add-product'),
    path('search/', views.product_search, name='product_search'),

    path('search/', views.product_search, name='product_search'),

]