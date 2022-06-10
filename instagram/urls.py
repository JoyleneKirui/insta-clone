from django.urls import path
from instagram import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newpost', views.NewPost, name='newpost'),
    # path('<uuid:post_id>', PostDetail, name='post-details'),
    # path('tag/<slug:tag_slug>', Tags, name='tags'),
    # path('<uuid:post_id>/like', like, name='like'),
    # path('<uuid:post_id>/favourite', favourite, name='favourite'),

]

