from django.http import HttpResponse
from django.shortcuts import render

def one(request):
    return HttpResponse('two_one')

def two(request):
    return HttpResponse('two_two')

def three(request):
    return HttpResponse('two_three')