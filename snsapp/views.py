from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.

class Home(LoginRequiredMixin, ListView):
    #Homeページで、自分以外のユーザー投稿をリスト表示
    model = Post
    template_name = 'list.html'

    def get_queryset(self):
        return Post.objects.exclude(user=self.request.user)

class MyPost(LoginRequiredMixin, ListView):
    #自分の投稿のみ表示
    model = Post
    template_name = 'list.html'

    def getqueryset(self):
        return Post.objects.filter(user=self.request.user)        