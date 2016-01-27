from django.shortcuts import render
from django.shortcuts import HttpResponse

def post_create(request):
	return HttpResponse('<h1>Create</h1>')

def post_detail(request):
	context = {
		'title' : 'dim details',
		'h1' : 'Detail'
	}
	return render(request, 'index.html', context)

def post_list(request):
	if request.user.is_authenticated():
		uname = request.user.username
		context = {
			'title' : 'Hi {}'.format(uname),
			'h1' : 'Welcome to your list {}'.format(uname)
	 	}
 	else:
 		context = {
			'title' : 'Welcome',
			'h1' : 'Please login'
	 	}
	return render(request, 'index.html', context)

def post_update(request):
	return HttpResponse('<h1>Update</h1>')

def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
