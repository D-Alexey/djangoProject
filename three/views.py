from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('two_index')

def two(request):
    return HttpResponse('two_two')

def three(request):
    return HttpResponse('two_three')