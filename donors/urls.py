from django.urls import path
from .import views
urlpatterns = [
    path('add-donor', views.add_donor, name='add-donor'),
    path('', views.donor_list, name='home'),
    path('filtered-donors/', views.filtered_donors, name='filtered-donors'),
]