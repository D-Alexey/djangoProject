from django.http import HttpResponse
from django.shortcuts import render

def startpage(request):
    return HttpResponse('Startpage')

def one(request):
    return HttpResponse('one_one')

def two(request):
    return HttpResponse('one_two')

def three(request):
    return HttpResponse('one_three')