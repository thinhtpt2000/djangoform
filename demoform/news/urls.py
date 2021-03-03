from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add'),
    path('save/', views.save_post, name='save'),
]