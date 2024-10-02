from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('three_index')

def two(request):
    return HttpResponse('three_two')

def three(request):
    return HttpResponse('three_three')