from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages

from .forms import PostModelForm
from .models import Post, Author

# Create your views here.


def posts_list(request):
	all_posts= Post.objects.all()
	context= {
	      'all_posts': all_posts
	}
	templates= "posts/posts_list.html"
	messages.info(request, 'Here are all the current blog posts.')
	return render(request,templates,context)

def posts_detail(request, slug):
	unique_post= get_object_or_404(Post, slug=slug)
	context= {
	      'post': unique_post
	}
	templates= "posts/posts_detail.html"
	messages.info(request, 'This is specific detailed view')
	return render(request,templates,context)

def posts_create(request):
	author, created = Author.objects.get_or_create(
		user=request.user,
		#email=request.user.email,
		mobile_num=7380803468)
	form = PostModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.instance.author = author
		form.save()
		messages.info(request, 'Successfully Created a new blog post.')
		return redirect('/')
	context = {
	    'form': form
	}
	templates = "posts/posts_create.html"
	return render(request,templates,context)


def posts_update(request, slug):
	unique_post= get_object_or_404(Post, slug=slug)
	form = PostModelForm(request.POST or None,
	                     request.FILES or None,
	                     instance= unique_post)
	if form.is_valid():
		form.save()
		messages.info(request, 'Successfully updated your blog post.')
		return redirect('/')
	context = {
	    'form': form
	}
	templates= "posts/posts_create.html"
	return render(request,templates,context)	

def posts_delete(request, slug):	
	unique_post= get_object_or_404(Post, slug=slug)
	unique_post.delete()
	messages.info(request, 'Successfully deleted blog posts.')
	return redirect('/')

def home(request):
		context= {}
		template = 'posts/home.html'
		return render(request, template, context)

def about(request):
		context= {}
		template = 'posts/about.html'
		return render(request, template, context)
@login_required
def userProfile(request):
		user = request.user
		context= {'user': user}
		template = 'posts/profile.html'
		return render(request, template, context)		
							

			

