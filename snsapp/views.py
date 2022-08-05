from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class Login(LoginView):
    template_name ='login.html'

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

class DetailPost(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'    

class DetaPost(LoginRequiredMixin, DetailView):
    #投稿詳細ページ
    model = Post
    template_name = 'detail.html'

class CreatePost(LoginRequiredMixin, CreateView):
    #投稿フォーム
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('mypost')

    def form_valid(self, form):
        #投稿ユーザーをリクエストユーザーと紐付け
        form.instance.user = self.request.user 
        return super().form_valid(form)   
       