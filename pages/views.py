from django.shortcuts import render

from django.views.generic import ListView
from .models import Post
from django.views.generic import TemplateView

class HomePageView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'all_posts_list'

class AboutPageView(TemplateView):
	template_name = 'about.html'