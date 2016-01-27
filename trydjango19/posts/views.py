from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from .models import Post

def post_create(request):
	return HttpResponse('<h1>Create</h1>')

def post_detail(request, id=None):
	instance = get_object_or_404 (Post, id=id)
	context = {
		'title' : 'Details',
		'instance' : instance,
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	if request.user.is_authenticated():
		uname = request.user.username
		queryset = Post.objects.all()
		context = {
			'title' : 'Hi {}'.format(uname),
			'h1' : 'Welcome to your list {}'.format(uname),
			'list' : queryset,
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
