from msilib.schema import ListView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
        return context

class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'
    #fields = ["title","content"]

class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'

class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    #fields = ['title', 'content']

class DeletePostView(generic.DeleteView):
    model = Post
    template_name: str = 'blog/delete_post.html'

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats, status=1)
    return render(request, 'blog/categories.html', {'cats':cats, 'category_posts':category_posts})

# def home(request):
#     # context = {
#     #     'posts': posts
#     # }
#     return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})

def news(request):
    return render(request, 'blog/news.html',{'title': 'news'})

def delete_post(request, id):
    
    post = Post.objects.filter(id=id)
    address.delete()
    return redirect('/home')

def delete(request, id):
  #if request.user.id == request.post.author.id:
    member = Post.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('blog-home'))

# def delete_post(request,post_id=None):
#     post_to_delete=Post.objects.get(id=post_id)
#     post_to_delete.delete()
#     return HttpResponseRedirect(home())

