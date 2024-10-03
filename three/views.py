from django.http import HttpResponse
from django.shortcuts import render

def one(request):
    return HttpResponse('one_one')

def two(request):
    return HttpResponse('three_two')

def three(request):
    return HttpResponse('three_three')