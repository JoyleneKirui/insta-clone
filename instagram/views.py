
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from instagram.models import Post, Tag, Follow, Stream, Likes

def index(request):
    user = request.user
    
    group_ids = []

    
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context = {
            'post_items': post_items,
            
        }
    return render(request, 'index.html', context)


