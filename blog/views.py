from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm, EditForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    #fields = ["title","content"]

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    #fields = ['title', 'content']

class DeletePostView(generic.DeleteView):
    model = Post
    template_name: str = 'blog/delete_post.html'

def home(request):
    # context = {
    #     'posts': posts
    # }
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})

def news(request):
    return render(request, 'blog/news.html',{'title': 'news'})

def delete_post(request, id):
    post = Post.objects.filter(id=id)
    address.delete()
    return redirect('/home')

def delete(request, id):
  member = Post.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('blog-home'))

# def delete_post(request,post_id=None):
#     post_to_delete=Post.objects.get(id=post_id)
#     post_to_delete.delete()
#     return HttpResponseRedirect(home())

