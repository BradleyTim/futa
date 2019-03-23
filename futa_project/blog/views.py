from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'id': 1,
		'text': 'Post One'
	},
	{
		'id': 2,
		'text': 'Post Two'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/index.html', context)

def about(request):
	return render(request, 'blog/about.html')

