from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('<int:category_id>/category/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('<int:news_id>/view/', views.view, name="view"),
]
