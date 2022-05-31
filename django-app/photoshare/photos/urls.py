from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photos/<str:pk>/', views.viewphotos, name='photos'),
    path('add', views.addphotos, name='add'),
]
