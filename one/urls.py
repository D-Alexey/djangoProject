from django.urls import path
from one.views import index, two, three, startpage

urlpatterns = [
    path('', startpage),
    path('one_index', index),
    path('one_two', two),
    path('one_three', three)
]