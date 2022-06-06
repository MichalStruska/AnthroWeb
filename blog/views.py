from django.shortcuts import render

posts = [
    {
        'author': 'Corey',
        'title': 'Blog post',
        'content': 'first post',
        'date_posted': '9. 5. 2021'
    },
    {
        'author': 'Mike',
        'title': 'Shit post',
        'content': 'second post',
        'date_posted': '25. 5. 2021'
    },
    {
        'author': 'Ken',
        'title': 'another post',
        'content': 'another post',
        'date_posted': '27. 2. 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'about'})

def news(request):
    return render(request, 'blog/news.html',{'title': 'news'})


