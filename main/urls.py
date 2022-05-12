from django.urls import path
from .views import homeView, listView

urlpatterns = [
    path('', homeView, name='home'),
    path('list/', listView, name='data-list'),
]