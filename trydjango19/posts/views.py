from django.shortcuts import render
from django.shortcuts import HttpResponse

def posts_home(request):
	return HttpResponse("<h1>Hello</h1>")
