from pages.models import page

def get_pages(request):

    pages = page.objects.filter(visible=True).order_by('order').values_list('id','title','slug')

    return {
        'pages':pages
    }