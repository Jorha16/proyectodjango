from django.shortcuts import render
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def list(request):

    articles = Article.objects.all()
    
    return render(request,'articles/list.html',{
        'title':'Articles',
        'articles': articles
    })