from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

class AddPostView(generic.CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
    #fields = ["title","content"]



def home(request):
    # context = {
    #     'posts': posts
    # }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})

def news(request):
    return render(request, 'blog/news.html',{'title': 'news'})


