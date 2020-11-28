from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello (request,name='world',digit=None):
    if digit is not None:
        return HttpResponse(f" Digit is {digit}")
    return HttpResponse (f'Hello {name}')

def buy_book (request):
    return HttpResponse ('Books')