from django.urls import path
from two.views import one, two, three

urlpatterns = [
    path('two_index', one),
    path('two_two', two),
    path('two_three', three)
]