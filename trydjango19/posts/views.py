from django.shortcuts import (
	render,
	HttpResponse,
	HttpResponseRedirect,
	get_object_or_404,
)

from .models import Post

from .forms import PostForm

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'form' : form,
	}
	return render(request, 'post_form.html', context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
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

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'form' : form,
		'instance': instance,
	}
	return render(request, 'post_form.html', context)

def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
