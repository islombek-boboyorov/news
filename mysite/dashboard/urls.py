from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category/list/', views.category_list, name="category_list"),
    path('category/add/', views.category_create, name="category_add"),
    path('category/<int:pk>/edit/', views.category_edit, name="category_edit"),
    path('category/<int:pk>/delete/', views.category_delete, name="category_delete"),

    path('author/list/', views.author_list, name="author_list"),
    path('author/add/', views.author_create, name="author_add"),
    path('author/<int:pk>/edit/', views.author_edit, name="author_edit"),
    path('author/<int:pk>/delete/', views.author_delete, name="author_delete"),

    path('news/list/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:pk>/add/', views.news_edit, name="news_edit"),
    path('news/<int:pk>/delete/', views.news_delete, name="news_delete"),

    path('reference/list/', views.reference_list, name="reference_list"),
    path('reference/add/', views.reference_create, name="reference_add"),
    path('reference/<int:pk>/edit/', views.reference_edit, name="reference_edit"),
    path('reference/<int:pk>/delete/', views.reference_delete, name="reference_delete"),
]