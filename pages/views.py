from django.shortcuts import render
from .models import page
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def Page(request,slug):

    page1 = page.objects.get(slug=slug)

    return render(request, 'pages/page.html', {
    
        "page": page1
    })