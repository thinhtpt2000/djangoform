from django.urls import path


urlpatterns = [
    path('news/', include('news.urls')),
]