from django.urls import path
from one.views import one, two, three, startpage

urlpatterns = [
    path('', startpage),
    path('one_one', one),
    path('one_two', two),
    path('one_three', three)
]