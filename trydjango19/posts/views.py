from django.shortcuts import (
	render,
	HttpResponse,
	HttpResponseRedirect,
	get_object_or_404,
	redirect,
)

from .models import Post

from .forms import PostForm

from django.contrib import messages

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "successfully created")
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
		messages.success(request, "successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		'form' : form,
		'instance': instance,
	}
	return render(request, 'post_form.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect('posts:list')
