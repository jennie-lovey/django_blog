from django.shortcuts import render
from  django.views.generic import ListView,DetailView,CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'author','body']
    template_name='blog_create.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
