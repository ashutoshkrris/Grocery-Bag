from django.urls import path

from bag.views import index

urlpatterns = [
    path('', index, name='index'),
]
