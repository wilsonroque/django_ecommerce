from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    return HttpResponse("<h1>Hello, galera de SBO! - Univesp - Computação PI Grupo 4</h1>")